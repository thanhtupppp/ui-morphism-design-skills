import importlib.util
import json
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
        cls.thresholds = json.loads((ROOT / "evals" / "thresholds.json").read_text(encoding="utf-8"))

    def test_all_reference_routes_match_expected(self):
        failures = []
        for case in self.cases:
            predicted, _, _ = MOD.route(case["intent"], self.rules)
            if predicted != case["expected_primary"]: failures.append((case["id"], case["expected_primary"], predicted))
        self.assertEqual([], failures)

    def test_every_declared_style_has_a_primary_fixture(self):
        self.assertEqual(set(self.rules["styles"]), {case["expected_primary"] for case in self.cases})

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
        self.assertEqual((1, 1, 1, 2), (flat["true_positive"], flat["false_positive"], flat["false_negative"], flat["support"]))
        self.assertEqual((0.5, 0.5, 0.5), (flat["precision"], flat["recall"], flat["f1"]))
        material = metrics["per_style"]["material-design"]
        self.assertEqual((0.5, 1.0, 0.6667), (material["precision"], material["recall"], material["f1"]))
        self.assertEqual({"precision": 0.3333, "recall": 0.5, "f1": 0.3889}, metrics["macro_average"])

    def test_unknown_prediction_gets_confusion_matrix_bucket(self):
        metrics = MOD.classification_metrics([{"expected_primary": "flat-design", "predicted_primary": "not-a-style"}], ["flat-design", "material-design"])
        self.assertIn(MOD.UNKNOWN_LABEL, metrics["predicted_labels"])
        self.assertEqual(1, metrics["confusion_matrix"]["flat-design"][MOD.UNKNOWN_LABEL])
        self.assertEqual(0.0, metrics["per_style"]["flat-design"]["recall"])

    def reference_metrics(self):
        styles = list(self.rules["styles"]); results = []
        for case in self.cases:
            predicted, _, _ = MOD.route(case["intent"], self.rules)
            results.append({"expected_primary": case["expected_primary"], "predicted_primary": predicted})
        return MOD.classification_metrics(results, styles)

    def test_reference_router_metrics_are_perfect(self):
        macro = self.reference_metrics()["macro_average"]
        self.assertEqual({"precision": 1.0, "recall": 1.0, "f1": 1.0}, macro)

    def test_repository_threshold_config_is_valid_and_passes_reference_router(self):
        styles = list(self.rules["styles"]); metrics = self.reference_metrics()
        summary = {"routing_accuracy": 1.0, "macro_precision": 1.0, "macro_recall": 1.0, "macro_f1": 1.0}
        result = MOD.evaluate_thresholds(summary, metrics, self.thresholds, styles)
        self.assertTrue(result["ok"])
        self.assertEqual([], result["config_errors"])
        self.assertEqual([], result["failures"])

    def test_threshold_failure_is_reported(self):
        styles = ["flat-design", "material-design"]
        metrics = MOD.classification_metrics([
            {"expected_primary": "flat-design", "predicted_primary": "material-design"},
            {"expected_primary": "material-design", "predicted_primary": "material-design"},
        ], styles)
        summary = {"routing_accuracy": 0.5, "macro_precision": metrics["macro_average"]["precision"], "macro_recall": metrics["macro_average"]["recall"], "macro_f1": metrics["macro_average"]["f1"]}
        config = {"global": {"routing_accuracy": 0.9, "macro_f1": 0.8}, "per_style": {"flat-design": {"recall": 0.8}}}
        result = MOD.evaluate_thresholds(summary, metrics, config, styles)
        self.assertFalse(result["ok"])
        self.assertEqual(3, result["failure_count"])
        failed = {(item.get("style"), item["metric"]) for item in result["failures"]}
        self.assertIn((None, "routing_accuracy"), failed)
        self.assertIn((None, "macro_f1"), failed)
        self.assertIn(("flat-design", "recall"), failed)

    def test_invalid_threshold_config_fails_validation(self):
        errors = MOD.validate_threshold_config({"global": {"macro_f1": 1.2}, "per_style": {"unknown-style": {"recall": 0.8}}}, ["flat-design"])
        self.assertTrue(any("between 0 and 1" in error for error in errors))
        self.assertTrue(any("unknown threshold style" in error for error in errors))


if __name__ == "__main__": unittest.main()
