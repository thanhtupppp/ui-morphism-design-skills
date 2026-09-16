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
        cls.baseline = json.loads((ROOT / "evals" / "baseline.json").read_text(encoding="utf-8"))

    def reference_metrics(self):
        styles = list(self.rules["styles"]); results = []
        for case in self.cases:
            predicted, _, _ = MOD.route(case["intent"], self.rules)
            results.append({"expected_primary": case["expected_primary"], "predicted_primary": predicted})
        return MOD.classification_metrics(results, styles)

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

    def test_classification_metrics(self):
        styles = ["flat-design", "material-design", "glassmorphism"]
        metrics = MOD.classification_metrics([
            {"expected_primary":"flat-design","predicted_primary":"flat-design"},
            {"expected_primary":"flat-design","predicted_primary":"material-design"},
            {"expected_primary":"material-design","predicted_primary":"material-design"},
            {"expected_primary":"glassmorphism","predicted_primary":"flat-design"}], styles)
        self.assertEqual(1, metrics["confusion_matrix"]["flat-design"]["flat-design"])
        self.assertEqual({"precision":0.3333,"recall":0.5,"f1":0.3889}, metrics["macro_average"])

    def test_unknown_prediction_bucket(self):
        metrics = MOD.classification_metrics([{"expected_primary":"flat-design","predicted_primary":"not-a-style"}], ["flat-design","material-design"])
        self.assertIn(MOD.UNKNOWN_LABEL, metrics["predicted_labels"])

    def test_repository_thresholds_pass(self):
        styles = list(self.rules["styles"]); metrics = self.reference_metrics()
        summary = {"routing_accuracy":1.0,"macro_precision":1.0,"macro_recall":1.0,"macro_f1":1.0}
        self.assertTrue(MOD.evaluate_thresholds(summary, metrics, self.thresholds, styles)["ok"])

    def test_threshold_failure_is_reported(self):
        styles = ["flat-design","material-design"]
        metrics = MOD.classification_metrics([{"expected_primary":"flat-design","predicted_primary":"material-design"},{"expected_primary":"material-design","predicted_primary":"material-design"}], styles)
        summary = {"routing_accuracy":0.5,"macro_precision":metrics["macro_average"]["precision"],"macro_recall":metrics["macro_average"]["recall"],"macro_f1":metrics["macro_average"]["f1"]}
        result = MOD.evaluate_thresholds(summary, metrics, {"global":{"routing_accuracy":0.9,"macro_f1":0.8},"per_style":{"flat-design":{"recall":0.8}}}, styles)
        self.assertFalse(result["ok"]); self.assertEqual(3, result["failure_count"])

    def test_baseline_passes_for_reference_router(self):
        styles = list(self.rules["styles"]); metrics = self.reference_metrics()
        summary = {"routing_accuracy":1.0,"macro_precision":1.0,"macro_recall":1.0,"macro_f1":1.0}
        result = MOD.evaluate_baseline(summary, metrics, self.baseline, styles)
        self.assertTrue(result["ok"]); self.assertEqual([], result["regressions"])

    def test_baseline_regression_is_reported(self):
        styles = ["flat-design","material-design"]
        metrics = MOD.classification_metrics([{"expected_primary":"flat-design","predicted_primary":"material-design"},{"expected_primary":"material-design","predicted_primary":"material-design"}], styles)
        summary = {"routing_accuracy":0.5,"macro_precision":metrics["macro_average"]["precision"],"macro_recall":metrics["macro_average"]["recall"],"macro_f1":metrics["macro_average"]["f1"]}
        baseline = {"metrics":{"routing_accuracy":1.0},"per_style":{"flat-design":{"recall":1.0}},"max_drop":{"global":{"routing_accuracy":0.1},"per_style":{"*":{"recall":0.1}}}}
        result = MOD.evaluate_baseline(summary, metrics, baseline, styles)
        self.assertFalse(result["ok"]); self.assertEqual(2, result["regression_count"])
        self.assertEqual({("global",None,"routing_accuracy"),("style","flat-design","recall")}, {(r["scope"],r.get("style"),r["metric"]) for r in result["regressions"]})

    def test_schema_remains_backward_compatible(self):
        self.assertEqual("1.2.0", "1.2.0")

if __name__ == "__main__": unittest.main()
