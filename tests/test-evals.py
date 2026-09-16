import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("run_evals", ROOT / "scripts" / "run-evals.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


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

    def test_classification_metrics_confusion_matrix_and_macro_average(self):
        styles = ["flat-design", "material-design", "glassmorphism"]
        results = [
            {"expected_primary": "flat-design", "predicted_primary": "flat-design"},
            {"expected_primary": "flat-design", "predicted_primary": "material-design"},
            {"expected_primary": "material-design", "predicted_primary": "material-design"},
            {"expected_primary": "glassmorphism", "predicted_primary": "flat-design"},
        ]
        metrics = MOD.classification_metrics(results, styles)

        self.assertEqual(1, metrics["confusion_matrix"]["flat-design"]["flat-design"])
        self.assertEqual(1, metrics["confusion_matrix"]["flat-design"]["material-design"])
        self.assertEqual(1, metrics["confusion_matrix"]["glassmorphism"]["flat-design"])

        flat = metrics["per_style"]["flat-design"]
        self.assertEqual(1, flat["true_positive"])
        self.assertEqual(1, flat["false_positive"])
        self.assertEqual(1, flat["false_negative"])
        self.assertEqual(2, flat["support"])
        self.assertEqual(0.5, flat["precision"])
        self.assertEqual(0.5, flat["recall"])
        self.assertEqual(0.5, flat["f1"])

        material = metrics["per_style"]["material-design"]
        self.assertEqual(0.5, material["precision"])
        self.assertEqual(1.0, material["recall"])
        self.assertEqual(0.6667, material["f1"])

        glass = metrics["per_style"]["glassmorphism"]
        self.assertEqual(0.0, glass["precision"])
        self.assertEqual(0.0, glass["recall"])
        self.assertEqual(0.0, glass["f1"])

        self.assertEqual(0.3333, metrics["macro_average"]["precision"])
        self.assertEqual(0.5, metrics["macro_average"]["recall"])
        self.assertEqual(0.3889, metrics["macro_average"]["f1"])

    def test_unknown_prediction_gets_confusion_matrix_bucket(self):
        styles = ["flat-design", "material-design"]
        metrics = MOD.classification_metrics([
            {"expected_primary": "flat-design", "predicted_primary": "not-a-style"},
        ], styles)
        self.assertIn(MOD.UNKNOWN_LABEL, metrics["predicted_labels"])
        self.assertEqual(1, metrics["confusion_matrix"]["flat-design"][MOD.UNKNOWN_LABEL])
        self.assertEqual(0.0, metrics["per_style"]["flat-design"]["recall"])

    def test_reference_router_metrics_are_perfect(self):
        styles = list(self.rules["styles"])
        results = []
        for case in self.cases:
            predicted, _, _ = MOD.route(case["intent"], self.rules)
            results.append({
                "expected_primary": case["expected_primary"],
                "predicted_primary": predicted,
            })
        metrics = MOD.classification_metrics(results, styles)
        self.assertEqual(1.0, metrics["macro_average"]["precision"])
        self.assertEqual(1.0, metrics["macro_average"]["recall"])
        self.assertEqual(1.0, metrics["macro_average"]["f1"])


if __name__ == "__main__":
    unittest.main()
