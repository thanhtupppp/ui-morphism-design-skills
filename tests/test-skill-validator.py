#!/usr/bin/env python3
"""Regression tests for the Skill package validator."""
import importlib.util
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))
import skill_validator as validator_module

Validator = validator_module.Validator
inspect_zip = validator_module.inspect_zip
render_json = validator_module.render_json


def make_valid_skill(root: Path, version: str = "1.9.0") -> None:
    (root / "agents").mkdir(parents=True)
    (root / "references").mkdir(parents=True)
    (root / "SKILL.md").write_text(
        "---\nname: ui-morphism-design\ndescription: Select and implement accessible cross-platform UI morphism systems for production interfaces.\n---\n\n# UI Morphism Design\n\nRead `references/guide.md` before implementation.\n",
        encoding="utf-8",
    )
    (root / "agents" / "openai.yaml").write_text(
        'interface:\n  display_name: "UI Morphism Design"\n  short_description: "Accessible cross-platform UI morphism design."\n', encoding="utf-8")
    (root / "references" / "guide.md").write_text("# Guide\n", encoding="utf-8")
    (root / "skill.json").write_text(json.dumps({
        "name": "ui-morphism-design", "displayName": "UI Morphism Design Intelligence", "version": version,
        "description": "Test manifest", "styles": [], "platforms": [], "workflow": [],
        "source_of_truth": "SKILL.md", "contracts": ["references/guide.md"],
    }), encoding="utf-8")


class ValidatorTests(unittest.TestCase):
    def test_valid_directory_has_no_errors(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); make_valid_skill(root); validator = Validator(root); validator.run_checks()
            self.assertFalse([f for f in validator.findings if f.severity == "ERROR"])

    def test_root_relative_reference_from_nested_markdown(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); make_valid_skill(root)
            (root / "references" / "nested.md").write_text("Read `references/guide.md` and `SKILL.md`.\n", encoding="utf-8")
            validator = Validator(root); validator.run_checks()
            self.assertFalse([f for f in validator.findings if f.code == "LK002"])

    def test_source_checkout_metadata_is_ignored(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); make_valid_skill(root)
            (root / ".git" / "hooks").mkdir(parents=True); (root / ".git" / "hooks" / "sample").write_text("x")
            (root / "tests" / "__pycache__").mkdir(parents=True); (root / "tests" / "__pycache__" / "x.pyc").write_bytes(b"x")
            validator = Validator(root); validator.run_checks()
            self.assertFalse([f for f in validator.findings if f.code in {"PK010", "PK012"}])

    def test_broken_reference_is_error(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); make_valid_skill(root); (root / "references" / "guide.md").unlink()
            validator = Validator(root); validator.run_checks()
            self.assertIn("LK002", {f.code for f in validator.findings})

    def test_manifest_name_drift_is_error(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); make_valid_skill(root); data = json.loads((root / "skill.json").read_text()); data["name"] = "wrong-name"
            (root / "skill.json").write_text(json.dumps(data), encoding="utf-8"); validator = Validator(root); validator.run_checks()
            self.assertIn("CF001", {f.code for f in validator.findings})

    def test_zip_path_traversal_is_error(self):
        with tempfile.TemporaryDirectory() as td:
            archive_path = Path(td) / "skill.zip"
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr("../escape.txt", "bad"); archive.writestr("SKILL.md", "---\nname: x\ndescription: this description is intentionally long enough for testing validation behavior\n---\n# X\n")
            self.assertIn("ZP010", {f.code for f in inspect_zip(archive_path)})

    def test_zip_rejects_development_artifacts(self):
        with tempfile.TemporaryDirectory() as td:
            archive_path = Path(td) / "skill.zip"
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr("SKILL.md", "---\nname: x\ndescription: this description is intentionally long enough for testing validation behavior\n---\n# X\n")
                archive.writestr(".git/config", "bad")
            self.assertIn("ZP016", {f.code for f in inspect_zip(archive_path)})

    def test_json_report_is_machine_readable(self):
        payload = json.loads(render_json([validator_module.Finding("ERROR", "X001", "SKILL.md", "bad")], False))
        self.assertFalse(payload["ok"]); self.assertEqual(payload["errors"], 1)


if __name__ == "__main__": unittest.main()
