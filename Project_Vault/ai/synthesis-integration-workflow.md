---
title: Synthesis Integration Workflow
tags:
  - ai
  - synthesis
  - workflow
  - handoff
status: active
---

# Synthesis Integration Workflow

Use this note in future AI chats when the user asks for the "integration step" or "synthesis additions" or "important points to integrate" for a specific paper they have finished reading and note-taking on.

## When This Workflow Triggers

Phrasings the user has used to invoke this:

- "Now perform the integration step."
- "Generate the important points for my synthesis."
- "Integrate this paper into my synthesis."
- "What should I add to the synthesis notes from this paper?"

Trigger only when the user has confirmed their Zotero notes are complete. If the user has only just finished reading the paper and not yet captured their reactions in the Zotero note, ask whether they want to do the note-taking pass first.

## Required Context (read in this order)

Always read fresh — the user iterates on these files between conversations.

1. `AGENTS.md` — already in context if vault is connected.
2. `THESIS_CONTEXT.md` — current project framing.
3. `Thesis Overview.md` — current state map of the four deliverables.
4. `Literature Review/Overview Synthesis and Reading Map.md` — reading plan and source map.
5. The paper's Zotero notes file: `Literature Review/zotero_notes/{citekey}-zotero-notes.md`.
   - Filenames are citekey-based and should follow the stable pattern `{citekey}-zotero-notes.md`.
   - **This file is the primary input.** It contains the user's reactions, reading-time judgments, and cross-paper connections that the synthesis additions must respect. Make sure to put emphasis on this.
1. All synthesis notes in `Literature Review/Synthesis/`
7. `Glossary.md` — for stable term definitions; do not redefine terms here.
8. The paper's main note in `Literature Review/imports/{citekey}.md` or under `Literature Review/Papers/` if it exists.

Use `obsidian_batch_get_file_contents` for efficiency if you are connected via MCP. Otherwise decide what is the best approach.

## Process

### Step 1 — Triage

For each synthesis note in `Literature Review/Synthesis/`, classify the paper's contribution:

- **Heavy** — substantive new material across multiple aspects of the note.
- **Medium** — meaningful contribution to one or two aspects.
- **Light** — one bullet's worth, possibly interpretive.
- **Skip** — paper does not substantively touch the note.

Skipped notes do not get their own section in the output. They are flagged in the cross-cutting reminders so the user knows the skip was deliberate, not an oversight.

### Step 2 — Identify the contribution type per touched note

For each touched note, determine whether the paper:

- **Confirms existing claims** → PC bullets; SP candidate if multiple papers now agree.
- **Sharpens existing claims** → PC bullets + WT update.
- **Qualifies existing claims** → PC bullets + WT update with explicit caveats.
- **Adds new material** → PC bullets + WT seed (if the note's WT is currently empty) or WT addendum.

### Step 3 — Watch for cross-paper signals

These belong in cross-cutting reminders, not in any single synthesis note:

- Disagreements with other papers, especially papers on the user's reading list.
- Future-reading pointers (papers cited that are not yet on the reading list).
- Methodological caveats that constrain how the paper can be cited.

### Step 4 — Decide on Synthesized Position drafts

Draft SP prose only when **three or more papers converge** on a claim. Below that threshold, propose SP candidate items as one-line pointers without drafted prose.

When drafting, mark explicitly as "first draft." Provide as a callout (purple, `.callout.sp`) immediately followed by an SP-tagged checkbox saying "Promote the SP draft above into the Synthesized Position section."

## Output Format

A standalone HTML file written to `/mnt/user-data/outputs/{citekey}-synthesis-checklist.html`, presented via `present_files`.

The file must match the style of existing checklists in this vault (if any). Reference existing scripts or HTML generation tools. Copy the CSS, JavaScript, callout patterns, and section structure exactly.

### Mandatory structural elements

- Sticky progress bar at the top with counter and section-level counts.
- Sections per touched synthesis note in the priority order from the cross-cutting reminders.
- Each item is a checkbox with a zone tag (PC, WT, SP, META).
- Callouts for WT seeds/updates (orange, `.callout`) and SP drafts (purple, `.callout.sp`).
- Cross-cutting reminders section at the bottom with META items and a numbered prioritization list.
- Reset button.
- `localStorage` persistence with `STORAGE_KEY = '{citekey}-checklist-v1'` — must be unique per paper so checklists don't collide.

### Tag conventions

- **PC** (green) — Paper Contributions: short pointer bullet matching existing synthesis-note bullet style.
- **WT** (orange) — Working Thoughts: prose in the user's voice.
- **SP** (purple) — Synthesized Position candidate.
- **META** (gray) — action on structure or links.

### PC bullet style

- Bold lead phrase identifying the key finding or concept.
- One to two sentences of explanation.
- Page references where relevant (`p42`, `§3.2.3`).
- Use citekeys when referring to other papers (e.g. `tankelevitch2024`, `colombatto2025`).
- Compressed: do not duplicate Zotero-note quotations. Synthesis layer is for cross-paper argument; Zotero already holds paper-level depth.
- Match the bullet style in the existing synthesis notes.

### WT prose style

- User's voice: direct, analytical, no padding.
- No conversational hedging ("might be worth," "perhaps consider").
- Frame as either "Append to your existing WT" (update) or "Add as initial WT entry" (seed).
- Acknowledge interpretive vs. direct contributions explicitly.
- Flag ambiguities rather than resolving them.
- Preserve numerical findings (effect sizes, percentages, p-values) and page references.

### Mandatory items in every checklist

- A META item to remove the paper's stub from any affected note's "To integrate once read" section.
- A META item in cross-cutting reminders explicitly flagging skipped synthesis notes with the reason for skipping.
- A META item in cross-cutting reminders saying "Don't duplicate the Zotero note."

### Priority ordering in cross-cutting reminders

- List touched notes in suggested integration order.
- Most-loaded note first (where the work pays off most).
- Lightest or most interpretive last.
- Skipped notes do not appear in the priority list.

## Style Guidelines

- Direct and analytical; avoid conversational softening.
- Do not write more than the source supports — distinguish empirical from interpretive contributions.
- When the paper qualifies a previous claim, surface the qualification in WT, not just in PC bullets.
- When the paper is silent on a synthesis dimension that prior papers covered, do not invent material.

## Anti-Patterns To Avoid

- Producing inline integration prose in the chat instead of an HTML artifact.
- PC bullets that duplicate Zotero-note quotations verbatim.
- Overlong PC bullets (more than ~3 sentences).
- Missing the "remove from To integrate once read" META cleanup.
- Forcing content into synthesis notes the paper does not touch.
- SP draft prose for claims with only one or two backing papers.
- Conversational tone instead of analytical register.
- Skipping the cross-cutting reminders section.
- Failing to set a unique `STORAGE_KEY` (causes localStorage collisions across papers).
- PC bullets that conflate the paper's operationalised variable with a higher-level mechanism it doesn't test (e.g. labelling exposure-confidence findings as 'fluency contamination evidence' when fluency was not measured).

## Pre-Flight Check

Before producing the checklist, confirm:

- Paper's Zotero notes have been read fresh (the user iterates between sessions).
- All synthesis notes have been read fresh (state may have changed).
- `THESIS_CONTEXT.md` and `Thesis Overview.md` have been read.
- For each PC bullet, confirm: what variable did the paper actually manipulate or measure? Does the bullet's framing stay within that scope, or does it import a mechanism the paper only references as background?

## Good Future-Chat Summary

If starting from a fresh chat, summarize the workflow like this:

> When the user asks for synthesis integration on a paper they have finished note-taking, read the paper's Zotero notes in `Literature Review/zotero_notes/` together with all synthesis notes in `Literature Review/Synthesis/`. Triage which synthesis notes the paper touches; for each touched note, decide whether the paper confirms, sharpens, qualifies, or adds material. Output a standalone HTML checklist in `/mnt/user-data/outputs/{citekey}-synthesis-checklist.html` — sticky progress bar, sections per touched note with PC/WT/SP/META checkbox items, callouts for WT and SP drafts, cross-cutting reminders with prioritization. Always include a META item to remove the paper from "To integrate once read" stubs and explicitly flag skipped synthesis notes. Use `STORAGE_KEY = '{citekey}-checklist-v1'`.

## Related Notes

- [[AGENTS]]
- [[THESIS_CONTEXT]]
- [[Literature Review/README]]
- [[Literature Review/Synthesis/README|Synthesis folder]]
- [[Literature Review/Overview Synthesis and Reading Map]]
- [[ai/zotero-import-template-guide]]
