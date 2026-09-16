#!/usr/bin/env python3
"""Validate a ChatGPT Skill-style repository/package.

Dependency-free and intentionally conservative. The repository root is treated as
one distributable skill. Nested skills/<style>/SKILL.md files are treated as
internal modules, not separate packages.
"""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

MAX_PACKAGE_BYTES = 25 * 1024 * 1024
MAX_SKILL_LINES = 500
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LOWER_KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*(?:\.[a-z0-9]+)*$")
MARKDOWN_LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
BACKTICK_PATH_RE = re.compile(
    r"`((?:references|scripts|assets|agents|skills|domains|templates)/[^`\s]+|(?:SKILL|README)\.md|skill\.json)`"
)
ALLOWED_ROOT_NAMES = {"SKILL.md", "README.md", "skill.json", "LICENSE", "LICENSE.md", ".gitignore"}
DISALLOWED_DIRS = {".git", "node_modules", "__pycache__", ".pytest_cache", ".mypy_cache", ".idea", ".vscode"}
DISALLOWED_FILES = {".DS_Store", "Thumbs.db"}


@dataclass
class Finding:
    severity: str
    code: str
    path: str
    message: str


class Validator:
    def __init__(self, root: Path, strict: bool = False) -> None:
        self.root = root.resolve()
        self.strict = strict
        self.findings: list[Finding] = []

    def error(self, code: str, path: Path | str, message: str) -> None:
        self.findings.append(Finding("ERROR", code, self._rel(path), message))

    def warn(self, code: str, path: Path | str, message: str) -> None:
        self.findings.append(Finding("WARN", code, self._rel(path), message))

    def _rel(self, path: Path | str) -> str:
        p = Path(path)
        try:
            return str(p.resolve().relative_to(self.root)) if p.is_absolute() else str(p)
        except Exception:
            return str(p)

    def read_text(self, path: Path) -> str | None:
        try:
            data = path.read_bytes()
        except OSError as exc:
            self.error("IO001", path, f"cannot read file: {exc}")
            return None
        if data.startswith(b"\xef\xbb\xbf"):
            self.warn("TXT001", path, "UTF-8 BOM is discouraged")
        try:
            return data.decode("utf-8-sig")
        except UnicodeDecodeError:
            self.error("TXT002", path, "file must be valid UTF-8")
            return None

    def parse_frontmatter(self, text: str, path: Path) -> tuple[dict[str, str], str] | None:
        lines = text.splitlines()
        if not lines or lines[0].strip() != "---":
            self.error("FM001", path, "SKILL.md must start with YAML frontmatter delimiter '---'")
            return None
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if end is None:
            self.error("FM002", path, "frontmatter is missing closing '---'")
            return None
        fields: dict[str, str] = {}
        for line_no, raw in enumerate(lines[1:end], start=2):
            if not raw.strip() or raw.lstrip().startswith("#"):
                continue
            if raw[:1].isspace() or ":" not in raw:
                self.error("FM003", path, f"unsupported frontmatter syntax at line {line_no}; only scalar key: value pairs are allowed")
                continue
            key, value = raw.split(":", 1)
            key, value = key.strip(), value.strip().strip('"\'')
            if key in fields:
                self.error("FM004", path, f"duplicate frontmatter field '{key}'")
            fields[key] = value
        body = "\n".join(lines[end + 1 :]).lstrip("\n")
        return fields, body

    def validate_skill_md(self) -> None:
        path = self.root / "SKILL.md"
        if not path.is_file():
            self.error("SK001", path, "root SKILL.md is required")
            return
        text = self.read_text(path)
        if text is None:
            return
        parsed = self.parse_frontmatter(text, path)
        if parsed is None:
            return
        fields, body = parsed
        required, allowed = {"name", "description"}, {"name", "description"}
        missing = required - fields.keys()
        extra = fields.keys() - allowed
        for key in sorted(missing):
            self.error("FM010", path, f"missing required frontmatter field '{key}'")
        for key in sorted(extra):
            self.error("FM011", path, f"unsupported frontmatter field '{key}'; only name and description are allowed")

        name = fields.get("name", "")
        if name and not NAME_RE.fullmatch(name):
            self.error("FM020", path, "name must be lowercase kebab-case: [a-z0-9]+(-[a-z0-9]+)*")
        if name.endswith("-skill") or name == "skill":
            self.warn("FM021", path, "skill names should not include the generic term 'skill'")

        desc = fields.get("description", "")
        if desc:
            if len(desc) < 40:
                self.warn("FM030", path, "description is too short to be a reliable trigger")
            if len(desc) > 1024:
                self.error("FM031", path, "description exceeds 1024 characters")
            if not re.search(r"\b(use|when|for|select|implement|create|design|review|validate)\b", desc, re.I):
                self.warn("FM032", path, "description should state what the skill does and when/where to use it")

        body_lines = body.splitlines()
        if not re.search(r"(?m)^#\s+\S+", body):
            self.error("SK010", path, "body must contain a level-1 heading")
        if not body.strip():
            self.error("SK011", path, "body must contain operating instructions")
        if len(body_lines) > MAX_SKILL_LINES:
            self.warn("SK012", path, f"SKILL.md has {len(body_lines)} body lines; prefer <= {MAX_SKILL_LINES} and move details to references/")
        if re.search(r"(?im)^#{1,6}\s+when to use", body):
            self.warn("SK013", path, "put trigger conditions in frontmatter description rather than a 'When to use' body section")

    def parse_openai_yaml_minimal(self, text: str, path: Path) -> dict[str, str]:
        """Parse only interface scalar fields owned by this repository contract."""
        result: dict[str, str] = {}
        in_interface = False
        for line_no, raw in enumerate(text.splitlines(), start=1):
            if not raw.strip() or raw.lstrip().startswith("#"):
                continue
            if raw.strip() == "interface:":
                in_interface = True
                continue
            if not raw.startswith((" ", "\t")):
                in_interface = False
                continue
            if in_interface:
                match = re.match(r"^\s{2}([a-z_][a-z0-9_]*):\s*(.*?)\s*$", raw)
                if not match:
                    self.error("AG003", path, f"unsupported interface YAML syntax at line {line_no}")
                    continue
                key, value = match.groups()
                result[key] = value.strip().strip('"\'')
        return result

    def validate_agents(self) -> None:
        path = self.root / "agents" / "openai.yaml"
        if not path.is_file():
            self.error("AG001", path, "agents/openai.yaml is required")
            return
        text = self.read_text(path)
        if text is None:
            return
        fields = self.parse_openai_yaml_minimal(text, path)
        for key in ("display_name", "short_description"):
            if not fields.get(key):
                self.error("AG010", path, f"interface.{key} is required")
        display = fields.get("display_name", "")
        short = fields.get("short_description", "")
        if display and ("-" in display and " " not in display):
            self.warn("AG020", path, "display_name should be human-readable, usually with spaces rather than a slug")
        if short and len(short) > 120:
            self.warn("AG021", path, "short_description is long; keep UI metadata concise")

    def validate_links(self, source: Path, text: str) -> None:
        candidates: set[str] = set()
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1).strip().split()[0].strip("<>\"'")
            candidates.add(target)
        candidates.update(BACKTICK_PATH_RE.findall(text))

        for target in sorted(candidates):
            if not target or target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            resolved = (source.parent / target).resolve()
            try:
                resolved.relative_to(self.root)
            except ValueError:
                self.error("LK001", source, f"link escapes repository root: {target}")
                continue
            if not resolved.exists():
                self.error("LK002", source, f"broken local reference: {target}")

    def validate_all_markdown_links(self) -> None:
        for path in self.root.rglob("*.md"):
            if any(part in DISALLOWED_DIRS for part in path.parts):
                continue
            text = self.read_text(path)
            if text is not None:
                self.validate_links(path, text)

    def validate_naming(self) -> None:
        styles = self.root / "skills"
        if styles.is_dir():
            for child in styles.iterdir():
                if child.is_dir() and not NAME_RE.fullmatch(child.name):
                    self.error("NM010", child, "style directory must use lowercase kebab-case")

        for path in self.root.rglob("*"):
            rel = path.relative_to(self.root)
            if any(part in DISALLOWED_DIRS for part in rel.parts):
                continue
            name = path.name
            if name in ALLOWED_ROOT_NAMES or name in {"SKILL.md", "openai.yaml"}:
                continue
            if name.startswith("."):
                continue
            if path.is_file() and not LOWER_KEBAB_RE.fullmatch(name):
                self.warn("NM020", path, "prefer lowercase kebab-case filenames (dots allowed for compound extensions)")
            if path.is_dir() and not NAME_RE.fullmatch(name):
                self.warn("NM021", path, "prefer lowercase kebab-case directory names")

    def validate_packaging(self) -> None:
        total = 0
        file_count = 0
        for path in self.root.rglob("*"):
            rel = path.relative_to(self.root)
            if any(part in DISALLOWED_DIRS for part in rel.parts):
                if path.is_dir() and path.name != ".git":
                    self.error("PK010", path, f"development/cache directory must not be packaged: {path.name}")
                continue
            if path.is_symlink():
                self.error("PK011", path, "symbolic links are not allowed in the distributable package")
                continue
            if not path.is_file():
                continue
            file_count += 1
            if path.name in DISALLOWED_FILES or path.suffix in {".pyc", ".pyo"}:
                self.error("PK012", path, "generated/system file must not be packaged")
            try:
                size = path.stat().st_size
            except OSError as exc:
                self.error("PK013", path, f"cannot stat file: {exc}")
                continue
            total += size
            if size > MAX_PACKAGE_BYTES:
                self.error("PK020", path, "single file exceeds the 25 MB package limit")

        if total > MAX_PACKAGE_BYTES:
            self.error("PK021", self.root, f"package content is {total / 1024 / 1024:.2f} MB; limit is 25 MB")
        if file_count == 0:
            self.error("PK022", self.root, "package contains no files")

        nested = [p for p in (self.root / "skills").glob("*/SKILL.md")] if (self.root / "skills").is_dir() else []
        if nested and not (self.root / "SKILL.md").is_file():
            self.error("PK023", self.root, "nested style SKILL.md files exist but the root package entrypoint is missing")

    def run(self) -> int:
        if not self.root.is_dir():
            self.error("PK001", self.root, "repository/package root does not exist or is not a directory")
        else:
            self.validate_skill_md()
            self.validate_agents()
            self.validate_all_markdown_links()
            self.validate_naming()
            self.validate_packaging()

        errors = [finding for finding in self.findings if finding.severity == "ERROR"]
        warnings = [finding for finding in self.findings if finding.severity == "WARN"]
        for finding in self.findings:
            print(f"{finding.severity} {finding.code} {finding.path}: {finding.message}")
        print(f"\nSummary: {len(errors)} error(s), {len(warnings)} warning(s)")
        if errors or (self.strict and warnings):
            return 1
        return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate ui-morphism-design-skills packaging and Skill metadata")
    parser.add_argument("root", nargs="?", default=".", help="repository/package root (default: current directory)")
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = parser.parse_args()
    return Validator(Path(args.root), strict=args.strict).run()


if __name__ == "__main__":
    raise SystemExit(main())
