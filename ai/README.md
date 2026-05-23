---
title: AI Notes
tags:
  - ai
  - workflow
  - handoff
---

# AI Notes

This folder stores notes that help AI agents pick up workflow context quickly across chat sessions.

For agent rules, the completion checklist, and validation requirements, see [[AGENTS]].

Substantive argument text in [[Literature Review/Synthesis/README|Literature Review/Synthesis]] is user-owned. AI agents should treat general cleanup there as tracking/list cleanup only unless the user explicitly asks for argument edits.

## When to Update This Folder

If a change should survive across chat contexts, update or create a note here. This includes:

- Zotero or Obsidian config changes
- installation or MCP setup steps
- import command changes
- folder or path renames
- naming convention changes
- new workflow rules
- new project phases or changes in research focus

If you are adding a new reusable handoff note, add it to this folder and list it below.

## Current Guides

- [[ai/init-project-workflow]]
- [[ai/init-project-feedback]]
- [[ai/zotero-import-template-guide]]
- [[ai/synthesis-integration-workflow]]
- [[ai/paper-reading-guide-workflow]]

Use [[ai/init-project-workflow]] as the canonical setup runbook for new projects. It covers local installation, Better BibTeX, Zotero Integration, Local REST API, MCP verification, Zotero import testing, and project personalization.

Use [[ai/init-project-feedback]] when improving the setup workflow. It preserves developer feedback from a hands-on initialization test and separates open design feedback from transient setup state.

Before project-specific personalization, agents should run `python3 ai/scripts/check_template_remote.py`. Normal users should not keep `origin` pointed at `Loligplayer33/research-vault-template`; they should use GitHub's template flow or connect the vault to their own repository first.

The canonical reading-plan note is [[Literature Review/Overview Synthesis and Reading Map]]. Do not recreate duplicate reading-map notes at the vault root.

New main paper headers import into `Literature Review/imports/`. Existing curated paper headers may be organized under `Literature Review/Papers/` by paper type. Raw imported Zotero notes and annotation assets stay in `Literature Review/zotero_notes/`.

Generated synthesis checklist artifacts, when requested, should be written inside the vault at `ai/outputs/{citekey}-synthesis-checklist.html` rather than to external artifact paths. These HTML files are working artifacts for integration; keep them lightweight and regenerate them when the underlying synthesis state changes.

Reading guides are inline, ephemeral scaffolding unless the user explicitly asks to save one. The durable record remains the Zotero note plus any later synthesis-note additions.

## Current Cross-Vault Anchors

- [[000_Semantic_Network_Context]]
- [[001_Semantic_Network_Overview]]
- [[Literature Review/README]]
- [[Literature Review/Overview Synthesis and Reading Map]]
- [[Literature Review/Synthesis/README|Synthesis]]
- [[Glossary]]
