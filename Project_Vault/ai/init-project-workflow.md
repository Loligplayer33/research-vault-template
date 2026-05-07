---
title: Vault Initialization & Personalization Workflow
tags:
  - ai
  - workflow
  - setup
  - initialization
status: active
---

# Vault Initialization & Personalization Workflow

Use this note when the user wants to transform this generic template vault into a specific, individualized project vault. 

This is a highly interactive, conversational process. You must work step-by-step with the user, keeping them in the driver's seat. Do not execute the entire setup at once. 

## Execution Rules for the Agent

1. **One step at a time:** Ask a set of related questions, wait for the user's response, execute the file changes for that phase, and then move to the next phase.
2. **Persistent State Tracking:** At the start of this workflow, create a file named `ai/INIT_STATE.md` to act as a checklist. Update this file with an `[x]` after completing each phase. This ensures you and the user know the current state, even if the conversation is interrupted.
3. **Continuous Validation:** After modifying structural files or paths, you MUST run `python3 ai/scripts/validate_ai_docs.py` to catch broken wikilinks or symlinks immediately. Do not move to the next phase until the script passes.
4. **Update Python Scripts if Renaming:** If the user chooses to rename foundational files like `THESIS_CONTEXT.md` or `Thesis Overview.md`, you MUST update the hardcoded paths in `ai/scripts/validate_ai_docs.py` to match the new names.

---

## Phase 1: Discovery & Core Project Details

**Agent Action:** Ask the user to define the core parameters of their research.

Ask the user:
1. What is the working title of the project?
2. What is the main research question or core problem you are investigating?
3. What are the key deliverables? (e.g., A systematic literature review, a taxonomy, a specific prototype, a thesis manuscript).
4. Do you want to rename the core contextual files (e.g., `THESIS_CONTEXT.md` to `PROJECT_CONTEXT.md`, `Thesis Overview.md` to `Project Overview.md`) to better fit your project type?

*Wait for response.*

**Execution:** 
- Inject the provided answers into the placeholder brackets inside `THESIS_CONTEXT.md` and `Thesis Overview.md`.
- If the user requested file renames, execute the renames via bash, update ALL internal wikilinks in the vault that point to them, and update `ai/scripts/validate_ai_docs.py` to check for the new filenames.
- Run validation script. Update `ai/INIT_STATE.md`.

---

## Phase 2: Literature Review & Synthesis Setup

**Agent Action:** Ask the user to define the foundational structure for their literature review.

Ask the user:
1. What is the primary guiding question for your literature review?
2. Let's establish your Synthesis Themes. What are 4-8 core themes, dimensions, or arguments you need to track across your readings? (Provide 2-3 examples based on their Phase 1 answers to help them brainstorm).
3. Do you have any initial "Phase 1" papers or authors you already know you need to read?

*Wait for response.*

**Execution:**
- Create a new markdown file for each theme inside `Literature Review/Synthesis/`. Use the template structure outlined in `Literature Review/Synthesis/README.md`.
- Update `Literature Review/Overview Synthesis and Reading Map.md` with the new guiding question, the themes, and any initial reading lists provided.
- Update `Literature Review/README.md` to reflect the specific literature guiding question.
- Run validation script. Update `ai/INIT_STATE.md`.

---

## Phase 3: Glossary & Theory Initialization

**Agent Action:** Ask the user to seed the glossary.

Ask the user:
1. Are there any foundational terms, theories, or acronyms specific to this project that we should establish right now? Defining them early helps keep our future writing and my contextual understanding consistent.

*Wait for response.*

**Execution:**
- Populate `Glossary.md` with the user's definitions. If the user provides a theory but doesn't know the exact definition, offer to generate a standard academic definition for them to review and approve.
- Update `ai/INIT_STATE.md`.

---

## Phase 4: Agent Context Finalization

**Agent Action:** Finalize the AI instructions so future agent sessions understand the project natively.

**Execution (No user input required for this step):**
- Rewrite the `## Project Context` section inside `AGENTS.md` using a crisp, synthesized summary of everything you learned in Phase 1 and Phase 2. 
- Ensure `AGENTS.md` explicitly mentions the current core themes and the project deliverables.
- Run `python3 ai/scripts/validate_ai_docs.py` one final time to guarantee the vault is fully healthy.

**Agent Action:** Present a completion summary.
- Tell the user the initialization is complete.
- Print out the final checklist of what was accomplished.
- Delete the temporary `ai/INIT_STATE.md` file.
- Ask the user what paper or task they would like to tackle first!