#!/usr/bin/env python3
"""Deterministic skill.zip builder with SBOM and provenance sidecars.

The ZIP uses stored entries, fixed timestamps, normalized permissions, and
canonical ordering. SBOM/provenance are release sidecars so their digests can
refer to the final archive without creating checksum cycles.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import zipfile
from dataclasses import dataclass
from pathlib import Path

FIXED_ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
MANIFEST_NAME = "PACKAGE-MANIFEST.json"
FORMAT_VERSION = 1
SBOM_FILENAME = "skill.sbom.cdx.json"
PROVENANCE_FILENAME = "skill.provenance.json"

EXCLUDED_DIRS = {
    ".git", ".github-cache", ".mypy_cache", ".pytest_cache", ".ruff_cache",
    ".tox", ".venv", ".idea", ".vscode", "__pycache__", "node_modules",
    "dist", "build",
}
EXCLUDED_FILES = {
    ".DS_Store", "Thumbs.db", ".coverage", "skill.zip", "skill.zip.sha256",
    "skill-package-manifest.json", SBOM_FILENAME, PROVENANCE_FILENAME,
}
EXCLUDED_SUFFIXES = {".pyc", ".pyo", ".tmp", ".temp", ".swp", ".swo", ".bak"}


@dataclass(frozen=True)
class PackageEntry:
    path: str
    size: int
    sha256: str


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_json_bytes(payload: dict) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def is_temporary_name(name: str) -> bool:
    return name.startswith(".#") or name.endswith("~")


def should_exclude(relative: Path) -> bool:
    if any(part in EXCLUDED_DIRS for part in relative.parts[:-1]):
        return True
    name = relative.name
    return name in EXCLUDED_FILES or is_temporary_name(name) or relative.suffix.lower() in EXCLUDED_SUFFIXES


def collect_source_files(root: Path, output: Path | None = None) -> list[Path]:
    root = root.resolve()
    output_resolved = output.resolve() if output else None
    files: list[Path] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in relative.parts):
            continue
        if path.is_symlink():
            raise ValueError(f"symbolic links are not allowed in packages: {relative.as_posix()}")
        if not path.is_file() or should_exclude(relative):
            continue
        if output_resolved is not None and path.resolve() == output_resolved:
            continue
        files.append(path)
    return sorted(files, key=lambda p: p.relative_to(root).as_posix())


def build_manifest(root: Path, files: list[Path]) -> dict:
    entries = []
    for path in files:
        data = path.read_bytes()
        entries.append(PackageEntry(path.relative_to(root).as_posix(), len(data), sha256_bytes(data)).__dict__)
    return {
        "format": "ui-morphism-skill-package",
        "format_version": FORMAT_VERSION,
        "hash_algorithm": "sha256",
        "file_count": len(entries),
        "files": entries,
    }


def load_skill_metadata(root: Path) -> dict:
    path = root / "skill.json"
    if not path.is_file():
        return {"name": "ui-morphism-design", "version": "unknown"}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"name": "ui-morphism-design", "version": "unknown"}
    return {"name": str(data.get("name", "ui-morphism-design")), "version": str(data.get("version", "unknown"))}


def build_sbom(root: Path, manifest: dict) -> dict:
    metadata = load_skill_metadata(root)
    components = []
    for entry in manifest["files"]:
        components.append({
            "type": "file",
            "name": entry["path"],
            "bom-ref": f"file:{entry['sha256']}",
            "hashes": [{"alg": "SHA-256", "content": entry["sha256"]}],
            "properties": [{"name": "ui-morphism:size", "value": str(entry["size"])}],
        })
    return {
        "bomFormat": "CycloneDX",
        "specVersion": "1.6",
        "serialNumber": f"urn:uuid:{sha256_bytes(canonical_json_bytes(manifest))[:32]}",
        "version": 1,
        "metadata": {
            "component": {
                "type": "application",
                "name": metadata["name"],
                "version": metadata["version"],
                "bom-ref": f"pkg:generic/{metadata['name']}@{metadata['version']}",
            },
            "tools": {"components": [{"type": "application", "name": "ui-morphism-skill-packager", "version": "1.0.0"}]},
        },
        "components": components,
    }


def build_provenance(root: Path, output: Path, archive_sha256: str, manifest_bytes: bytes, sbom_bytes: bytes, source: dict | None = None) -> dict:
    metadata = load_skill_metadata(root)
    source = source or {}
    return {
        "_type": "https://in-toto.io/Statement/v1",
        "subject": [{"name": output.name, "digest": {"sha256": archive_sha256}}],
        "predicateType": "https://slsa.dev/provenance/v1",
        "predicate": {
            "buildDefinition": {
                "buildType": "https://github.com/thanhtupppp/ui-morphism-design-skills/deterministic-skill-package/v1",
                "externalParameters": {
                    "package": metadata,
                    "source": {
                        "repository": source.get("repository", ""),
                        "ref": source.get("ref", ""),
                        "revision": source.get("revision", ""),
                    },
                },
                "resolvedDependencies": [],
            },
            "runDetails": {
                "builder": {"id": source.get("builder_id", "ui-morphism-skill-packager/1.0.0")},
                "metadata": {"invocationId": source.get("invocation_id", "")},
            },
            "byproducts": [
                {"name": "skill-package-manifest.json", "digest": {"sha256": sha256_bytes(manifest_bytes)}},
                {"name": SBOM_FILENAME, "digest": {"sha256": sha256_bytes(sbom_bytes)}},
            ],
        },
    }


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(filename=name, date_time=FIXED_ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_STORED
    info.create_system = 3
    info.external_attr = (stat.S_IFREG | 0o644) << 16
    info.flag_bits |= 0x800
    return info


def write_member(archive: zipfile.ZipFile, name: str, data: bytes) -> None:
    archive.writestr(zip_info(name), data)


def default_source_context() -> dict:
    server = os.getenv("GITHUB_SERVER_URL", "https://github.com")
    repository = os.getenv("GITHUB_REPOSITORY", "")
    return {
        "repository": f"{server}/{repository}" if repository else "",
        "ref": os.getenv("GITHUB_REF", ""),
        "revision": os.getenv("GITHUB_SHA", ""),
        "invocation_id": os.getenv("GITHUB_RUN_ID", ""),
        "builder_id": "github-actions" if os.getenv("GITHUB_ACTIONS") == "true" else "ui-morphism-skill-packager/1.0.0",
    }


def build_package(root: Path, output: Path, source: dict | None = None) -> dict:
    root = root.resolve()
    output = output.resolve()
    if not (root / "SKILL.md").is_file():
        raise ValueError("package root must contain SKILL.md")

    files = collect_source_files(root, output)
    manifest = build_manifest(root, files)
    manifest_bytes = canonical_json_bytes(manifest)

    output.parent.mkdir(parents=True, exist_ok=True)
    temp_output = output.with_name(output.name + ".tmp")
    try:
        with zipfile.ZipFile(temp_output, "w", compression=zipfile.ZIP_STORED, allowZip64=True) as archive:
            for path in files:
                write_member(archive, path.relative_to(root).as_posix(), path.read_bytes())
            write_member(archive, MANIFEST_NAME, manifest_bytes)
        os.replace(temp_output, output)
    finally:
        if temp_output.exists():
            temp_output.unlink()

    checksum = sha256_file(output)
    sbom = build_sbom(root, manifest)
    sbom_bytes = canonical_json_bytes(sbom)
    provenance = build_provenance(root, output, checksum, manifest_bytes, sbom_bytes, source or default_source_context())
    provenance_bytes = canonical_json_bytes(provenance)

    sidecar_manifest = output.with_name("skill-package-manifest.json")
    sidecar_checksum = output.with_name(output.name + ".sha256")
    sidecar_sbom = output.with_name(SBOM_FILENAME)
    sidecar_provenance = output.with_name(PROVENANCE_FILENAME)
    sidecar_manifest.write_bytes(manifest_bytes)
    sidecar_checksum.write_text(f"{checksum}  {output.name}\n", encoding="utf-8", newline="\n")
    sidecar_sbom.write_bytes(sbom_bytes)
    sidecar_provenance.write_bytes(provenance_bytes)

    return {
        "archive": str(output),
        "sha256": checksum,
        "manifest": manifest,
        "manifest_path": str(sidecar_manifest),
        "checksum_path": str(sidecar_checksum),
        "sbom": sbom,
        "sbom_path": str(sidecar_sbom),
        "provenance": provenance,
        "provenance_path": str(sidecar_provenance),
    }


def run_cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build deterministic skill.zip with SBOM and provenance")
    parser.add_argument("--root", default=".")
    parser.add_argument("--output", default="skill.zip")
    parser.add_argument("--json", action="store_true", dest="json_output")
    args = parser.parse_args(argv)
    result = build_package(Path(args.root), Path(args.output))
    payload = {
        "archive": result["archive"],
        "sha256": result["sha256"],
        "file_count": result["manifest"]["file_count"],
        "manifest": result["manifest_path"],
        "sbom": result["sbom_path"],
        "provenance": result["provenance_path"],
    }
    if args.json_output:
        print(json.dumps(payload, sort_keys=True))
    else:
        print(f"Built {payload['archive']}")
        print(f"SHA-256 {payload['sha256']}")
        print(f"Files {payload['file_count']}")
        print(f"SBOM {payload['sbom']}")
        print(f"Provenance {payload['provenance']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run_cli())
