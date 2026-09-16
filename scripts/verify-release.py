#!/usr/bin/env python3
"""Verify the release artifact graph for a deterministic Skill package."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path

REQUIRED = (
    "skill.zip",
    "skill.zip.sha256",
    "skill-package-manifest.json",
    "skill.sbom.cdx.json",
    "skill.provenance.json",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_release(root: Path, expected_revision: str | None = None) -> dict:
    root = root.resolve()
    errors: list[str] = []
    paths = {name: root / name for name in REQUIRED}
    for name, path in paths.items():
        if not path.is_file():
            errors.append(f"missing release artifact: {name}")
    if errors:
        return {"ok": False, "errors": errors}

    archive = paths["skill.zip"]
    archive_digest = sha256_file(archive)
    expected_checksum = f"{archive_digest}  skill.zip\n"
    if paths["skill.zip.sha256"].read_text(encoding="utf-8") != expected_checksum:
        errors.append("skill.zip.sha256 does not match skill.zip")

    try:
        manifest = json.loads(paths["skill-package-manifest.json"].read_text(encoding="utf-8"))
        sbom = json.loads(paths["skill.sbom.cdx.json"].read_text(encoding="utf-8"))
        provenance = json.loads(paths["skill.provenance.json"].read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"ok": False, "errors": errors + [f"invalid JSON sidecar: {exc}"]}

    with zipfile.ZipFile(archive) as zf:
        names = set(zf.namelist())
        if "PACKAGE-MANIFEST.json" not in names:
            errors.append("skill.zip is missing PACKAGE-MANIFEST.json")
        else:
            embedded = json.loads(zf.read("PACKAGE-MANIFEST.json"))
            if embedded != manifest:
                errors.append("embedded PACKAGE-MANIFEST.json differs from sidecar manifest")
        for entry in manifest.get("files", []):
            name = entry.get("path", "")
            if name not in names:
                errors.append(f"manifest entry missing from archive: {name}")
                continue
            data = zf.read(name)
            if len(data) != entry.get("size"):
                errors.append(f"manifest size mismatch: {name}")
            if hashlib.sha256(data).hexdigest() != entry.get("sha256"):
                errors.append(f"manifest digest mismatch: {name}")

    if sbom.get("bomFormat") != "CycloneDX" or sbom.get("specVersion") != "1.6":
        errors.append("SBOM must be CycloneDX 1.6")
    sbom_files = {
        component.get("name"): next((h.get("content") for h in component.get("hashes", []) if h.get("alg") == "SHA-256"), None)
        for component in sbom.get("components", [])
        if component.get("type") == "file"
    }
    for entry in manifest.get("files", []):
        if sbom_files.get(entry["path"]) != entry["sha256"]:
            errors.append(f"SBOM digest mismatch: {entry['path']}")

    subjects = provenance.get("subject", [])
    subject_digest = subjects[0].get("digest", {}).get("sha256") if subjects else None
    if subject_digest != archive_digest:
        errors.append("provenance subject digest does not match skill.zip")

    predicate = provenance.get("predicate", {})
    byproducts = {
        item.get("name"): item.get("digest", {}).get("sha256")
        for item in predicate.get("byproducts", [])
    }
    manifest_digest = sha256_file(paths["skill-package-manifest.json"])
    sbom_digest = sha256_file(paths["skill.sbom.cdx.json"])
    if byproducts.get("skill-package-manifest.json") != manifest_digest:
        errors.append("provenance manifest byproduct digest mismatch")
    if byproducts.get("skill.sbom.cdx.json") != sbom_digest:
        errors.append("provenance SBOM byproduct digest mismatch")

    revision = (
        predicate.get("buildDefinition", {})
        .get("externalParameters", {})
        .get("source", {})
        .get("revision", "")
    )
    if expected_revision is not None and revision != expected_revision:
        errors.append(f"provenance revision mismatch: expected {expected_revision}, found {revision or '<empty>'}")

    return {
        "ok": not errors,
        "errors": errors,
        "archive_sha256": archive_digest,
        "manifest_files": manifest.get("file_count", 0),
        "sbom_components": len(sbom.get("components", [])),
        "provenance_revision": revision,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify skill release artifacts")
    parser.add_argument("root", nargs="?", default="release-a")
    parser.add_argument("--expected-revision")
    parser.add_argument("--output")
    args = parser.parse_args()
    report = verify_release(Path(args.root), args.expected_revision)
    payload = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        Path(args.output).write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
