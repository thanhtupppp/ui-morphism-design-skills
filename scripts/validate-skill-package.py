#!/usr/bin/env python3
"""Release-grade validator for ui-morphism-design-skills.

Validates either a repository directory or a packaged skill.zip. The repository
root is one distributable Skill; nested skills/<style>/SKILL.md files are
internal style modules, not separate packages.
"""
from __future__ import annotations

import argparse
import json
import re
import stat
import tempfile
import zipfile
from dataclasses import asdict, dataclass
from pathlib import Path, PurePosixPath

MAX_PACKAGE_BYTES = 25 * 1024 * 1024
MAX_UNCOMPRESSED_ZIP_BYTES = 100 * 1024 * 1024
MAX_ZIP_RATIO = 100.0
MAX_SKILL_LINES = 500
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
LOWER_KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*(?:\.[a-z0-9]+)*$")
MARKDOWN_LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
BACKTICK_PATH_RE = re.compile(
    r"`((?:references|scripts|assets|agents|skills|domains|templates|tests)/[^`\s]+|(?:SKILL|README)\.md|skill\.json)`"
)
DISALLOWED_DIRS = {
    ".git", "node_modules", "__pycache__", ".pytest_cache", ".mypy_cache",
    ".ruff_cache", ".idea", ".vscode", "dist", "build",
}
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
        self.frontmatter: dict[str, str] = {}
        self.agent_fields: dict[str, str] = {}
        self.skill_json: dict = {}

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

    def parse_frontmatter(self, text: str, path: Path):
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
        return fields, "\n".join(lines[end + 1:]).lstrip("\n")

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
        self.frontmatter = fields
        for key in sorted({"name", "description"} - fields.keys()):
            self.error("FM010", path, f"missing required frontmatter field '{key}'")
        for key in sorted(fields.keys() - {"name", "description"}):
            self.error("FM011", path, f"unsupported frontmatter field '{key}'; only name and description are allowed")
        name = fields.get("name", "")
        desc = fields.get("description", "")
        if name and not NAME_RE.fullmatch(name):
            self.error("FM020", path, "name must be lowercase kebab-case")
        if name.endswith("-skill") or name == "skill":
            self.warn("FM021", path, "skill names should not include the generic term 'skill'")
        if desc and len(desc) < 40:
            self.warn("FM030", path, "description is too short to be a reliable trigger")
        if len(desc) > 1024:
            self.error("FM031", path, "description exceeds 1024 characters")
        if desc and not re.search(r"\b(use|when|for|select|implement|create|design|review|validate|adapt)\b", desc, re.I):
            self.warn("FM032", path, "description should state what the skill does and when/where to use it")
        if not re.search(r"(?m)^#\s+\S+", body):
            self.error("SK010", path, "body must contain a level-1 heading")
        if not body.strip():
            self.error("SK011", path, "body must contain operating instructions")
        if len(body.splitlines()) > MAX_SKILL_LINES:
            self.warn("SK012", path, f"SKILL.md exceeds {MAX_SKILL_LINES} body lines; move detail to references/")
        if re.search(r"(?im)^#{1,6}\s+when to use", body):
            self.warn("SK013", path, "put trigger conditions in frontmatter description rather than a 'When to use' body section")

    def parse_openai_yaml_minimal(self, text: str, path: Path) -> dict[str, str]:
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
        self.agent_fields = fields
        for key in ("display_name", "short_description"):
            if not fields.get(key):
                self.error("AG010", path, f"interface.{key} is required")
        display = fields.get("display_name", "")
        short = fields.get("short_description", "")
        if display and "-" in display and " " not in display:
            self.warn("AG020", path, "display_name should be human-readable")
        if len(short) > 120:
            self.warn("AG021", path, "short_description is long; keep UI metadata concise")

    def validate_skill_json(self) -> None:
        path = self.root / "skill.json"
        if not path.is_file():
            self.warn("JS001", path, "skill.json is optional for ChatGPT packaging but required by this repository manifest contract")
            return
        text = self.read_text(path)
        if text is None:
            return
        try:
            parsed = json.loads(text)
        except json.JSONDecodeError as exc:
            self.error("JS002", path, f"invalid JSON: {exc}")
            return
        if not isinstance(parsed, dict):
            self.error("JS003", path, "manifest must be a JSON object")
            return
        self.skill_json = parsed
        for key in ("name", "version", "description", "styles", "platforms", "workflow", "source_of_truth", "contracts"):
            if key not in parsed:
                self.error("JS010", path, f"missing repository manifest field '{key}'")
        if isinstance(parsed.get("name"), str) and not NAME_RE.fullmatch(parsed["name"]):
            self.error("JS011", path, "name must use lowercase kebab-case")
        if isinstance(parsed.get("version"), str) and not SEMVER_RE.fullmatch(parsed["version"]):
            self.error("JS012", path, "version must use semantic versioning")
        if parsed.get("source_of_truth") != "SKILL.md":
            self.error("JS013", path, "source_of_truth must be SKILL.md")
        contracts = parsed.get("contracts")
        if isinstance(contracts, list):
            for ref in contracts:
                if not isinstance(ref, str):
                    self.error("JS014", path, "contracts entries must be strings")
                    continue
                target = (self.root / ref).resolve()
                try:
                    target.relative_to(self.root)
                except ValueError:
                    self.error("JS015", path, f"contract path escapes repository: {ref}")
                    continue
                if not target.is_file():
                    self.error("JS016", path, f"contract does not exist: {ref}")

    def validate_consistency(self) -> None:
        fm_name = self.frontmatter.get("name")
        js_name = self.skill_json.get("name") if self.skill_json else None
        if fm_name and js_name and fm_name != js_name:
            self.error("CF001", "skill.json", f"name '{js_name}' must match SKILL.md frontmatter name '{fm_name}'")
        display = self.agent_fields.get("display_name")
        manifest_display = self.skill_json.get("displayName") if self.skill_json else None
        if display and manifest_display and display.lower() not in manifest_display.lower():
            self.warn("CF002", "agents/openai.yaml", "display_name differs materially from skill.json displayName")
        desc = self.frontmatter.get("description", "")
        short = self.agent_fields.get("short_description", "")
        if desc and short and short.rstrip(".").lower() == desc.rstrip(".").lower():
            self.warn("CF003", "agents/openai.yaml", "short_description duplicates the long trigger description")

    def validate_links(self, source: Path, text: str) -> None:
        candidates: set[str] = set()
        for match in MARKDOWN_LINK_RE.finditer(text):
            candidates.add(match.group(1).strip().split()[0].strip("<>\"'"))
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
            rel = path.relative_to(self.root)
            if any(part in DISALLOWED_DIRS for part in rel.parts):
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
            if path.name in {"SKILL.md", "README.md", "LICENSE", "LICENSE.md", "openai.yaml", "skill.json"} or path.name.startswith("."):
                continue
            if path.is_file() and not LOWER_KEBAB_RE.fullmatch(path.name):
                self.warn("NM020", path, "prefer lowercase kebab-case filenames")
            if path.is_dir() and not NAME_RE.fullmatch(path.name):
                self.warn("NM021", path, "prefer lowercase kebab-case directory names")

    def validate_packaging(self) -> None:
        total = 0
        file_count = 0
        for path in self.root.rglob("*"):
            rel = path.relative_to(self.root)
            if any(part in DISALLOWED_DIRS for part in rel.parts):
                if path.is_dir() and path.name not in {".git", "dist", "build"}:
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
        nested = list((self.root / "skills").glob("*/SKILL.md")) if (self.root / "skills").is_dir() else []
        if nested and not (self.root / "SKILL.md").is_file():
            self.error("PK023", self.root, "nested style SKILL.md files exist but root package entrypoint is missing")

    def run_checks(self) -> None:
        if not self.root.is_dir():
            self.error("PK001", self.root, "package root does not exist or is not a directory")
            return
        self.validate_skill_md()
        self.validate_agents()
        self.validate_skill_json()
        self.validate_all_markdown_links()
        self.validate_naming()
        self.validate_packaging()
        self.validate_consistency()


def inspect_zip(path: Path) -> list[Finding]:
    findings: list[Finding] = []

    def add(severity: str, code: str, member: str, message: str) -> None:
        findings.append(Finding(severity, code, member, message))

    if path.name != "skill.zip":
        add("WARN", "ZP001", path.name, "distributable archive should be named exactly skill.zip")
    try:
        with zipfile.ZipFile(path) as archive:
            infos = archive.infolist()
            if not infos:
                add("ERROR", "ZP002", path.name, "archive is empty")
                return findings
            total_uncompressed = 0
            roots: set[str] = set()
            for info in infos:
                pp = PurePosixPath(info.filename)
                if info.filename.startswith(("/", "\\")) or ".." in pp.parts:
                    add("ERROR", "ZP010", info.filename, "unsafe archive path/path traversal")
                if pp.parts:
                    roots.add(pp.parts[0])
                mode = (info.external_attr >> 16) & 0xFFFF
                if stat.S_ISLNK(mode):
                    add("ERROR", "ZP011", info.filename, "symbolic links are not allowed in skill.zip")
                total_uncompressed += info.file_size
                if info.file_size > MAX_PACKAGE_BYTES:
                    add("ERROR", "ZP012", info.filename, "single uncompressed member exceeds 25 MB")
                if info.compress_size and info.file_size / info.compress_size > MAX_ZIP_RATIO:
                    add("ERROR", "ZP013", info.filename, f"compression ratio exceeds {MAX_ZIP_RATIO:.0f}:1")
            if total_uncompressed > MAX_UNCOMPRESSED_ZIP_BYTES:
                add("ERROR", "ZP014", path.name, "archive uncompressed size exceeds 100 MB safety limit")
            if path.stat().st_size > MAX_PACKAGE_BYTES:
                add("ERROR", "ZP015", path.name, "skill.zip exceeds 25 MB upload limit")
            files = {i.filename.rstrip("/") for i in infos if not i.is_dir()}
            root_skill = "SKILL.md" in files
            if not root_skill and len(roots) == 1:
                prefix = next(iter(roots)) + "/"
                root_skill = prefix + "SKILL.md" in files
            if not root_skill:
                add("ERROR", "ZP020", path.name, "archive must contain a root skill entrypoint SKILL.md")
            if len(roots) > 1 and "SKILL.md" not in files:
                add("ERROR", "ZP021", path.name, "archive has multiple top-level roots; package one skill directory")
    except (OSError, zipfile.BadZipFile) as exc:
        add("ERROR", "ZP003", path.name, f"invalid ZIP archive: {exc}")
    return findings


def render_text(findings: list[Finding], strict: bool) -> str:
    lines = [f"{f.severity} {f.code} {f.path}: {f.message}" for f in findings]
    errors = sum(f.severity == "ERROR" for f in findings)
    warnings = sum(f.severity == "WARN" for f in findings)
    lines.append(f"\nSummary: {errors} error(s), {warnings} warning(s){' (strict)' if strict else ''}")
    return "\n".join(lines)


def render_json(findings: list[Finding], strict: bool) -> str:
    errors = sum(f.severity == "ERROR" for f in findings)
    warnings = sum(f.severity == "WARN" for f in findings)
    return json.dumps({
        "ok": errors == 0 and not (strict and warnings),
        "errors": errors,
        "warnings": warnings,
        "strict": strict,
        "findings": [asdict(f) for f in findings],
    }, indent=2)


def render_sarif(findings: list[Finding]) -> str:
    rules: dict[str, dict] = {}
    results = []
    for finding in findings:
        rules.setdefault(finding.code, {
            "id": finding.code,
            "name": finding.code,
            "shortDescription": {"text": finding.message},
        })
        results.append({
            "ruleId": finding.code,
            "level": "error" if finding.severity == "ERROR" else "warning",
            "message": {"text": finding.message},
            "locations": [{"physicalLocation": {"artifactLocation": {"uri": finding.path}}}],
        })
    return json.dumps({
        "version": "2.1.0",
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "runs": [{
            "tool": {"driver": {"name": "ui-morphism-skill-validator", "rules": list(rules.values())}},
            "results": results,
        }],
    }, indent=2)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate ui-morphism-design-skills repository or skill.zip")
    parser.add_argument("target", nargs="?", default=".")
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    parser.add_argument("--format", choices=("text", "json", "sarif"), default="text")
    parser.add_argument("--output", help="write report to a file instead of stdout")
    args = parser.parse_args()
    target = Path(args.target)
    findings: list[Finding] = []

    if target.is_file() and target.suffix.lower() == ".zip":
        findings.extend(inspect_zip(target))
        if not any(f.code == "ZP003" for f in findings):
            with tempfile.TemporaryDirectory(prefix="skill-validate-") as temp_dir:
                with zipfile.ZipFile(target) as archive:
                    archive.extractall(temp_dir)
                base = Path(temp_dir)
                entries = [p for p in base.iterdir() if p.name != "__MACOSX"]
                root = entries[0] if len(entries) == 1 and entries[0].is_dir() and not (base / "SKILL.md").exists() else base
                validator = Validator(root, strict=args.strict)
                validator.run_checks()
                findings.extend(validator.findings)
    else:
        validator = Validator(target, strict=args.strict)
        validator.run_checks()
        findings.extend(validator.findings)

    if args.format == "json":
        output = render_json(findings, args.strict)
    elif args.format == "sarif":
        output = render_sarif(findings)
    else:
        output = render_text(findings, args.strict)

    if args.output:
        Path(args.output).write_text(output + "\n", encoding="utf-8")
    else:
        print(output)

    errors = sum(f.severity == "ERROR" for f in findings)
    warnings = sum(f.severity == "WARN" for f in findings)
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
