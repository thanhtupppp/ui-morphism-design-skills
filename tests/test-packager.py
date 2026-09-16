#!/usr/bin/env python3
"""Regression tests for deterministic skill.zip release artifacts."""
import hashlib
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import skill_packager as packager

SOURCE = {
    "repository": "https://github.com/example/ui-morphism-design-skills",
    "ref": "refs/heads/test",
    "revision": "0123456789abcdef",
    "invocation_id": "test-run-1",
    "builder_id": "test-builder",
}


def make_source(root: Path) -> None:
    (root / "references").mkdir(parents=True)
    (root / "agents").mkdir(parents=True)
    (root / "SKILL.md").write_text("---\nname: test-skill\ndescription: A deterministic package fixture used for regression testing.\n---\n# Test Skill\n", encoding="utf-8")
    (root / "references" / "guide.md").write_text("# Guide\nStable content.\n", encoding="utf-8")
    (root / "agents" / "openai.yaml").write_text('interface:\n  display_name: "Test Skill"\n  short_description: "Test deterministic packaging."\n', encoding="utf-8")
    (root / "skill.json").write_text(json.dumps({"name": "test-skill", "version": "1.9.0"}), encoding="utf-8")


class PackagerTests(unittest.TestCase):
    def test_same_source_produces_same_archive_checksum_manifest_sbom_and_provenance(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "source"; root.mkdir(); make_source(root)
            first = packager.build_package(root, Path(td) / "one" / "skill.zip", SOURCE)
            second = packager.build_package(root, Path(td) / "two" / "skill.zip", SOURCE)
            self.assertEqual(first["sha256"], second["sha256"])
            self.assertEqual(Path(first["archive"]).read_bytes(), Path(second["archive"]).read_bytes())
            self.assertEqual(first["manifest"], second["manifest"])
            self.assertEqual(first["sbom"], second["sbom"])
            self.assertEqual(first["provenance"], second["provenance"])

    def test_manifest_matches_packaged_file_bytes(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "source"; root.mkdir(); make_source(root)
            result = packager.build_package(root, Path(td) / "skill.zip", SOURCE)
            with zipfile.ZipFile(result["archive"]) as archive:
                embedded = json.loads(archive.read(packager.MANIFEST_NAME))
                self.assertEqual(result["manifest"], embedded)
                self.assertEqual(embedded["file_count"], len(embedded["files"]))
                for entry in embedded["files"]:
                    data = archive.read(entry["path"])
                    self.assertEqual(entry["size"], len(data))
                    self.assertEqual(entry["sha256"], hashlib.sha256(data).hexdigest())

    def test_git_cache_temporary_and_release_sidecars_are_excluded(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "source"; root.mkdir(); make_source(root)
            (root / ".git" / "objects").mkdir(parents=True); (root / ".git" / "objects" / "x").write_text("secret")
            (root / "scripts" / "__pycache__").mkdir(parents=True); (root / "scripts" / "__pycache__" / "x.pyc").write_bytes(b"cache")
            for name in ("notes.tmp", "draft.md~", packager.SBOM_FILENAME, packager.PROVENANCE_FILENAME):
                (root / name).write_text("temporary")
            result = packager.build_package(root, Path(td) / "skill.zip", SOURCE)
            with zipfile.ZipFile(result["archive"]) as archive:
                names = archive.namelist()
            self.assertFalse(any(name.startswith(".git/") or "__pycache__" in name for name in names))
            for name in ("notes.tmp", "draft.md~", packager.SBOM_FILENAME, packager.PROVENANCE_FILENAME):
                self.assertNotIn(name, names)

    def test_checksum_sidecar_matches_archive(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "source"; root.mkdir(); make_source(root)
            result = packager.build_package(root, Path(td) / "skill.zip", SOURCE)
            actual = hashlib.sha256(Path(result["archive"]).read_bytes()).hexdigest()
            self.assertEqual(actual, result["sha256"])
            self.assertEqual(f"{actual}  skill.zip\n", Path(result["checksum_path"]).read_text(encoding="utf-8"))

    def test_sbom_is_cyclonedx_and_covers_manifest_files(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "source"; root.mkdir(); make_source(root)
            result = packager.build_package(root, Path(td) / "skill.zip", SOURCE)
            sbom = json.loads(Path(result["sbom_path"]).read_text(encoding="utf-8"))
            self.assertEqual("CycloneDX", sbom["bomFormat"])
            self.assertEqual("1.6", sbom["specVersion"])
            self.assertEqual("test-skill", sbom["metadata"]["component"]["name"])
            self.assertEqual("1.9.0", sbom["metadata"]["component"]["version"])
            expected = {entry["path"]: entry["sha256"] for entry in result["manifest"]["files"]}
            actual = {component["name"]: component["hashes"][0]["content"] for component in sbom["components"]}
            self.assertEqual(expected, actual)

    def test_provenance_links_archive_manifest_sbom_and_source(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "source"; root.mkdir(); make_source(root)
            result = packager.build_package(root, Path(td) / "skill.zip", SOURCE)
            provenance = json.loads(Path(result["provenance_path"]).read_text(encoding="utf-8"))
            self.assertEqual("https://in-toto.io/Statement/v1", provenance["_type"])
            self.assertEqual("https://slsa.dev/provenance/v1", provenance["predicateType"])
            self.assertEqual(result["sha256"], provenance["subject"][0]["digest"]["sha256"])
            source = provenance["predicate"]["buildDefinition"]["externalParameters"]["source"]
            self.assertEqual(SOURCE["repository"], source["repository"])
            self.assertEqual(SOURCE["revision"], source["revision"])
            byproducts = {item["name"]: item["digest"]["sha256"] for item in provenance["predicate"]["byproducts"]}
            self.assertEqual(packager.sha256_file(Path(result["manifest_path"])), byproducts["skill-package-manifest.json"])
            self.assertEqual(packager.sha256_file(Path(result["sbom_path"])), byproducts[packager.SBOM_FILENAME])

    def test_release_artifact_set_is_complete_and_consistent(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "source"; root.mkdir(); make_source(root)
            result = packager.build_package(root, Path(td) / "skill.zip", SOURCE)
            required = ["archive", "manifest_path", "checksum_path", "sbom_path", "provenance_path"]
            for key in required:
                self.assertTrue(Path(result[key]).is_file(), key)
            self.assertEqual(result["sha256"], packager.sha256_file(Path(result["archive"])))

    def test_zip_metadata_is_normalized(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "source"; root.mkdir(); make_source(root)
            result = packager.build_package(root, Path(td) / "skill.zip", SOURCE)
            with zipfile.ZipFile(result["archive"]) as archive:
                for info in archive.infolist():
                    self.assertEqual(packager.FIXED_ZIP_TIMESTAMP, info.date_time)
                    self.assertEqual(zipfile.ZIP_STORED, info.compress_type)
                    self.assertEqual(0o644, (info.external_attr >> 16) & 0o777)


if __name__ == "__main__":
    unittest.main()
