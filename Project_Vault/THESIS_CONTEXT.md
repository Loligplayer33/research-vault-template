# Project Context

This vault is the working space for an academic research project.

## What the Project Is About

The project is titled **"[Insert Project Title Here]"**. It investigates **[Insert Main Subject/Research Question Here]**.

The core problem: **[Describe the core problem your research addresses here.]**

The project aims to **[Describe the goals/aims of the project here.]**

## The Deliverables

1. **Systematic Literature Review** — [Describe deliverable 1]
2. **[Deliverable 2]** — [Describe deliverable 2]
3. **[Deliverable 3]** — [Describe deliverable 3]
4. **[Deliverable 4]** — [Describe deliverable 4]

## What This Vault Is For

This vault is the research and thinking workspace for the project. It is where:

- Literature is collected, read, and annotated.
- Per-paper notes are connected to the broader research argument.
- Synthesis notes develop cross-paper claims over time.
- Draft-quality framing, terms, questions, and deliverable outlines are refined.

This vault does not have to be the codebase, prototype folder, or final writing repository. If those live elsewhere, document the handoff here.

## Current Literature Workflow

The current literature-review workflow in this vault is centered in:

- [[Literature Review/README]]
- [[ai/zotero-import-template-guide]]

The workflow spans three layers: Zotero (reading record), per-paper thin headers in Obsidian, and thematic synthesis notes in the [[Literature Review/Synthesis/README|Synthesis folder]] where arguments develop across papers.

Treat substantive argument text in `Literature Review/Synthesis/` as user-owned. Cleanup may update bottom reading/tracking stubs there, but `Current Argument`, `Working Thoughts`, and `Synthesized Position` should only be rewritten when the user explicitly asks.

### Import Logic

- New main literature notes import into `Literature Review/imports/`.
- Existing curated paper headers may be organized under `Literature Review/Papers/` by paper type.
- Raw Zotero notes and annotation-heavy imports are stored in `Literature Review/zotero_notes/`.
- Raw Zotero notes and their asset folders should stay in `zotero_notes` so re-imports keep updating the same files.
- Imported filenames should stay **citekey-based**, not title-based, to keep links stable and avoid long path problems in synced folders.

### Current Zotero Integration Commands

- `Import overview paper`
  - creates the main thin header note for a source
  - writes to `Literature Review/imports/{{citekey}}.md`
- `Import Zotero notes`
  - creates the companion raw note with Zotero item notes and PDF annotations
  - writes to `Literature Review/zotero_notes/{{citekey}}-zotero-notes.md`
  - uses the stable `zotero_notes` folder

### Asset Handling

- The Zotero-notes import owns the stable asset location:
  - `Literature Review/zotero_notes/{{citekey}}-zotero-notes-assets`
- Main-note imports may still trigger annotation asset extraction because of plugin behavior.
- To avoid stray top-level asset files, main-note imports should share the same asset path and base naming as the Zotero-notes import rather than creating a separate asset folder.

## Literature Framing

The detailed literature framing for this project should be treated as **provisional** and may evolve during the review.

For current reading orientation and source priorities, consult:

- [[Thesis Overview]]
- [[Literature Review/Overview Synthesis and Reading Map]]
- [[Literature Review/README]]

Do not assume that one current source list, one paper, or one early synthesis theme is the final settled grounding unless the notes in those locations clearly say so.

## Important Links

- [[Thesis Overview]] — Where the project stands currently
- [[Literature Review/README|Literature Review Workflow]]
- [[AGENTS|Agent Rules]]
- [[ai/README|AI Scripts & Tools]]