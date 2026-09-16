#!/usr/bin/env python3
"""Enforce style-level stabilization invariants for UI morphism styles."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

STYLES = (
    "aurora-ui",
    "bento-ui",
    "claymorphism",
    "flat-design",
    "glassmorphism",
    "liquid-glass",
    "material-design",
    "neobrutalism",
    "neumorphism",
    "skeuomorphism",
    "swiss-editorial",
)
REQUIRED_FILES = (
    "SKILL.md",
    "components.md",
    "platforms.md",
    "example.css",
    "example.tsx",
    "example.flutter.dart",
    "example.native.tsx",
)
LEGACY_PREFIXES = (
    "--aurora-", "--bento-", "--clay-", "--flat-", "--glass-",
    "--liquid-", "--md-", "--neo-", "--neu-", "--sk-",
)
PROPERTY_DECL_RE = re.compile(r"(?m)^\s*(--[a-z][a-z0-9-]*)\s*:")
PROPERTY_VAR_RE = re.compile(r"var\(\s*(--[a-z][a-z0-9-]*)\b")
SESSION_CITATION_RE = re.compile(r"\ue200cite\ue202|cite|turn\d+(?:search|file|fetch|view)\d+")
PINNED_FRAMEWORK_RE = re.compile(
    r"\b(?:Flutter|React|React Native|Node(?:\.js)?|Material)\s+v?\d+\.\d+(?:\.\d+)?\b",
    re.IGNORECASE,
)


def css_custom_properties(text: str) -> set[str]:
    return set(PROPERTY_DECL_RE.findall(text)) | set(PROPERTY_VAR_RE.findall(text))


def audit_style(root: Path, style: str) -> dict:
    root = root.resolve()
    findings: list[dict] = []
    checked_files = 0

    def fail(code: str, path: Path, message: str) -> None:
        findings.append({
            "severity": "ERROR",
            "code": code,
            "path": path.relative_to(root).as_posix(),
            "message": message,
        })

    style_dir = root / "skills" / style
    if not style_dir.is_dir():
        fail("STYLE001", style_dir, f"missing style directory: {style}")
        return {"style": style, "ok": False, "checked_files": 0, "errors": len(findings), "findings": findings}

    for filename in REQUIRED_FILES:
        path = style_dir / filename
        checked_files += 1
        if not path.is_file():
            fail("STYLE002", path, f"missing required style file: {filename}")
            continue

        text = path.read_text(encoding="utf-8")
        if SESSION_CITATION_RE.search(text):
            fail("STYLE003", path, "non-portable session citation/reference detected")
        if PINNED_FRAMEWORK_RE.search(text):
            fail("STYLE004", path, "framework-version-pinned guidance detected; keep reusable guidance version-neutral")

        if filename == "components.md":
            expected = f"--um-{style}-"
            for token in sorted(css_custom_properties(text)):
                if any(token.startswith(prefix) for prefix in LEGACY_PREFIXES):
                    fail("STYLE010", path, f"legacy token namespace detected: {token}")
                if not token.startswith(expected):
                    fail("STYLE011", path, f"custom property '{token}' must use namespace '{expected}*'")

    return {
        "style": style,
        "ok": not findings,
        "checked_files": checked_files,
        "errors": len(findings),
        "findings": findings,
    }


def audit(root: Path, styles: list[str] | tuple[str, ...]) -> dict:
    reports = [audit_style(root, style) for style in styles]
    findings = [finding for report in reports for finding in report["findings"]]
    return {
        "ok": not findings,
        "styles_checked": len(reports),
        "required_files": sum(report["checked_files"] for report in reports),
        "errors": len(findings),
        "style_results": [
            {"style": report["style"], "ok": report["ok"], "checked_files": report["checked_files"], "errors": report["errors"]}
            for report in reports
        ],
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate style stabilization invariants")
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--style", action="append", choices=STYLES, help="Audit only this style; may be repeated")
    parser.add_argument("--output")
    args = parser.parse_args()
    styles = args.style or list(STYLES)
    report = audit(Path(args.root), styles)
    payload = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        Path(args.output).write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
