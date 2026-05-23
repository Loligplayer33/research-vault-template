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
- **Obsidian per-paper layer** holds a thin wrapper per paper (title + Zotero metadata + links). It is mainly a navigation hub to the Zotero note and linked material. Light paper-level context can live here when useful, but the full reading record lives in Zotero/Zotero notes.
- **Obsidian synthesis layer** holds thematic notes in [[Literature Review/Synthesis/README|the Synthesis folder]] where arguments develop across papers.

## Workflow Per Paper

1. Add the paper to Zotero.
2. Before close reading, optionally run [[ai/paper-reading-guide-workflow]] on the paper PDF. Use it when you want the paper routed against the current context, reading map, and synthesis notes before deciding what to read closely, skim, or skip.
3. Read and annotate it in Zotero, capturing highlights and in-situ reactions.
4. Run `Import overview paper` to create the thin wrapper note in `Literature Review/imports/`.
5. Run `Import Zotero notes` to create the companion imported-material note in `Literature Review/zotero_notes/`.
6. Leave the Zotero-notes imports and their assets in `zotero_notes` so re-imports keep updating the same files.
7. Open the 1–3 synthesis notes the paper touches. For each:
   - Add 2–6 bullets under an H3 subheading wikilinked to the overview paper
   - If the paper shifts your thinking, update the **Working Thoughts** section of Current Argument. Once multiple papers back a claim, promote it into **Synthesized Position** with citations.
8. If the paper references sources worth tracking (without being read yet), add them to [[Literature Review/Sources by Domain]] under the relevant theme. Treat that note as a source bank; reading status belongs in [[Literature Review/Overview Synthesis and Reading Map]] and the per-paper notes.

## Good Defaults

- Keep raw highlights and in-situ reactions in Zotero.
- Keep paper-level structure minimal in Obsidian — the Zotero note already does that work.
- Treat `Literature Review/imports/` as the default landing zone for newly imported main paper notes. Existing curated paper headers may be organized under `Literature Review/Papers/` by paper type.
- Treat substantive argument sections in `Literature Review/Synthesis/` as user-owned. During cleanup, only reading lists, tracking stubs, or other explicitly requested maintenance there should be changed.
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

- [[ai/paper-reading-guide-workflow]] — produced *before* reading, given the paper PDF. Triage tool that commits a High / Moderate / Light relevance verdict, labels sections Read closely / Read selectively / Skim / Skip when warranted, and maps the paper to the synthesis notes it will feed. Inline markdown only; not archived to the vault unless the user asks.
- [[ai/synthesis-integration-workflow]] — run *after* reading and Zotero-note completion. Produces a standalone HTML checklist in `ai/outputs/{citekey}-synthesis-checklist.html` with a visible relevance verdict and PC/WT/SP/META items per touched synthesis note.

Abbreviations used by the synthesis integration checklist: PC = Paper Contributions, WT = Working Thoughts, SP = Synthesized Position, META = cleanup, linking, or caveat tasks.

## Start Here

- [[Literature Review/Overview Synthesis and Reading Map]] — the reading map and source priorities
- [[Literature Review/Synthesis/README|Synthesis]] — the thematic synthesis notes
- [[Literature Review/templates/overview-paper-template]] — the paper header template
- [[Literature Review/Sources by Domain]] — source bank for referenced and adjacent sources; use the reading map and per-paper notes for status
- [[Glossary]] — stable definitions
