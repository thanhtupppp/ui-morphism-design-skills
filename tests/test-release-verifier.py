#!/usr/bin/env python3
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import skill_packager

SPEC = importlib.util.spec_from_file_location("verify_release", ROOT / "scripts" / "verify-release.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def make_source(root: Path) -> None:
    (root / "SKILL.md").write_text("---\nname: test-skill\ndescription: A deterministic release verifier fixture for regression testing.\n---\n# Test Skill\n", encoding="utf-8")
    (root / "skill.json").write_text(json.dumps({"name": "test-skill", "version": "1.0.0"}), encoding="utf-8")
    (root / "references").mkdir()
    (root / "references" / "guide.md").write_text("# Guide\n", encoding="utf-8")


class ReleaseVerifierTests(unittest.TestCase):
    def build(self, td: str):
        source = Path(td) / "source"; source.mkdir(); make_source(source)
        release = Path(td) / "release"; release.mkdir()
        skill_packager.build_package(source, release / "skill.zip", source={
            "repository": "https://github.com/example/test",
            "ref": "refs/tags/v1.0.0",
            "revision": "abc123",
            "invocation_id": "42",
            "builder_id": "github-actions",
        })
        return release

    def test_valid_release_graph_passes(self):
        with tempfile.TemporaryDirectory() as td:
            release = self.build(td)
            report = VERIFY.verify_release(release, "abc123")
            self.assertTrue(report["ok"], report["errors"])

    def test_tampered_archive_fails_checksum_and_provenance(self):
        with tempfile.TemporaryDirectory() as td:
            release = self.build(td)
            with (release / "skill.zip").open("ab") as handle:
                handle.write(b"tamper")
            report = VERIFY.verify_release(release, "abc123")
            self.assertFalse(report["ok"])
            self.assertTrue(any("sha256" in error.lower() or "subject digest" in error for error in report["errors"]))

    def test_tampered_sbom_fails_provenance_link(self):
        with tempfile.TemporaryDirectory() as td:
            release = self.build(td)
            sbom_path = release / "skill.sbom.cdx.json"
            sbom = json.loads(sbom_path.read_text(encoding="utf-8"))
            sbom["components"][0]["hashes"][0]["content"] = "0" * 64
            sbom_path.write_text(json.dumps(sbom, sort_keys=True) + "\n", encoding="utf-8")
            report = VERIFY.verify_release(release, "abc123")
            self.assertFalse(report["ok"])
            self.assertTrue(any("SBOM" in error for error in report["errors"]))

    def test_wrong_expected_revision_fails(self):
        with tempfile.TemporaryDirectory() as td:
            release = self.build(td)
            report = VERIFY.verify_release(release, "different")
            self.assertFalse(report["ok"])
            self.assertTrue(any("revision mismatch" in error for error in report["errors"]))

    def test_missing_artifact_fails(self):
        with tempfile.TemporaryDirectory() as td:
            release = self.build(td)
            (release / "skill.provenance.json").unlink()
            report = VERIFY.verify_release(release)
            self.assertFalse(report["ok"])
            self.assertIn("missing release artifact: skill.provenance.json", report["errors"])


if __name__ == "__main__":
    unittest.main()
