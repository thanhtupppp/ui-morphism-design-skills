#!/usr/bin/env python3
"""Render eval-report.json as a compact GitHub Actions job summary."""
import argparse, json
from pathlib import Path


def fmt(value):
    return "—" if value is None else f"{value:.4f}" if isinstance(value, float) else str(value)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("report", nargs="?", default="eval-report.json"); ap.add_argument("--output")
    args = ap.parse_args(); report = json.loads(Path(args.report).read_text(encoding="utf-8")); s = report.get("summary", {})
    lines = ["## UI Morphism Eval Summary", "", f"**Overall:** {'PASS' if report.get('ok') else 'FAIL'}", "", "| Metric | Value |", "|---|---:|"]
    for key in ("routing_accuracy","macro_precision","macro_recall","macro_f1"):
        lines.append(f"| {key} | {fmt(s.get(key))} |")
    lines += ["", f"Thresholds: **{'PASS' if s.get('thresholds_passed') else 'FAIL'}** · failures: {s.get('threshold_failures', 0)}", f"Baseline: **{'PASS' if s.get('baseline_passed', True) else 'FAIL'}** · regressions: {s.get('baseline_regressions', 0)}", f"Semantic parity: **{'PASS' if s.get('semantic_parity') else 'FAIL'}**"]
    failures = report.get("thresholds", {}).get("failures", [])
    lines += ["", "### Threshold failures"]
    if not failures: lines.append("None.")
    else:
        lines += ["| Scope | Style | Metric | Actual | Minimum |", "|---|---|---|---:|---:|"]
        for f in failures: lines.append(f"| {f.get('scope','')} | {f.get('style','—')} | {f.get('metric','')} | {fmt(f.get('actual'))} | {fmt(f.get('minimum'))} |")
    regressions = report.get("baseline", {}).get("regressions", [])
    lines += ["", "### Baseline regressions"]
    if not regressions: lines.append("None.")
    else:
        lines += ["| Scope | Style | Metric | Current | Baseline | Delta | Max drop |", "|---|---|---|---:|---:|---:|---:|"]
        for r in regressions: lines.append(f"| {r.get('scope','')} | {r.get('style','—')} | {r.get('metric','')} | {fmt(r.get('current'))} | {fmt(r.get('baseline'))} | {fmt(r.get('delta'))} | {fmt(r.get('max_drop'))} |")
    text = "\n".join(lines) + "\n"
    if args.output: Path(args.output).write_text(text, encoding="utf-8")
    else: print(text, end="")

if __name__ == "__main__": main()
