---
title: Zotero Import Template Guide
tags:
  - ai
  - zotero
  - obsidian
  - workflow
  - handoff
status: active
---

# Zotero Import Template Guide

Use this note in future AI chats when changing or extending the Zotero Integration setup for literature notes.

## Current Working Setup

- Plugin config file:
  - `.obsidian/plugins/obsidian-zotero-desktop-connector/data.json`
- Main note template:
  - `Literature Review/templates/overview-paper-template.md`
- Raw Zotero import template:
  - `Literature Review/templates/zotero-notes-template.md`
- Main import folder:
  - `Literature Review/imports/`
- Organized paper folder:
  - `Literature Review/Papers/`
- Stable raw Zotero folder:
  - `Literature Review/zotero_notes/`

## Current Commands

- `Import overview paper`
  - creates the thin wrapper/navigation note for overview paper types
  - output path:
    - `Literature Review/imports/{{citekey}}.md`
  - important:
    - this command should not create its own separate asset folder
    - it shares the stable Zotero-notes asset folder to avoid stray top-level assets caused by the plugin fallback behavior

- `Import Zotero notes`
  - universal raw-material import
  - creates the companion note with Zotero item notes and PDF annotations
  - output path:
    - `Literature Review/zotero_notes/{{citekey}}-zotero-notes.md`
  - image output path:
    - `Literature Review/zotero_notes/{{citekey}}-zotero-notes-assets`

## Naming Rules

- Use `{{citekey}}` for imported filenames.
- Do not use `{{title}}` for filenames in this vault.
- Reason:
  - title-based filenames can become too long in synced folders and cause timeouts, broken reads, or brittle links.
- Keep the full paper title inside the note body, not in the path.

## Structure Rules

- Main note commands are paper-type-specific.
  - `Import overview paper` is specific to overview papers.
  - future commands for other paper types should also be type-specific
- New imports land in `Literature Review/imports/` by default; existing curated headers may be organized under `Literature Review/Papers/` by paper type.

- `Import Zotero notes` is universal.
  - it should stay generic across paper types
  - it imports raw Zotero material, not project-specific thinking structure

- PDF annotation assets should only be exported by `Import Zotero notes`.
- In practice, the overview-paper command shares the Zotero-notes asset path because the plugin otherwise falls back to the vault base path and can create stray `image-*` files.
- Do not create a separate asset folder for the main paper-type commands unless there is a very explicit reason.

## Current Template Intent

### Main note

- Holds the thin project-facing wrapper for the paper.
- Links to the companion raw note using:
  - `Literature Review/zotero_notes/{{citekey}}-zotero-notes`
- Usually stays focused on navigation and light orientation:
  - Zotero metadata
  - link to the raw Zotero note
  - optional one-sentence takeaway or context that needs to be visible without opening the Zotero note

The main note is not the primary place for paper-level thinking. The full reading record lives in Zotero/Zotero notes, and cross-paper argument lives in synthesis notes.

### Raw Zotero note

- Holds imported raw source material.
- Current order:
  1. `Zotero`
  2. `PDF Annotations`
  3. `Zotero Item Notes`
- Horizontal separators are intentionally placed between all major sections.
- `Zotero Item Notes` means standalone child notes in Zotero.
- Comments typed onto PDF highlights belong to `PDF Annotations`, not `Zotero Item Notes`.

## How To Work With A Paper

After import, use the main literature note as the paper wrapper and navigation point. Reading-time reactions stay in Zotero/Zotero notes; cross-paper integration happens in synthesis notes.

1. Add the paper to Zotero.
2. Before close reading, optionally run [[ai/paper-reading-guide-workflow]] on the paper PDF to decide what to read closely, skim, or skip.
3. Read and annotate it in Zotero.
4. Run `Import overview paper`.
5. Run `Import Zotero notes` for the same paper.
6. Open the main note in `Literature Review/imports/` or its curated `Literature Review/Papers/` location, and the companion raw note in `Literature Review/zotero_notes/`.
7. Leave the raw Zotero note and its assets in `zotero_notes` so re-imports keep updating the same files.
8. Integrate from the Zotero note into the relevant synthesis notes. Optionally use [[ai/synthesis-integration-workflow]] after Zotero notes are complete.

The plugin creates the wrapper and imports the raw material. Analytical integration is completed manually in synthesis notes or with the synthesis integration checklist.

## Important Caveats

- The plugin's built-in `Import notes` command exists but is not part of this workflow.
- Do not patch it out unless explicitly asked.
- The plugin writes to fixed output paths.
- `zotero_notes` is intentionally the stable update location for raw Zotero imports and their assets.
- Do not move raw Zotero notes or their asset folders out of `zotero_notes` if you want re-imports to keep updating the same files.
- The plugin may still try to extract PDF annotation images during main-note imports.
- To avoid stray files at the vault root, main-note imports should share the Zotero-notes asset folder and base naming.

## Safe Procedure For Adding A New Paper-Type Import

1. Inspect the current plugin config in:
   - `.obsidian/plugins/obsidian-zotero-desktop-connector/data.json`
2. Keep `Import Zotero notes` unchanged unless the user explicitly wants raw-import behavior changed.
3. Create a new paper-type template in:
   - `Literature Review/templates/`
4. Add a new export format command with a paper-type-specific name.
   - examples:
     - `Import theory paper`
     - `Import empirical paper`
     - `Import framework paper`
5. Default main note output path:
   - `Literature Review/imports/{{citekey}}.md`
6. Link the main note to:
   - `Literature Review/zotero_notes/{{citekey}}-zotero-notes`
7. Point the main note command's asset path to the same stable Zotero-notes asset folder:
   - `Literature Review/zotero_notes/{{citekey}}-zotero-notes-assets`
   - use the same base naming as the raw import, currently `annotation`
8. Reload the plugin after config changes.
9. Test both:
   - the new paper-type command
   - `Import Zotero notes`

## When To Deviate From The Default

- If the user wants multiple distinct main-note files for the same paper type at once, then the filename strategy must change intentionally.
- Otherwise assume:
  - one canonical main note per paper
  - one canonical raw Zotero note per paper

## Good Future-Chat Summary

If starting from a fresh chat, summarize the setup like this:

> This vault uses Zotero Integration with one universal raw-import command (`Import Zotero notes`) and paper-type-specific main-note commands such as `Import overview paper`. Imported filenames must stay citekey-based because title-based filenames can become too long and brittle in synced folders. New main notes import into `Literature Review/imports/`; existing curated headers may be organized under `Literature Review/Papers/` by paper type. Raw Zotero notes and their assets live in `Literature Review/zotero_notes`, and main-note imports share that asset path to avoid stray image files at the vault root.

## Related Notes

- [[Literature Review/README]]
