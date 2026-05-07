# Agent Rules

This file is the canonical source for agent rules in this vault. `CLAUDE.md` symlinks here — if you are reading this as `CLAUDE.md`, you are in the right place.

## Completion Checklist

You MUST complete these steps before finishing any task that modifies shared documentation, workflow, folder paths, naming conventions, or config. Do not skip these. Do not mark the task as done until both steps pass.

1. Update all affected shared docs: [[THESIS_CONTEXT]], notes in [[ai/README]], and relevant workflow notes in [[Literature Review/README]].
2. Run `python3 ai/scripts/validate_ai_docs.py` and confirm it passes.

## Rules

- Do NOT fabricate claims, sources, or citations. Accuracy and proper attribution are non-negotiable.
- Keep the user in the thinker role. When in doubt, ask questions rather than producing conclusions. Do not replace the user's judgment with unsupported recommendations.
- Respect the existing vault structure and naming conventions. If unsure, ask before reorganizing.
- Use Obsidian wikilinks for all internal vault references.
- Update canonical notes rather than duplicating content across files.
- Treat substantive argument text in `Literature Review/Synthesis/` as user-owned. Do not rewrite `Current Argument`, `Working Thoughts`, or `Synthesized Position` there unless the user explicitly asks; bottom tracking lists and reading-stub cleanup are okay when requested.

## Project Context

This vault is a research workspace template for academic research and literature review.

[INSERT YOUR PROJECT CONTEXT HERE]
(Describe your research topic, core concern, and deliverables here. For example: "This vault is the research workspace for a master's thesis about X, investigating Y...")

> **Note for new projects:** If you are starting a new project in this vault, ask the agent to run the [[ai/init-project-workflow]] to interactively set up the project context and synthesis files.

For the full project context, literature workflow details, and current reading orientation, read [[THESIS_CONTEXT]].

For Zotero import setup and template conventions:

- [[ai/zotero-import-template-guide]]

For active literature-review work:

- [[Literature Review/README]]

For paper synthesis integration (the "generate synthesis additions" workflow):

- [[ai/synthesis-integration-workflow]]

## Zotero Import Conventions

- New main paper notes import into `Literature Review/imports/`.
- Existing curated paper headers may be organized under `Literature Review/Papers/` by paper type.
- Raw Zotero notes and their assets live in `Literature Review/zotero_notes/`.
- Imported filenames MUST be citekey-based, not title-based.

See [[ai/zotero-import-template-guide]] for the full setup.