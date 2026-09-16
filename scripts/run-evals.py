#!/usr/bin/env python3
"""Deterministic trigger/routing and semantic-parity eval runner."""
from __future__ import annotations
import argparse, json, re, subprocess, sys
from pathlib import Path


def load(path: Path):
    with path.open(encoding="utf-8") as f: return json.load(f)

def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()

def route(intent: str, rules: dict) -> tuple[str, dict[str,int], list[dict]]:
    text = norm(intent); scores = {style: 0 for style in rules["styles"]}; evidence = []
    for style, cfg in rules["styles"].items():
        for phrase, weight in cfg.get("positive", {}).items():
            if norm(phrase) in text: scores[style] += weight; evidence.append({"style":style,"phrase":phrase,"weight":weight})
        for phrase, weight in cfg.get("negative", {}).items():
            if norm(phrase) in text: scores[style] += weight; evidence.append({"style":style,"phrase":phrase,"weight":weight})
    for rule in rules.get("global_rules", []):
        if any(norm(p) in text for p in rule.get("when_any", [])):
            for style, weight in rule.get("boost", {}).items(): scores[style] += weight
            for style, weight in rule.get("penalize", {}).items(): scores[style] += weight
    ranked = sorted(scores, key=lambda s: (-scores[s], s))
    return ranked[0], scores, evidence

def parity(root: Path) -> dict:
    script = root / "scripts" / "validate-semantic-parity.mjs"
    if not script.exists(): return {"ok":False,"exit_code":127,"output":"missing scripts/validate-semantic-parity.mjs"}
    proc = subprocess.run(["node", str(script)], cwd=root, text=True, capture_output=True)
    return {"ok":proc.returncode == 0,"exit_code":proc.returncode,"output":(proc.stdout + proc.stderr).strip()}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--intents", default="evals/intents.json")
    ap.add_argument("--rules", default="evals/routing-rules.json")
    ap.add_argument("--predictions", help="optional JSON mapping case id to predicted primary style")
    ap.add_argument("--output", default="eval-report.json")
    ap.add_argument("--skip-parity", action="store_true")
    args = ap.parse_args(); root = Path(args.root).resolve()
    intents = load(root / args.intents); rules = load(root / args.rules)
    predictions = load(Path(args.predictions)) if args.predictions else None
    declared_styles = set(rules.get("styles", {})); results = []; fixture_errors = []
    for case in intents.get("cases", []):
        cid = case.get("id"); expected = case.get("expected_primary")
        if not cid or not case.get("intent") or expected not in declared_styles:
            fixture_errors.append(f"invalid case: {cid or '<missing id>'}"); continue
        predicted, scores, evidence = route(case["intent"], rules)
        source = "reference-router"
        if predictions is not None:
            value = predictions.get(cid) if isinstance(predictions, dict) else None
            if isinstance(value, dict): value = value.get("primary")
            if value: predicted, source = value, "external-predictions"
        forbidden = set(case.get("forbidden", [])); passed = predicted == expected and predicted not in forbidden
        results.append({"id":cid,"intent":case["intent"],"expected_primary":expected,"predicted_primary":predicted,"source":source,"pass":passed,"scores":scores,"evidence":evidence,"allowed_supporting":case.get("allowed_supporting", []),"forbidden":case.get("forbidden", [])})
    route_passed = sum(r["pass"] for r in results); total = len(results)
    parity_result = {"ok":True,"skipped":True} if args.skip_parity else parity(root)
    ok = not fixture_errors and route_passed == total and parity_result.get("ok", False)
    report = {"schema_version":"1.0.0","ok":ok,"summary":{"routing_passed":route_passed,"routing_total":total,"routing_accuracy":round(route_passed/total,4) if total else 0,"semantic_parity":bool(parity_result.get("ok")),"fixture_errors":len(fixture_errors)},"fixture_errors":fixture_errors,"routing":results,"semantic_parity":parity_result}
    out = root / args.output; out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], ensure_ascii=False))
    return 0 if ok else 1

if __name__ == "__main__": raise SystemExit(main())
