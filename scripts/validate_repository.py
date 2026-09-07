#!/usr/bin/env python3
"""Mechanical integrity checks for Better Research.

These checks validate repository structure only. Passing them does not imply
academic validity, source support, ethical approval, or quality-gate readiness.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

TEXT_SUFFIXES = {
    ".md", ".txt", ".yml", ".yaml", ".py", ".sh", ".bib", ".tex", ".json"
}

STALE_EXCLUDE = {
    "CHANGELOG.md",
}
STALE_EXCLUDE_PREFIXES = (
    "docs/migrations/",
)

SENSITIVE_PREFIXES = (
    "private/",
    "secrets/",
    "data/raw/",
    "data/processed/",
    "data/linkage/",
    "data/consent/",
    "literature/pdfs/",
)

LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
BIB_ENTRY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,", re.IGNORECASE)
FRONTMATTER_LINE_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")


def iter_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(".git/"):
            continue
        yield path, rel


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def check_markdown_links(errors: list[str]) -> None:
    for path, rel in iter_files():
        if path.suffix.lower() != ".md":
            continue
        text = read_text(path)
        if text is None:
            continue
        for raw in LINK_RE.findall(text):
            target = raw.strip().split()[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{rel}: link escapes repository: {raw}")
                continue
            if not resolved.exists():
                errors.append(f"{rel}: missing relative link target: {raw}")


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    result: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return result
        match = FRONTMATTER_LINE_RE.match(line)
        if match:
            result[match.group(1)] = match.group(2).strip()
    return {}


def check_skills(errors: list[str]) -> None:
    skills_root = ROOT / ".agents" / "skills"
    if not skills_root.is_dir():
        errors.append(".agents/skills directory is missing")
        return
    for skill_dir in sorted(p for p in skills_root.iterdir() if p.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{skill_dir.relative_to(ROOT)}: missing SKILL.md")
            continue
        text = skill_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        expected = skill_dir.name
        if fm.get("name") != expected:
            errors.append(
                f"{skill_file.relative_to(ROOT)}: frontmatter name "
                f"{fm.get('name')!r} != directory {expected!r}"
            )
        if not fm.get("description"):
            errors.append(f"{skill_file.relative_to(ROOT)}: missing description")


def check_stale_skill_names(errors: list[str]) -> None:
    needle = "dissertation-"
    for path, rel in iter_files():
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if rel in STALE_EXCLUDE or rel.startswith(STALE_EXCLUDE_PREFIXES):
            continue
        text = read_text(path)
        if text is not None and needle in text.lower():
            errors.append(f"{rel}: contains stale skill prefix '{needle}'")


def check_bibliography(errors: list[str]) -> None:
    bib = ROOT / "literature" / "references.bib"
    if not bib.is_file():
        errors.append("literature/references.bib is missing")
        return
    text = bib.read_text(encoding="utf-8").strip()
    if not text:
        return
    if text.count("{") != text.count("}"):
        errors.append("literature/references.bib: unbalanced braces")
    keys = BIB_ENTRY_RE.findall(text)
    at_count = len(re.findall(r"(?m)^\s*@", text))
    if at_count != len(keys):
        errors.append(
            "literature/references.bib: one or more BibTeX entries "
            "do not match '@type{citation-key,'"
        )
    duplicates = sorted({k for k in keys if keys.count(k) > 1})
    if duplicates:
        errors.append(
            "literature/references.bib: duplicate citation keys: "
            + ", ".join(duplicates)
        )


def check_sensitive_paths(errors: list[str]) -> None:
    for path, rel in iter_files():
        if rel == ".env" or (rel.startswith(".env.") and rel != ".env.example"):
            errors.append(f"{rel}: environment secret file must not be committed")
        if rel.startswith(SENSITIVE_PREFIXES):
            errors.append(f"{rel}: sensitive/private path must not be committed")


def main() -> int:
    errors: list[str] = []
    check_markdown_links(errors)
    check_skills(errors)
    check_stale_skill_names(errors)
    check_bibliography(errors)
    check_sensitive_paths(errors)

    if errors:
        print("Repository integrity checks FAILED:")
        for error in sorted(set(errors)):
            print(f"  - {error}")
        return 1

    print("Repository integrity checks passed.")
    print(
        "Scope: mechanical repository integrity only; "
        "this is not an academic quality assessment."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
