#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[3]
VAULT_ROOT = WORKSPACE_ROOT / "Project_Vault"

REQUIRED_FILES = [
    VAULT_ROOT / "AGENTS.md",
    VAULT_ROOT / "CLAUDE.md",
    VAULT_ROOT / "THESIS_CONTEXT.md",
    VAULT_ROOT / "ai" / "README.md",
    VAULT_ROOT / "ai" / "zotero-import-template-guide.md",
    VAULT_ROOT / "Literature Review" / "README.md",
    VAULT_ROOT / ".obsidian" / "plugins" / "obsidian-zotero-desktop-connector" / "data.json",
    # Root-level entrypoints
    WORKSPACE_ROOT / "AGENTS.md",
    WORKSPACE_ROOT / "CLAUDE.md",
]

# CLAUDE.md files are symlinks to AGENTS.md — only check AGENTS.md to avoid duplicate wikilink errors
CHECK_LINK_FILES = [
    VAULT_ROOT / "AGENTS.md",
    VAULT_ROOT / "THESIS_CONTEXT.md",
    VAULT_ROOT / "ai" / "README.md",
    VAULT_ROOT / "ai" / "zotero-import-template-guide.md",
    VAULT_ROOT / "Literature Review" / "README.md",
]

# Symlinks that must point to the correct target
EXPECTED_SYMLINKS = {
    VAULT_ROOT / "CLAUDE.md": "AGENTS.md",
    WORKSPACE_ROOT / "CLAUDE.md": "AGENTS.md",
}

FORBIDDEN_SUBSTRINGS = [
    "literature_review_workflow",
]

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def collect_markdown_targets(root: Path) -> set[str]:
    return {
        str(path.relative_to(root).with_suffix("")).replace("\\", "/")
        for path in root.rglob("*.md")
    }


def check_required_files(errors: list[str]) -> None:
    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"Missing required file: {path}")


def check_wikilinks(errors: list[str]) -> None:
    known_targets = collect_markdown_targets(VAULT_ROOT)
    for path in CHECK_LINK_FILES:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for match in WIKILINK_RE.finditer(text):
            raw_target = match.group(1).split("|", 1)[0].rstrip("/")
            if "{{" in raw_target or "}}" in raw_target:
                continue
            if raw_target not in known_targets:
                errors.append(f"Broken wikilink in {path.relative_to(VAULT_ROOT)}: [[{raw_target}]]")


def check_symlinks(errors: list[str]) -> None:
    for path, expected_target in EXPECTED_SYMLINKS.items():
        if not path.exists():
            continue  # already caught by check_required_files
        if not path.is_symlink():
            errors.append(f"{path.relative_to(WORKSPACE_ROOT)} should be a symlink to {expected_target}")
        elif os.readlink(path) != expected_target:
            errors.append(
                f"{path.relative_to(WORKSPACE_ROOT)} symlink points to "
                f"'{os.readlink(path)}', expected '{expected_target}'"
            )


def check_forbidden_strings(errors: list[str]) -> None:
    for path in CHECK_LINK_FILES:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for token in FORBIDDEN_SUBSTRINGS:
            if token in text:
                errors.append(f"Forbidden stale string '{token}' found in {path.relative_to(VAULT_ROOT)}")


def check_plugin_config(errors: list[str]) -> None:
    path = VAULT_ROOT / ".obsidian" / "plugins" / "obsidian-zotero-desktop-connector" / "data.json"
    if not path.exists():
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    export_formats = {fmt["name"]: fmt for fmt in data.get("exportFormats", [])}

    overview = export_formats.get("Import overview paper")
    zotero = export_formats.get("Import Zotero notes")

    if overview is None:
        errors.append("Plugin config missing export format: Import overview paper")
    if zotero is None:
        errors.append("Plugin config missing export format: Import Zotero notes")
    if overview and overview.get("outputPathTemplate") != "Literature Review/imports/{{citekey}}.md":
        errors.append("Import overview paper output path is not the expected citekey-based imports path")
    if zotero and zotero.get("outputPathTemplate") != "Literature Review/zotero_notes/{{citekey}}-zotero-notes.md":
        errors.append("Import Zotero notes output path is not the expected stable zotero_notes path")
    if zotero and zotero.get("imageOutputPathTemplate") != "Literature Review/zotero_notes/{{citekey}}-zotero-notes-assets":
        errors.append("Import Zotero notes image output path is not the expected stable asset path")
    if overview and overview.get("imageOutputPathTemplate") != "Literature Review/zotero_notes/{{citekey}}-zotero-notes-assets":
        errors.append("Import overview paper should share the Zotero notes asset path")
    if overview and overview.get("imageBaseNameTemplate") != "annotation":
        errors.append("Import overview paper should use imageBaseNameTemplate 'annotation'")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_symlinks(errors)
    check_wikilinks(errors)
    check_forbidden_strings(errors)
    check_plugin_config(errors)

    if errors:
        print("AI documentation validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("AI documentation validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
