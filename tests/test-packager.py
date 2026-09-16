#!/usr/bin/env python3
"""Regression tests for deterministic skill.zip packaging."""
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


def make_source(root: Path) -> None:
    (root / "references").mkdir(parents=True)
    (root / "agents").mkdir(parents=True)
    (root / "SKILL.md").write_text("---\nname: test-skill\ndescription: A deterministic package fixture used for regression testing.\n---\n# Test Skill\n", encoding="utf-8")
    (root / "references" / "guide.md").write_text("# Guide\nStable content.\n", encoding="utf-8")
    (root / "agents" / "openai.yaml").write_text('interface:\n  display_name: "Test Skill"\n  short_description: "Test deterministic packaging."\n', encoding="utf-8")


class PackagerTests(unittest.TestCase):
    def test_same_source_produces_same_archive_checksum_and_manifest(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "source"; root.mkdir(); make_source(root)
            out1 = Path(td) / "one" / "skill.zip"
            out2 = Path(td) / "two" / "skill.zip"
            first = packager.build_package(root, out1)
            second = packager.build_package(root, out2)
            self.assertEqual(first["sha256"], second["sha256"])
            self.assertEqual(out1.read_bytes(), out2.read_bytes())
            self.assertEqual(first["manifest"], second["manifest"])

    def test_manifest_matches_packaged_file_bytes(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "source"; root.mkdir(); make_source(root)
            output = Path(td) / "skill.zip"
            result = packager.build_package(root, output)
            with zipfile.ZipFile(output) as archive:
                embedded = json.loads(archive.read(packager.MANIFEST_NAME))
                self.assertEqual(result["manifest"], embedded)
                self.assertEqual(embedded["file_count"], len(embedded["files"]))
                for entry in embedded["files"]:
                    data = archive.read(entry["path"])
                    self.assertEqual(entry["size"], len(data))
                    self.assertEqual(entry["sha256"], hashlib.sha256(data).hexdigest())

    def test_git_cache_and_temporary_files_are_excluded(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "source"; root.mkdir(); make_source(root)
            (root / ".git" / "objects").mkdir(parents=True); (root / ".git" / "objects" / "x").write_text("secret")
            (root / "scripts" / "__pycache__").mkdir(parents=True); (root / "scripts" / "__pycache__" / "x.pyc").write_bytes(b"cache")
            (root / "notes.tmp").write_text("temporary")
            (root / "draft.md~").write_text("temporary")
            output = Path(td) / "skill.zip"
            packager.build_package(root, output)
            with zipfile.ZipFile(output) as archive:
                names = archive.namelist()
            self.assertFalse(any(name.startswith(".git/") for name in names))
            self.assertFalse(any("__pycache__" in name for name in names))
            self.assertNotIn("notes.tmp", names)
            self.assertNotIn("draft.md~", names)

    def test_checksum_sidecar_matches_archive(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "source"; root.mkdir(); make_source(root)
            output = Path(td) / "skill.zip"
            result = packager.build_package(root, output)
            actual = hashlib.sha256(output.read_bytes()).hexdigest()
            self.assertEqual(actual, result["sha256"])
            self.assertEqual(f"{actual}  skill.zip\n", Path(result["checksum_path"]).read_text(encoding="utf-8"))

    def test_zip_metadata_is_normalized(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "source"; root.mkdir(); make_source(root)
            output = Path(td) / "skill.zip"; packager.build_package(root, output)
            with zipfile.ZipFile(output) as archive:
                for info in archive.infolist():
                    self.assertEqual(packager.FIXED_ZIP_TIMESTAMP, info.date_time)
                    self.assertEqual(zipfile.ZIP_STORED, info.compress_type)
                    self.assertEqual(0o644, (info.external_attr >> 16) & 0o777)


if __name__ == "__main__":
    unittest.main()
