#!/usr/bin/env python3
"""Deterministic trigger/routing and semantic-parity eval runner."""
from __future__ import annotations
import argparse, json, re, subprocess
from pathlib import Path

UNKNOWN_LABEL = "__unknown__"
GLOBAL_THRESHOLD_KEYS = {"routing_accuracy", "macro_precision", "macro_recall", "macro_f1"}
STYLE_THRESHOLD_KEYS = {"precision", "recall", "f1"}


def load(path: Path):
    with path.open(encoding="utf-8") as f: return json.load(f)

def norm(text: str) -> str: return re.sub(r"\s+", " ", text.lower()).strip()

def route(intent: str, rules: dict) -> tuple[str, dict[str, int], list[dict]]:
    text = norm(intent); scores = {style: 0 for style in rules["styles"]}; evidence = []
    for style, cfg in rules["styles"].items():
        for phrase, weight in cfg.get("positive", {}).items():
            if norm(phrase) in text: scores[style] += weight; evidence.append({"style": style, "phrase": phrase, "weight": weight})
        for phrase, weight in cfg.get("negative", {}).items():
            if norm(phrase) in text: scores[style] += weight; evidence.append({"style": style, "phrase": phrase, "weight": weight})
    for rule in rules.get("global_rules", []):
        if any(norm(p) in text for p in rule.get("when_any", [])):
            for style, weight in rule.get("boost", {}).items(): scores[style] += weight
            for style, weight in rule.get("penalize", {}).items(): scores[style] += weight
    ranked = sorted(scores, key=lambda s: (-scores[s], s)); return ranked[0], scores, evidence

def parity(root: Path) -> dict:
    script = root / "scripts" / "validate-semantic-parity.mjs"
    if not script.exists(): return {"ok": False, "exit_code": 127, "output": "missing scripts/validate-semantic-parity.mjs"}
    proc = subprocess.run(["node", str(script)], cwd=root, text=True, capture_output=True)
    return {"ok": proc.returncode == 0, "exit_code": proc.returncode, "output": (proc.stdout + proc.stderr).strip()}

def safe_div(numerator, denominator) -> float: return numerator / denominator if denominator else 0.0

def classification_metrics(results: list[dict], declared_styles: list[str]) -> dict:
    unknown_present = any(r["predicted_primary"] not in declared_styles for r in results)
    predicted_labels = list(declared_styles) + ([UNKNOWN_LABEL] if unknown_present else [])
    matrix = {expected: {predicted: 0 for predicted in predicted_labels} for expected in declared_styles}
    for result in results:
        expected, predicted = result["expected_primary"], result["predicted_primary"]
        if expected not in matrix: continue
        matrix[expected][predicted if predicted in declared_styles else UNKNOWN_LABEL] += 1
    per_style = {}
    for style in declared_styles:
        tp = matrix[style].get(style, 0); fn = sum(matrix[style].values()) - tp
        fp = sum(matrix[other].get(style, 0) for other in declared_styles if other != style)
        support = tp + fn; predicted_count = tp + fp
        precision = safe_div(tp, predicted_count); recall = safe_div(tp, support); f1 = safe_div(2 * precision * recall, precision + recall)
        per_style[style] = {"true_positive": tp, "false_positive": fp, "false_negative": fn, "support": support, "predicted": predicted_count, "precision": round(precision, 4), "recall": round(recall, 4), "f1": round(f1, 4)}
    count = len(declared_styles)
    macro = {key: round(safe_div(sum(v[key] for v in per_style.values()), count), 4) for key in ("precision", "recall", "f1")}
    return {"labels": declared_styles, "predicted_labels": predicted_labels, "confusion_matrix": matrix, "per_style": per_style, "macro_average": macro}

def validate_threshold_config(config: dict, declared_styles: list[str]) -> list[str]:
    errors = []
    if not isinstance(config, dict): return ["threshold config must be a JSON object"]
    for key, value in config.get("global", {}).items():
        if key not in GLOBAL_THRESHOLD_KEYS: errors.append(f"unknown global threshold: {key}")
        if not isinstance(value, (int, float)) or isinstance(value, bool) or not 0 <= value <= 1: errors.append(f"global.{key} must be between 0 and 1")
    for style, cfg in config.get("per_style", {}).items():
        if style not in declared_styles: errors.append(f"unknown threshold style: {style}")
        if not isinstance(cfg, dict): errors.append(f"per_style.{style} must be an object"); continue
        for key, value in cfg.items():
            if key not in STYLE_THRESHOLD_KEYS: errors.append(f"unknown per-style threshold: {style}.{key}")
            if not isinstance(value, (int, float)) or isinstance(value, bool) or not 0 <= value <= 1: errors.append(f"per_style.{style}.{key} must be between 0 and 1")
    return errors

def evaluate_thresholds(summary: dict, metrics: dict, config: dict, declared_styles: list[str]) -> dict:
    config_errors = validate_threshold_config(config, declared_styles); checks, failures = [], []
    for key, minimum in config.get("global", {}).items():
        actual = summary.get(key); passed = isinstance(actual, (int, float)) and actual >= minimum
        check = {"scope": "global", "metric": key, "minimum": minimum, "actual": actual, "pass": passed}; checks.append(check)
        if not passed: failures.append(check)
    for style, cfg in config.get("per_style", {}).items():
        actual_metrics = metrics.get("per_style", {}).get(style, {})
        for key, minimum in cfg.items():
            actual = actual_metrics.get(key); passed = isinstance(actual, (int, float)) and actual >= minimum
            check = {"scope": "style", "style": style, "metric": key, "minimum": minimum, "actual": actual, "pass": passed}; checks.append(check)
            if not passed: failures.append(check)
    return {"ok": not config_errors and not failures, "config_errors": config_errors, "checks": checks, "failures": failures, "failure_count": len(failures)}

def evaluate_baseline(summary: dict, metrics: dict, baseline: dict, declared_styles: list[str]) -> dict:
    errors, checks, regressions = [], [], []
    if not isinstance(baseline, dict): return {"ok": False, "config_errors": ["baseline must be a JSON object"], "checks": [], "regressions": [], "regression_count": 0}
    global_drop = baseline.get("max_drop", {}).get("global", {})
    for metric, previous in baseline.get("metrics", {}).items():
        if metric not in GLOBAL_THRESHOLD_KEYS: errors.append(f"unknown baseline metric: {metric}"); continue
        allowed = global_drop.get(metric, 0); current = summary.get(metric)
        if not all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in (previous, allowed, current)): errors.append(f"invalid baseline metric: {metric}"); continue
        drop = round(previous - current, 4); passed = drop <= allowed
        check = {"scope": "global", "metric": metric, "baseline": previous, "current": current, "delta": round(current - previous, 4), "max_drop": allowed, "pass": passed}; checks.append(check)
        if not passed: regressions.append(check)
    wildcard = baseline.get("max_drop", {}).get("per_style", {}).get("*", {})
    overrides = baseline.get("max_drop", {}).get("per_style", {})
    for style, previous_metrics in baseline.get("per_style", {}).items():
        if style not in declared_styles: errors.append(f"unknown baseline style: {style}"); continue
        current_metrics = metrics.get("per_style", {}).get(style, {}); limits = dict(wildcard); limits.update(overrides.get(style, {}))
        for metric, previous in previous_metrics.items():
            if metric not in STYLE_THRESHOLD_KEYS: errors.append(f"unknown baseline style metric: {style}.{metric}"); continue
            current = current_metrics.get(metric); allowed = limits.get(metric, 0)
            if not all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in (previous, allowed, current)): errors.append(f"invalid baseline style metric: {style}.{metric}"); continue
            drop = round(previous - current, 4); passed = drop <= allowed
            check = {"scope": "style", "style": style, "metric": metric, "baseline": previous, "current": current, "delta": round(current - previous, 4), "max_drop": allowed, "pass": passed}; checks.append(check)
            if not passed: regressions.append(check)
    return {"ok": not errors and not regressions, "config_errors": errors, "checks": checks, "regressions": regressions, "regression_count": len(regressions)}

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--root", default="."); ap.add_argument("--intents", default="evals/intents.json"); ap.add_argument("--rules", default="evals/routing-rules.json")
    ap.add_argument("--thresholds", default="evals/thresholds.json"); ap.add_argument("--baseline", default="evals/baseline.json"); ap.add_argument("--predictions"); ap.add_argument("--output", default="eval-report.json")
    ap.add_argument("--skip-parity", action="store_true"); ap.add_argument("--skip-thresholds", action="store_true"); ap.add_argument("--skip-baseline", action="store_true")
    args = ap.parse_args(); root = Path(args.root).resolve(); intents = load(root / args.intents); rules = load(root / args.rules); predictions = load(Path(args.predictions)) if args.predictions else None
    declared_styles = list(rules.get("styles", {})); declared_set = set(declared_styles); results, fixture_errors = [], []
    for case in intents.get("cases", []):
        cid, expected = case.get("id"), case.get("expected_primary")
        if not cid or not case.get("intent") or expected not in declared_set: fixture_errors.append(f"invalid case: {cid or '<missing id>'}"); continue
        predicted, scores, evidence = route(case["intent"], rules); source = "reference-router"
        if predictions is not None:
            value = predictions.get(cid) if isinstance(predictions, dict) else None
            if isinstance(value, dict): value = value.get("primary")
            if value: predicted, source = value, "external-predictions"
        forbidden = set(case.get("forbidden", [])); passed = predicted == expected and predicted not in forbidden
        results.append({"id": cid, "intent": case["intent"], "expected_primary": expected, "predicted_primary": predicted, "source": source, "pass": passed, "scores": scores, "evidence": evidence, "allowed_supporting": case.get("allowed_supporting", []), "forbidden": case.get("forbidden", [])})
    route_passed = sum(r["pass"] for r in results); total = len(results); metrics = classification_metrics(results, declared_styles)
    summary = {"routing_passed": route_passed, "routing_total": total, "routing_accuracy": round(route_passed / total, 4) if total else 0, "macro_precision": metrics["macro_average"]["precision"], "macro_recall": metrics["macro_average"]["recall"], "macro_f1": metrics["macro_average"]["f1"], "fixture_errors": len(fixture_errors)}
    threshold_result = {"ok": True, "skipped": True, "config_errors": [], "checks": [], "failures": [], "failure_count": 0} if args.skip_thresholds else evaluate_thresholds(summary, metrics, load(root / args.thresholds), declared_styles)
    baseline_result = {"ok": True, "skipped": True, "config_errors": [], "checks": [], "regressions": [], "regression_count": 0} if args.skip_baseline else evaluate_baseline(summary, metrics, load(root / args.baseline), declared_styles)
    parity_result = {"ok": True, "skipped": True} if args.skip_parity else parity(root)
    summary.update({"semantic_parity": bool(parity_result.get("ok")), "thresholds_passed": bool(threshold_result.get("ok")), "threshold_failures": threshold_result.get("failure_count", 0), "baseline_passed": bool(baseline_result.get("ok")), "baseline_regressions": baseline_result.get("regression_count", 0)})
    ok = not fixture_errors and route_passed == total and parity_result.get("ok", False) and threshold_result.get("ok", False) and baseline_result.get("ok", False)
    report = {"schema_version": "1.2.0", "ok": ok, "summary": summary, "classification": metrics, "thresholds": threshold_result, "fixture_errors": fixture_errors, "routing": results, "semantic_parity": parity_result, "baseline": baseline_result}
    out = root / args.output; out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"); print(json.dumps(report["summary"], ensure_ascii=False)); return 0 if ok else 1

if __name__ == "__main__": raise SystemExit(main())
