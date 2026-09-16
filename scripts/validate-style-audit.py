#!/usr/bin/env python3
"""Enforce style-level stabilization invariants for all ten UI styles."""
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
    """Return actual CSS custom properties from declarations and var() references.

    This intentionally ignores BEM modifiers such as `.card--featured` and
    Markdown separators such as `---`, which are not custom properties.
    """
    return set(PROPERTY_DECL_RE.findall(text)) | set(PROPERTY_VAR_RE.findall(text))


def audit(root: Path) -> dict:
    root = root.resolve()
    findings: list[dict] = []
    rows = 0

    def fail(code: str, path: Path, message: str) -> None:
        findings.append({
            "severity": "ERROR",
            "code": code,
            "path": path.relative_to(root).as_posix(),
            "message": message,
        })

    for style in STYLES:
        style_dir = root / "skills" / style
        if not style_dir.is_dir():
            fail("STYLE001", style_dir, f"missing style directory: {style}")
            continue

        for filename in REQUIRED_FILES:
            path = style_dir / filename
            rows += 1
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
                tokens = sorted(css_custom_properties(text))
                for token in tokens:
                    if any(token.startswith(prefix) for prefix in LEGACY_PREFIXES):
                        fail("STYLE010", path, f"legacy token namespace detected: {token}")
                    if not token.startswith(expected):
                        fail("STYLE011", path, f"custom property '{token}' must use namespace '{expected}*'")

    return {
        "ok": not findings,
        "styles": len(STYLES),
        "required_files": rows,
        "findings": findings,
        "errors": len(findings),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate style stabilization invariants")
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    report = audit(Path(args.root))
    payload = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        Path(args.output).write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
