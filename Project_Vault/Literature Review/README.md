---
title: Literature Review Workflow
tags:
  - workflow
  - literature-review
  - project
aliases:
  - Lit Review Workflow
  - Reading Plan - Literature Review
  - Literature Review Reading Plan
---
# Literature Review Workflow

This folder contains the working literature review for the project. The workflow spans three layers that feed into each other: Zotero (reading record), Obsidian (per-paper headers + thematic synthesis), and the Synthesis notes where cross-paper argument develops.

## Core Principle

- **Zotero** holds sources, metadata, PDFs, highlights, and in-situ reading reactions. This is the full reading record.
- **Obsidian per-paper layer** holds a thin header per paper (title + Zotero metadata + links). Paper-level thinking lives in the Zotero note, not here.
- **Obsidian synthesis layer** holds thematic notes in [[Literature Review/Synthesis/README|the Synthesis folder]] where arguments develop across papers.

## Workflow Per Paper

1. Add the paper to Zotero.
2. Read and annotate it in Zotero, capturing highlights and in-situ reactions.
3. Run `Import overview paper` (via templater or scripts) to create the thin header note in `Literature Review/imports/`.
4. Run `Import Zotero notes` to create the companion imported-material note in `Literature Review/zotero_notes/`.
5. Leave the Zotero-notes imports and their assets in `zotero_notes` so re-imports keep updating the same files.
6. Open the 1–3 synthesis notes the paper touches. For each:
   - Add 2–6 bullets under an H3 subheading wikilinked to the overview paper
   - If the paper shifts your thinking, update the **Working Thoughts** section of Current Argument. Once multiple papers back a claim, promote it into **Synthesized Position** with citations.
7. If the paper references sources worth tracking (without being read yet), add them to [[Literature Review/Sources by Domain]] under the relevant theme.

## Good Defaults

- Keep raw highlights and in-situ reactions in Zotero.
- Keep paper-level structure minimal in Obsidian — the Zotero note already does that work.
- Treat `Literature Review/imports/` as the default landing zone for newly imported main paper notes. Existing curated paper headers may be organized under `Literature Review/Papers/` by paper type.
- Treat substantive argument sections in `Literature Review/Synthesis/` as user-owned.
- Paper Contributions bullets in synthesis notes are 1–2 sentences max; compress further if they drift longer.
- In synthesis prose (Working Thoughts, Synthesized Position), use plain citekeys in parentheses like `(smith2024)`. The H3 wikilink in Paper Contributions handles backlink coverage.
- Stable terms go in [[Glossary]]. Open research questions live there too.
- Use Obsidian wikilinks for all internal vault references.

## Current Reading Orientation

The canonical overview note for the current source map is [[Literature Review/Overview Synthesis and Reading Map]].

## Reading Sequence

The literature review should answer your guiding question(s):

**[Insert your main literature review guiding question here]**

Reading happens in phases defined in [[Literature Review/Overview Synthesis and Reading Map]].

## What To Extract From Each Paper

When reading, capture the core points across the Zotero note and the relevant synthesis notes:

1. [Extraction point 1]
2. [Extraction point 2]
3. [Extraction point 3]

## Reading-Guide and Synthesis-Integration Workflows

Two AI-assisted workflows support the per-paper loop:

- [[ai/paper-reading-guide-workflow]] — produced *before* reading, given the paper PDF. Triage tool that labels each section Read closely / Read selectively / Skim / Skip and maps the paper to the synthesis notes it will feed. Inline markdown only; not archived to the vault.
- [[ai/synthesis-integration-workflow]] — run *after* reading and Zotero-note completion. Produces a standalone HTML checklist with PC/WT/SP/META items per touched synthesis note.

## Start Here

- [[Literature Review/Overview Synthesis and Reading Map]] — the reading map and source priorities
- [[Literature Review/Synthesis/README|Synthesis]] — the thematic synthesis notes
- [[Literature Review/templates/overview-paper-template]] — the paper header template
- [[Literature Review/Sources by Domain]] — tracking for sources referenced but not yet read
- [[Glossary]] — stable definitions