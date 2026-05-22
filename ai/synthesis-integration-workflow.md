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

Use this note in future AI chats when the user asks for the "integration step", "synthesis additions", or "important points to integrate" for a paper they have finished reading and note-taking on.

## When This Workflow Triggers

Phrasings the user may use to invoke this:

- "Now perform the integration step."
- "Generate the important points for my synthesis."
- "Integrate this paper into my synthesis."
- "What should I add to the synthesis notes from this paper?"

Trigger only when the user has confirmed their Zotero notes are complete. If the user has just finished reading the paper but has not yet captured reactions in the Zotero note, ask whether they want to do the note-taking pass first.

## Required Context (read in this order)

Always read fresh. The user iterates on these files between conversations.

1. `AGENTS.md` - agent rules and completion checklist.
2. `PROJECT_CONTEXT.md` - current project framing.
3. `Project Overview.md` - current state map of the project deliverables.
4. `Literature Review/Overview Synthesis and Reading Map.md` - reading plan, source priorities, and current cross-source synthesis.
5. The paper's Zotero notes file: `Literature Review/zotero_notes/{citekey}-zotero-notes.md`.
   - Filenames are citekey-based and should follow the stable pattern `{citekey}-zotero-notes.md`.
   - **This file is the primary input.** It contains the user's reactions, reading-time judgments, and cross-paper connections that the synthesis additions must respect.
6. All synthesis notes in `Literature Review/Synthesis/`.
7. `Glossary.md` - stable term definitions; do not redefine terms here.
8. Any optional project-specific anchor note if the paper touches a topic covered by one. Examples: an argument-level synthesis, a theory note, a methods note, or a design-framework note. Pull these only when the current vault actually contains them and they are relevant.
9. The paper's main note in `Literature Review/imports/{citekey}.md` or under `Literature Review/Papers/` if it exists.
10. The synthesis checklist template at `ai/templates/synthesis-checklist-template.html` - use this as the base for the output.

Use `obsidian_batch_get_file_contents` for efficiency if you are connected via MCP. Otherwise use the best available read method and stop if required context is unavailable.

## Process

### Step 0 - Relevance Check

Before triaging which synthesis notes the paper touches, commit to a relevance verdict that scales the rest of the integration. This is the guardrail against producing heavy multi-note integration for a paper whose actual contribution is one bullet's worth, and against silently downgrading a paper the reading map flagged as central. The verdict goes visibly into the checklist artifact.

The verdict is one of:

- **High** - substantive new contribution to the project: a new mechanism, boundary condition, domain transfer, cross-paradigm test, structural framing, or strong counterweight that the existing library does not already provide. Standard Step 1-4 process applies and the full checklist follows.
- **Moderate** - meaningfully extends, qualifies, or replicates an existing claim without adding a new mechanism or framing. Integrate to one or two best-fitting notes; PC bullets and at most one WT update; no SP drafts unless the paper is the third or later converging source on a claim already pending; do not seed empty WTs unless the paper is a natural anchor.
- **Light** - on-topic but adds little the existing library does not already have at equal or better quality. One PC bullet in the single best-fitting note. No WT updates, no SP drafts, no seeding of empty WTs. The checklist artifact is still produced so the verdict, cleanup task, and skip reasoning are recorded, but the body is small.

Decide the verdict by holding the paper against the current state of the vault: `PROJECT_CONTEXT.md`, `Project Overview.md`, the synthesis notes, and the cross-source synthesis in the reading map. Ask: against this existing structure, what does the paper actually add? Use judgment grounded in vault content; do not apply a fixed checklist.

The verdict is not "is this paper exactly on the project topic." Papers can be High-relevance because they provide contrast cases, methods, adoption evidence, problem-mechanism evidence, boundary conditions, or counterweights. The check is about how much the paper adds against what the user already has.

#### When to flag-and-ask before producing the checklist

If the paper appears in the reading map as a must-read, minimum viable source, or top-priority source but your verdict is Moderate or Light, surface the tension to the user before producing the checklist. The reading map represents a prior judgment; downgrading that source warrants a check rather than silent execution. State the verdict, name the specific gap or redundancy that drove it, and ask whether to proceed at the lower weight or recalibrate.

If the paper is on the broader source list and your verdict is Light, no flag is needed. Produce the compressed checklist and let the verdict reasoning speak for itself.

### Step 1 - Triage

For each synthesis note in `Literature Review/Synthesis/`, classify the paper's contribution under the verdict ceiling. A Light-verdict paper cannot have a Heavy contribution to any single note; a Moderate-verdict paper rarely has more than one Heavy or two Medium notes.

- **Heavy** - substantive new material across multiple aspects of the note. Only available at High verdict.
- **Medium** - meaningful contribution to one or two aspects. Available at High and Moderate verdicts.
- **Light** - one bullet's worth, possibly interpretive. Available at any verdict; the default for Light-verdict papers.
- **Skip** - paper does not substantively touch the note.

Skipped notes do not get their own section in the output. They are flagged in the cross-cutting reminders so the user knows the skip was deliberate, not an oversight.

If the verdict-to-triage mapping feels wrong, re-examine the verdict before forcing the triage. For example, a paper with Heavy material for one note probably should not remain Moderate; a paper with only one Light contribution probably should not remain High.

### Step 2 - Identify the contribution type per touched note

For each touched note, determine whether the paper:

- **Confirms existing claims** -> PC bullets; SP candidate if multiple papers now agree.
- **Sharpens existing claims** -> PC bullets plus WT update.
- **Qualifies existing claims** -> PC bullets plus WT update with explicit caveats.
- **Adds new material** -> PC bullets plus WT seed if the note's WT is currently empty, or WT addendum if it already exists.

WT updates and SP drafts are gated by the verdict. Light-verdict papers do not produce WT updates or SP drafts, regardless of contribution type per note.

### Step 3 - Watch for cross-paper signals

These belong in cross-cutting reminders, not in any single synthesis note:

- Disagreements with other papers, especially papers on the user's reading list.
- Future-reading pointers: papers cited by this paper that are not yet on the reading list.
- Methodological caveats that constrain how the paper can be cited.
- Cross-references to optional project-specific anchor notes where the paper bears on them.

### Step 4 - Decide on Synthesized Position drafts

Draft SP prose only when **three or more papers converge** on a claim and the verdict is High or Moderate. Below either threshold, propose SP candidate items as one-line pointers without drafted prose. Light-verdict papers do not produce SP drafts.

When drafting, mark explicitly as "first draft." Provide the draft as a purple `.callout.sp` block immediately followed by an SP-tagged checkbox saying "Promote the SP draft above into the Synthesized Position section."

## Output Format

Create a standalone HTML file in the vault at `ai/outputs/{citekey}-synthesis-checklist.html`. From the repository root, this is `Project_Vault/ai/outputs/{citekey}-synthesis-checklist.html`. Create `ai/outputs/` if it does not exist. Do not use external artifact paths or presentation helpers; those are not part of this vault workflow.

The file must use the reference template for its base structure, styling, and functionality. Copy the HTML structure, CSS, JavaScript, callout patterns, and section structure from `ai/templates/synthesis-checklist-template.html`, then fill in the paper-specific content.

### Mandatory structural elements

- Sticky progress bar at the top with counter and section-level counts.
- **Verdict block directly under the title block.** Displays the relevance verdict (High / Moderate / Light) and a one-to-two-sentence reason grounded in vault content. The verdict block is visible without scrolling. Color-code subtly: High green, Moderate amber, Light gray.
- Sections per touched synthesis note in the priority order from the cross-cutting reminders.
- Each item is a checkbox with a zone tag (PC, WT, SP, META).
- Callouts for WT seeds/updates (orange, `.callout`) and SP drafts (purple, `.callout.sp`), only when permitted by the verdict.
- Cross-cutting reminders section at the bottom with META items and a numbered prioritization list.
- Reset button.
- `localStorage` persistence with `STORAGE_KEY = '{citekey}-checklist-v1'`. This must be unique per paper so checklists do not collide.

### Tag conventions

- **PC** (green) - Paper Contributions: short pointer bullet matching the existing synthesis-note bullet style.
- **WT** (orange) - Working Thoughts: prose in the user's voice.
- **SP** (purple) - Synthesized Position candidate.
- **META** (gray) - action on structure, links, cleanup, or caveats.

### PC bullet style

- Bold lead phrase identifying the key finding or concept.
- One to two sentences of explanation.
- Page references where relevant (`p42`, `sec. 3.2.3`, `Table 2`).
- Use citekeys when referring to other papers.
- Compressed: do not duplicate Zotero-note quotations. The synthesis layer is for cross-paper argument; Zotero already holds paper-level depth.
- Match the bullet style in the existing synthesis notes.

### WT prose style

- User's voice: direct, analytical, no padding.
- No conversational hedging ("might be worth", "perhaps consider").
- Frame as either "Append to your existing WT" (update) or "Add as initial WT entry" (seed).
- Acknowledge interpretive vs. direct contributions explicitly.
- Flag ambiguities rather than resolving them.
- Preserve numerical findings (effect sizes, percentages, p-values) and page references.

### Mandatory items in every checklist

- A META item to remove the paper's stub from any affected note's "To integrate once read" section, if such a stub exists.
- A META item in cross-cutting reminders explicitly flagging skipped synthesis notes with the reason for skipping.
- A META item in cross-cutting reminders saying "Do not duplicate the Zotero note."

### Priority ordering in cross-cutting reminders

- List touched notes in suggested integration order.
- Most-loaded note first, where the work pays off most.
- Lightest or most interpretive last.
- Skipped notes do not appear in the priority list.

### Light-verdict checklist body

A Light-verdict checklist is honest scaffolding: it tells the user where the paper sits and why it does not earn more integration work.

- Verdict block visible at top with reasoning.
- One section for the single best-fitting note, containing one PC checkbox and any necessary META cleanup.
- Cross-cutting reminders include the explicit reasoning for the Light verdict, the list of other notes that were considered and skipped, and the standard "do not duplicate Zotero" / "remove from To integrate once read" META items.
- No WT callouts, no SP callouts, no flag-and-ask language inside the checklist body.

## Style Guidelines

- Direct and analytical; avoid conversational softening.
- Do not write more than the source supports. Distinguish empirical findings from interpretive contributions.
- When the paper qualifies a previous claim, surface the qualification in WT, not just in PC bullets.
- When the paper is silent on a synthesis dimension that prior papers covered, do not invent material.

## Anti-Patterns To Avoid

- Producing inline integration prose in the chat instead of an HTML checklist artifact when the user requested this workflow.
- PC bullets that duplicate Zotero-note quotations verbatim.
- Overlong PC bullets (more than about three sentences).
- Missing the "remove from To integrate once read" META cleanup.
- Forcing content into synthesis notes the paper does not touch.
- SP draft prose for claims with only one or two backing papers.
- WT updates or SP drafts for Light-verdict papers.
- Conversational tone instead of analytical register.
- Skipping the cross-cutting reminders section.
- Failing to set a unique `STORAGE_KEY`, causing localStorage collisions across papers.
- Conflating what the paper actually measured or manipulated with a higher-level mechanism it only mentions as background.
- Producing a Heavy or full-checklist integration for a paper that only earns a Moderate or Light verdict because the reading map listed it as worth reading.
- Silently downgrading a must-read or top-priority paper without raising the tension with the user first.

## Pre-Flight Check

Before producing the checklist, confirm:

- Paper's Zotero notes have been read fresh.
- All synthesis notes have been read fresh.
- `PROJECT_CONTEXT.md`, `Project Overview.md`, and the reading map have been read.
- Optional anchor notes were pulled if the paper clearly touches their territory.
- Relevance verdict committed before starting triage.
- Verdict-to-triage consistency: if the paper has Heavy material for any note, verdict should not be Light; if it has Medium material for multiple notes, verdict probably should not be Light.
- For each PC bullet, confirm: what variable, method, theory, or object did the paper actually manipulate, measure, analyze, or argue? Does the bullet stay within that scope?

## Good Future-Chat Summary

If starting from a fresh chat, summarize the workflow like this:

> When the user asks for synthesis integration on a paper they have finished note-taking, read the paper's Zotero notes in `Literature Review/zotero_notes/` together with all synthesis notes in `Literature Review/Synthesis/`, the current project context, the project overview, the reading map, the glossary, and any relevant optional anchor notes. First commit a relevance verdict (High / Moderate / Light) by holding the paper against the current synthesis state. If a must-read or top-priority paper is downgraded to Moderate or Light, flag-and-ask before producing the checklist. Then triage which synthesis notes the paper touches under the verdict ceiling, decide whether the paper confirms, sharpens, qualifies, or adds material, and output a standalone HTML checklist at `ai/outputs/{citekey}-synthesis-checklist.html` using `ai/templates/synthesis-checklist-template.html` as the base. Include a verdict block under the title, PC/WT/SP/META checkbox items where warranted, cross-cutting reminders, skipped-note reasoning, cleanup tasks, and a unique `STORAGE_KEY = '{citekey}-checklist-v1'`.

## Related Notes

- [[AGENTS]]
- [[PROJECT_CONTEXT]]
- [[Literature Review/README]]
- [[Literature Review/Synthesis/README|Synthesis folder]]
- [[Literature Review/Overview Synthesis and Reading Map]]
- [[ai/zotero-import-template-guide]]
