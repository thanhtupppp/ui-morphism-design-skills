#!/usr/bin/env python3
"""Deterministic skill.zip builder.

The builder intentionally uses ZIP_STORED rather than DEFLATE so identical
source bytes produce identical archive bytes independent of zlib versions.
Archive metadata, ordering, permissions, and timestamps are normalized.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

FIXED_ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
MANIFEST_NAME = "PACKAGE-MANIFEST.json"
FORMAT_VERSION = 1

EXCLUDED_DIRS = {
    ".git",
    ".github-cache",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".tox",
    ".venv",
    ".idea",
    ".vscode",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
}
EXCLUDED_FILES = {
    ".DS_Store",
    "Thumbs.db",
    ".coverage",
    "skill.zip",
    "skill.zip.sha256",
    "skill-package-manifest.json",
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


def is_temporary_name(name: str) -> bool:
    return name.startswith(".#") or name.endswith("~")


def should_exclude(relative: Path) -> bool:
    parts = relative.parts
    if any(part in EXCLUDED_DIRS for part in parts[:-1]):
        return True
    name = relative.name
    return (
        name in EXCLUDED_FILES
        or is_temporary_name(name)
        or relative.suffix.lower() in EXCLUDED_SUFFIXES
    )


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
        entries.append(
            PackageEntry(
                path=path.relative_to(root).as_posix(),
                size=len(data),
                sha256=sha256_bytes(data),
            ).__dict__
        )
    return {
        "format": "ui-morphism-skill-package",
        "format_version": FORMAT_VERSION,
        "hash_algorithm": "sha256",
        "file_count": len(entries),
        "files": entries,
    }


def canonical_json_bytes(payload: dict) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(filename=name, date_time=FIXED_ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_STORED
    info.create_system = 3
    info.external_attr = (stat.S_IFREG | 0o644) << 16
    info.flag_bits |= 0x800
    return info


def write_member(archive: zipfile.ZipFile, name: str, data: bytes) -> None:
    archive.writestr(zip_info(name), data)


def build_package(root: Path, output: Path) -> dict:
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
    sidecar_manifest = output.with_name("skill-package-manifest.json")
    sidecar_checksum = output.with_name(output.name + ".sha256")
    sidecar_manifest.write_bytes(manifest_bytes)
    sidecar_checksum.write_text(f"{checksum}  {output.name}\n", encoding="utf-8", newline="\n")
    return {
        "archive": str(output),
        "sha256": checksum,
        "manifest": manifest,
        "manifest_path": str(sidecar_manifest),
        "checksum_path": str(sidecar_checksum),
    }


def run_cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build deterministic skill.zip")
    parser.add_argument("--root", default=".")
    parser.add_argument("--output", default="skill.zip")
    parser.add_argument("--json", action="store_true", dest="json_output")
    args = parser.parse_args(argv)
    result = build_package(Path(args.root), Path(args.output))
    if args.json_output:
        print(json.dumps({"archive": result["archive"], "sha256": result["sha256"], "file_count": result["manifest"]["file_count"]}, sort_keys=True))
    else:
        print(f"Built {result['archive']}")
        print(f"SHA-256 {result['sha256']}")
        print(f"Files {result['manifest']['file_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run_cli())
