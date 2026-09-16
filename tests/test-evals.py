import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("run_evals", ROOT / "scripts" / "run-evals.py")
MOD = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)

class EvalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = json.loads((ROOT / "evals" / "routing-rules.json").read_text(encoding="utf-8"))
        cls.cases = json.loads((ROOT / "evals" / "intents.json").read_text(encoding="utf-8"))["cases"]

    def test_all_reference_routes_match_expected(self):
        failures = []
        for case in self.cases:
            predicted, _, _ = MOD.route(case["intent"], self.rules)
            if predicted != case["expected_primary"]:
                failures.append((case["id"], case["expected_primary"], predicted))
        self.assertEqual([], failures)

    def test_every_declared_style_has_a_primary_fixture(self):
        covered = {case["expected_primary"] for case in self.cases}
        self.assertEqual(set(self.rules["styles"]), covered)

    def test_forbidden_styles_never_win_reference_router(self):
        for case in self.cases:
            predicted, _, _ = MOD.route(case["intent"], self.rules)
            self.assertNotIn(predicted, case.get("forbidden", []), case["id"])

if __name__ == "__main__": unittest.main()
