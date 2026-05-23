#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
VAULT_ROOT = WORKSPACE_ROOT

REQUIRED_FILES = [
    VAULT_ROOT / "AGENTS.md",
    VAULT_ROOT / "CLAUDE.md",
    VAULT_ROOT / "000_Semantic_Network_Context.md",
    VAULT_ROOT / "001_Semantic_Network_Overview.md",
    VAULT_ROOT / "ai" / "README.md",
    VAULT_ROOT / "ai" / "init-project-workflow.md",
    VAULT_ROOT / "ai" / "init-project-feedback.md",
    VAULT_ROOT / "ai" / "scripts" / "check_template_remote.py",
    VAULT_ROOT / "ai" / "zotero-import-template-guide.md",
    VAULT_ROOT / "Literature Review" / "README.md",
    VAULT_ROOT / "Literature Review" / "Overview Synthesis and Reading Map.md",
    VAULT_ROOT / "Literature Review" / "Synthesis" / "README.md",
    VAULT_ROOT / ".obsidian" / "plugins" / "obsidian-zotero-desktop-connector" / "data.json",
]

# CLAUDE.md files are symlinks to AGENTS.md — only check AGENTS.md to avoid duplicate wikilink errors
CHECK_LINK_FILES = [
    VAULT_ROOT / "README.md",
    VAULT_ROOT / "AGENTS.md",
    VAULT_ROOT / "000_Semantic_Network_Context.md",
    VAULT_ROOT / "001_Semantic_Network_Overview.md",
    VAULT_ROOT / "ai" / "README.md",
    VAULT_ROOT / "ai" / "init-project-workflow.md",
    VAULT_ROOT / "ai" / "init-project-feedback.md",
    VAULT_ROOT / "ai" / "paper-reading-guide-workflow.md",
    VAULT_ROOT / "ai" / "synthesis-integration-workflow.md",
    VAULT_ROOT / "ai" / "zotero-import-template-guide.md",
    VAULT_ROOT / "Literature Review" / "README.md",
    VAULT_ROOT / "Literature Review" / "Overview Synthesis and Reading Map.md",
    VAULT_ROOT / "Literature Review" / "Synthesis" / "README.md",
    VAULT_ROOT / "Literature Review" / "Sources by Domain.md",
]

# Symlinks that must point to the correct target
EXPECTED_SYMLINKS = {
    VAULT_ROOT / "CLAUDE.md": "AGENTS.md",
}

FORBIDDEN_SUBSTRINGS = [
    "literature_review_workflow",
    "THESIS_CONTEXT",
    "Thesis Overview",
    "TfT_Notes_Vault",
    "Project_Vault",
    "/mnt/user-data",
    "present_files",
    "OneDrive-backed vault",
    "BEGIN RSA PRIVATE KEY",
    "593168a6d13090de9beb65dc3bdcca9ddc114bb288a69383f91ed8a7988fc6d5",
]

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
MARKDOWN_FILE_REF_RE = re.compile(r"`([^`]+\.md)`")


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
            raw_target = match.group(1).split("|", 1)[0].split("#", 1)[0].rstrip("/")
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


def check_markdown_file_refs(errors: list[str]) -> None:
    """Catch stale literal `.md` references in shared docs after file renames."""
    for path in CHECK_LINK_FILES:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_FILE_REF_RE.finditer(text):
            raw = match.group(1)
            if "{{" in raw or "}}" in raw or "{" in raw or "}" in raw:
                continue
            candidate = VAULT_ROOT / raw
            if not candidate.exists() and "/" not in raw:
                # Root-level note reference, e.g. `Project Overview.md`.
                errors.append(f"Stale markdown file reference in {path.relative_to(VAULT_ROOT)}: `{raw}`")


def check_plugin_config(errors: list[str]) -> None:
    path = VAULT_ROOT / ".obsidian" / "plugins" / "obsidian-zotero-desktop-connector" / "data.json"
    if not path.exists():
        return
    
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        errors.append(f"Could not parse {path.relative_to(VAULT_ROOT)}")
        return
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


def is_git_ignored(path: Path) -> bool:
    rel_path = path.relative_to(VAULT_ROOT)
    result = subprocess.run(
        ["git", "check-ignore", "-q", str(rel_path)],
        cwd=VAULT_ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


def check_local_rest_config(errors: list[str]) -> None:
    path = VAULT_ROOT / ".obsidian" / "plugins" / "obsidian-local-rest-api" / "data.json"
    if not path.exists():
        return
    if is_git_ignored(path):
        return
    
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        errors.append(f"Could not parse {path.relative_to(VAULT_ROOT)}")
        return
    api_key = data.get("apiKey", "")
    if api_key and api_key != "REPLACE_WITH_LOCAL_OBSIDIAN_REST_API_KEY":
        errors.append("Local REST API data.json contains a non-placeholder apiKey")

    crypto = data.get("crypto", {})
    for key in ("cert", "privateKey", "publicKey"):
        value = crypto.get(key, "")
        if "PRIVATE KEY" in value or "BEGIN CERTIFICATE" in value or "BEGIN PUBLIC KEY" in value:
            errors.append(f"Local REST API data.json contains generated TLS material in crypto.{key}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_symlinks(errors)
    check_wikilinks(errors)
    check_forbidden_strings(errors)
    check_markdown_file_refs(errors)
    check_plugin_config(errors)
    check_local_rest_config(errors)

    if errors:
        print("AI documentation validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("AI documentation validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
