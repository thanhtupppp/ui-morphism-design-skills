#!/usr/bin/env python3
"""Deterministic trigger/routing and semantic-parity eval runner."""
from __future__ import annotations
import argparse, json, re, subprocess
from pathlib import Path

UNKNOWN_LABEL = "__unknown__"


def load(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def route(intent: str, rules: dict) -> tuple[str, dict[str, int], list[dict]]:
    text = norm(intent)
    scores = {style: 0 for style in rules["styles"]}
    evidence = []
    for style, cfg in rules["styles"].items():
        for phrase, weight in cfg.get("positive", {}).items():
            if norm(phrase) in text:
                scores[style] += weight
                evidence.append({"style": style, "phrase": phrase, "weight": weight})
        for phrase, weight in cfg.get("negative", {}).items():
            if norm(phrase) in text:
                scores[style] += weight
                evidence.append({"style": style, "phrase": phrase, "weight": weight})
    for rule in rules.get("global_rules", []):
        if any(norm(p) in text for p in rule.get("when_any", [])):
            for style, weight in rule.get("boost", {}).items():
                scores[style] += weight
            for style, weight in rule.get("penalize", {}).items():
                scores[style] += weight
    ranked = sorted(scores, key=lambda s: (-scores[s], s))
    return ranked[0], scores, evidence


def parity(root: Path) -> dict:
    script = root / "scripts" / "validate-semantic-parity.mjs"
    if not script.exists():
        return {"ok": False, "exit_code": 127, "output": "missing scripts/validate-semantic-parity.mjs"}
    proc = subprocess.run(["node", str(script)], cwd=root, text=True, capture_output=True)
    return {
        "ok": proc.returncode == 0,
        "exit_code": proc.returncode,
        "output": (proc.stdout + proc.stderr).strip(),
    }


def safe_div(numerator: int | float, denominator: int | float) -> float:
    return numerator / denominator if denominator else 0.0


def classification_metrics(results: list[dict], declared_styles: list[str]) -> dict:
    """Return confusion matrix and one-vs-rest metrics for each declared style.

    Matrix convention: rows are expected labels, columns are predicted labels.
    Predictions outside the declared taxonomy are accumulated under __unknown__.
    """
    unknown_present = any(r["predicted_primary"] not in declared_styles for r in results)
    predicted_labels = list(declared_styles) + ([UNKNOWN_LABEL] if unknown_present else [])
    matrix = {
        expected: {predicted: 0 for predicted in predicted_labels}
        for expected in declared_styles
    }

    for result in results:
        expected = result["expected_primary"]
        predicted = result["predicted_primary"]
        if expected not in matrix:
            continue
        column = predicted if predicted in declared_styles else UNKNOWN_LABEL
        if column not in matrix[expected]:
            for row in matrix.values():
                row[column] = 0
            predicted_labels.append(column)
        matrix[expected][column] += 1

    per_style = {}
    for style in declared_styles:
        tp = matrix[style].get(style, 0)
        fn = sum(matrix[style].values()) - tp
        fp = sum(matrix[other].get(style, 0) for other in declared_styles if other != style)
        support = tp + fn
        predicted_count = tp + fp
        precision = safe_div(tp, predicted_count)
        recall = safe_div(tp, support)
        f1 = safe_div(2 * precision * recall, precision + recall)
        per_style[style] = {
            "true_positive": tp,
            "false_positive": fp,
            "false_negative": fn,
            "support": support,
            "predicted": predicted_count,
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1": round(f1, 4),
        }

    style_count = len(declared_styles)
    macro = {
        "precision": round(safe_div(sum(v["precision"] for v in per_style.values()), style_count), 4),
        "recall": round(safe_div(sum(v["recall"] for v in per_style.values()), style_count), 4),
        "f1": round(safe_div(sum(v["f1"] for v in per_style.values()), style_count), 4),
    }

    return {
        "labels": declared_styles,
        "predicted_labels": predicted_labels,
        "confusion_matrix": matrix,
        "per_style": per_style,
        "macro_average": macro,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--intents", default="evals/intents.json")
    ap.add_argument("--rules", default="evals/routing-rules.json")
    ap.add_argument("--predictions", help="optional JSON mapping case id to predicted primary style")
    ap.add_argument("--output", default="eval-report.json")
    ap.add_argument("--skip-parity", action="store_true")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    intents = load(root / args.intents)
    rules = load(root / args.rules)
    predictions = load(Path(args.predictions)) if args.predictions else None
    declared_styles = list(rules.get("styles", {}))
    declared_style_set = set(declared_styles)
    results = []
    fixture_errors = []

    for case in intents.get("cases", []):
        cid = case.get("id")
        expected = case.get("expected_primary")
        if not cid or not case.get("intent") or expected not in declared_style_set:
            fixture_errors.append(f"invalid case: {cid or '<missing id>'}")
            continue

        predicted, scores, evidence = route(case["intent"], rules)
        source = "reference-router"
        if predictions is not None:
            value = predictions.get(cid) if isinstance(predictions, dict) else None
            if isinstance(value, dict):
                value = value.get("primary")
            if value:
                predicted, source = value, "external-predictions"

        forbidden = set(case.get("forbidden", []))
        passed = predicted == expected and predicted not in forbidden
        results.append({
            "id": cid,
            "intent": case["intent"],
            "expected_primary": expected,
            "predicted_primary": predicted,
            "source": source,
            "pass": passed,
            "scores": scores,
            "evidence": evidence,
            "allowed_supporting": case.get("allowed_supporting", []),
            "forbidden": case.get("forbidden", []),
        })

    route_passed = sum(r["pass"] for r in results)
    total = len(results)
    metrics = classification_metrics(results, declared_styles)
    parity_result = {"ok": True, "skipped": True} if args.skip_parity else parity(root)
    ok = not fixture_errors and route_passed == total and parity_result.get("ok", False)

    report = {
        "schema_version": "1.1.0",
        "ok": ok,
        "summary": {
            "routing_passed": route_passed,
            "routing_total": total,
            "routing_accuracy": round(route_passed / total, 4) if total else 0,
            "macro_precision": metrics["macro_average"]["precision"],
            "macro_recall": metrics["macro_average"]["recall"],
            "macro_f1": metrics["macro_average"]["f1"],
            "semantic_parity": bool(parity_result.get("ok")),
            "fixture_errors": len(fixture_errors),
        },
        "classification": metrics,
        "fixture_errors": fixture_errors,
        "routing": results,
        "semantic_parity": parity_result,
    }

    out = root / args.output
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], ensure_ascii=False))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
