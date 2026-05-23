---
title: Init Project Workflow Feedback
tags:
  - ai
  - workflow
  - setup
  - feedback
status: active
---

# Init Project Workflow Feedback

This note preserves developer feedback from a hands-on test of [[ai/init-project-workflow]]. Treat the conversation transcript as the primary source and this note as the structured handoff.

## Conversation Behavior

- Keep the user in the current phase unless they clearly ask to skip ahead. If the user says to continue setup, resume from the last explained section rather than jumping to installation.
- When the user says "note for later" or "do not respond to this", record the feedback in setup state or this feedback note and continue without summarizing it back.
- Agent-facing workflow docs should use clear filenames and paths. Do not replace agent-facing paths with Obsidian wikilinks just to make chat output clickable.
- Do not use awkward chat code citations as a workaround for clickable file references unless the user asks for that exact format.

## Orientation

- The Project Overview link issue in the test conversation was a chat-presentation issue, not an Obsidian wikilink or hub-structure issue. Do not overcorrect by adding unnecessary vault links.
- `Literature Review/README.md` may be too redundant with the project context and reading map. This is an open design discussion, not a finalized change.
- In the core paper loop, explain that the main paper note is usually a thin wrapper/navigation hub to the Zotero note and linked material. It can hold light context, but it is not the primary place for paper-level thinking.
- The paper reading guide belongs before close reading. It helps connect the paper to the current notes, existing arguments, and synthesis priorities before the user reads in detail.
- The synthesis integration workflow should be connected back to the paper loop and should explain `PC`, `WT`, `SP`, and `META` before using those abbreviations.

## Installation

- Better BibTeX citekey check: select the Zotero item and look for the citekey in the details panel on the right, near the top.
- Zotero Integration templates/config can ship with the vault, but the plugin itself must always be installed manually. The vault does not ship plugin binaries.
- The Local REST API plugin is called **Local REST API & MCP Server** in Obsidian.
- The Local REST API & MCP Server plugin also has an MCP configuration example for Claude Code farther down in its settings.
- If MCP points at the wrong vault during developer testing, continue with direct file access if available and record MCP as a follow-up. Do not block template testing on MCP.

## Phase 4: Project Details

- Ask questions step by step, not all at once.
- Offer examples and formulation help, but do not write invented project details into the vault.
- Do not ask about external locations during setup.
- Only include project details explicitly provided by the user. Do not invent context, deliverables, claims, source lists, or planned structure.
- After setup, invite the user to start a follow-up chat if they want to expand project framing in more detail.
- Do not modify [[Glossary]] during setup. It should grow organically during research.

## Phase 5: Literature Setup

- Explain the goal of the phase before asking for inputs.
- Do not require comprehensive answers. The user may skip this phase entirely or provide only a few details.
- Reading map and synthesis notes are optional scaffolding. They can be populated later and the reading map can be removed if the user does not want it.
- Create only synthesis notes, reading-map sections, and source lists that the user explicitly names or confirms.
- Ask before creating a large set of synthesis notes.

## Phase 6: Workflow Calibration

- Briefly re-explain the paper reading guide and synthesis integration workflows here: what they do, why they are needed, and when they are used.
- Default choices from the test run:
  - Paper reading guides remain ephemeral inline chat output.
  - Synthesis checklists save to `ai/outputs/`.
  - Verdict labels remain `High`, `Moderate`, and `Light`.
  - Anchor notes stay at the default always-pull set.

## Phase 7: Cleanup

- Do not mark Phase 7 complete until cleanup has actually run or the user explicitly defers it.
- Developer/test mode should be explicit. In developer testing, it can be valid to keep `ai/INIT_STATE.md`, test imports, or local workspace state temporarily.
- Cleanup should separate reusable workflow changes from test-run artifacts.

## Related

- [[ai/init-project-workflow]]
- [[ai/README]]
- [[Literature Review/README]]
