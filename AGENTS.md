# Agent Rules

This file is the canonical source for agent rules in this vault. `CLAUDE.md` symlinks here — if you are reading this as `CLAUDE.md`, you are in the right place.

## Completion Checklist

You MUST complete these steps before finishing any task that modifies shared documentation, workflow, folder paths, naming conventions, or config. Do not skip these. Do not mark the task as done until both steps pass.

1. Update all affected shared docs: [[000_Semantic_Network_Context]], notes in [[ai/README]], and relevant workflow notes in [[Literature Review/README]].
2. Run `python3 ai/scripts/validate_ai_docs.py` and confirm it passes.

## Rules

- Do NOT fabricate claims, sources, or citations. Accuracy and proper attribution are non-negotiable.
- Keep the user in the thinker role. When in doubt, ask questions rather than producing conclusions. Do not replace the user's judgment with unsupported recommendations.
- Respect the existing vault structure and naming conventions. If unsure, ask before reorganizing.
- Use Obsidian wikilinks for all internal vault references.
- Update canonical notes rather than duplicating content across files.
- Treat substantive argument text in `Literature Review/Synthesis/` as user-owned. Do not rewrite `Current Argument`, `Working Thoughts`, or `Synthesized Position` there unless the user explicitly asks; bottom tracking lists and reading-stub cleanup are okay when requested.

## Project Context

This vault is the research workspace for a **seminar / independent research project** titled **"Project - Local AI Semantic Network Architectures."** It investigates **how local AI automation can assist in organizing large personal knowledge bases, like an Obsidian vault, specifically to reduce manual linking and tag clutter**.

**Deliverables:** systematic literature review (PKM frameworks and automated tagging methods), formal taxonomy for note types and relationships, basic prototype tool or local script to suggest backlinks, concise project manuscript.

**Literature guiding question:** How can automated graph construction and local graph-based retrieval be optimized for highly personalized, markdown-based knowledge environments to prevent semantic drift over time?

**Synthesis notes:** The Problem, Design Strategies, Open Questions; Graph Extraction Accuracy, Semantic Drift Prevention, Context-Awareness and Personalization, Local Computational Overhead, Human-in-the-Loop Interaction Design. See [[Literature Review/Synthesis/README]] and [[Literature Review/Overview Synthesis and Reading Map]].

**Minimum viable reading set:** GraphRAG (From Local to Global), PROM, PersonaAgent with GraphRAG — see reading map for full titles.

**Context files:** [[000_Semantic_Network_Context]], [[001_Semantic_Network_Overview]].

**MCP:** Configured in Cursor; during template testing, local file access was used when MCP pointed at another vault.

For the full project context, literature workflow details, and current reading orientation, read [[000_Semantic_Network_Context]].

For the one-page current-state map, read [[001_Semantic_Network_Overview]].

For Zotero import setup and template conventions:

- [[ai/zotero-import-template-guide]]

For active literature-review work:

- [[Literature Review/README]]

For pre-reading paper triage:

- [[ai/paper-reading-guide-workflow]]

For paper synthesis integration (the "generate synthesis additions" workflow):

- [[ai/synthesis-integration-workflow]]

## Zotero Import Conventions

- New main paper notes import into `Literature Review/imports/`.
- Existing curated paper headers may be organized under `Literature Review/Papers/` by paper type.
- Raw Zotero notes and their assets live in `Literature Review/zotero_notes/`.
- Imported filenames MUST be citekey-based, not title-based.
- Generated synthesis checklist artifacts live in `ai/outputs/` and should not use external artifact paths.

See [[ai/zotero-import-template-guide]] for the full setup.