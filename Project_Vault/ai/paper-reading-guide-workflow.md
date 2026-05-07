---
title: Paper Reading Guide Workflow
tags:
  - ai
  - reading
  - workflow
  - handoff
status: active
---

# Paper Reading Guide Workflow

Use this note when the user asks for a structured reading guide for a project-relevant paper. The output is a triage tool that lets them decide what to read closely, what to skim, and what to skip — grounded in the synthesis notes the paper will eventually feed. It is not a summary. A summary replaces the paper; this guide orients them inside it.

## When This Workflow Triggers

Phrasings the user uses to invoke this:

- "Read paper X for my project."
- "Give me a reading guide for X."
- "Help me work through paper X."
- A paper PDF attached with framing along these lines.

If it is unclear whether the user wants this workflow vs. a full summary vs. a Zotero-note draft vs. the synthesis-integration workflow, ask before producing anything. The synthesis-integration workflow ([[ai/synthesis-integration-workflow]]) runs *after* reading and note-taking; this one runs *before* reading.

## Required Context

The paper PDF is always provided by the user in the message. Everything else lives in the obsidian vault and **must be pulled fresh via the obsidian MCP** — the user iterates on these files between sessions, so a snapshot from a prior chat or an earlier attachment is unsafe to rely on. Do not ask the user to attach vault files; pull them yourself.

### How to pull (MCP, default path)

Use `obsidian_batch_get_file_contents` to fetch the always-pull set in one call. Pass the exact vault-relative paths listed below — they are the canonical paths and should be used verbatim. Use `obsidian_get_file_contents` for a single conditional file. Use `obsidian_list_files_in_dir` only if you suspect a new file exists in `Literature Review/Synthesis/` or other structural folders that this workflow doesn't yet name (i.e. the vault has gained a draft you should know about).

If the MCP is unreachable or returns errors for required files, say so and stop — ask the user to attach the missing files manually rather than producing the guide without them. Do not improvise around missing context.

### Always pull (vault-relative paths, use verbatim)

1. `AGENTS.md` — already in context if the vault is connected; pull explicitly if it isn't.
2. `THESIS_CONTEXT.md` — current project framing.
3. `Thesis Overview.md` — current state map of the deliverables.
4. `Literature Review/Overview Synthesis and Reading Map.md` — reading plan, source priorities, and the current cross-source synthesis. Without this, the guide reroutes the user through ground already covered and "Why this matters" collapses into generic relevance claims.
5. All synthesis notes in `Literature Review/Synthesis/`
6. `Glossary.md` — stable term definitions. Match the glossary's framing rather than improvising definitions.

### Conditionally pull

7. Any specific structural or synthesis files if the paper touches territory relevant to them.

### When to ask the user instead of pulling

Only three cases:

- The obsidian MCP is unavailable for this session.
- A required file errors on retrieval and the cause isn't a transient hiccup (try once more before reporting).
- You suspect a vault file you don't know about exists and would change the guide. In that case, list the directory first; if a candidate appears, name it to the user and ask whether to pull it.

Never ask the user to attach the always-pull set as a default. The MCP is there precisely so the workflow doesn't bottleneck on their attention.

## Pre-Flight Check

Before producing the guide, confirm:

- The paper PDF was actually opened and read, not skimmed from the abstract.
- Always-pull set retrieved fresh via `obsidian_batch_get_file_contents` this session — not relied on from prior context.
- Argumentation/Problem note pulled via `obsidian_get_file_contents` if the paper is problem-side.
- For each section depth label, the rationale traces back to a specific synt hesis note's needs, not generic interest.

## Output Format

Ä_'
Five parts, in this order. Use H2 (`##`) for parts; the section-by-section reading guide uses H3 (`### §N Section Name — **Read closely**`) per paper section.

### 1. Title block
A single H1 with the paper's short citation (`Author et al. (Year): "Short title"`). Nothing else here.

### 2. Overview (~150 words)
What the paper does and finds, in your own words. Lead with the headline finding, then add the structural complication. Mention methodology only if it shapes how the result should be read. This is what the user reads first to decide whether to keep going.

### 3. Why this paper matters for the project
A short framing paragraph naming the synthesis notes the paper feeds, then a tight bulleted list (one bullet per relevant note) of the contribution it makes. Be specific. When naming adjacent already-read papers, use citekeys (the convention used across the synthesis notes) so the guide and the synthesis stay aligned on naming. If the paper has limitations or framings the user should be wary of, name them in a closing sentence or two.

If the paper genuinely feeds none of the synthesis notes, say so plainly here. That is a useful triage signal, not a failure mode — and it should propagate downstream into the section-by-section guide as liberal "Skim" / "Skip" labels.

### 4. Section-by-section reading guide
Walk through the paper in order. For each section give a header like `### §N Section Name — **Read closely**` (or `Skim`, `Read selectively`, `Skip unless needed`). The four reading-depth labels:

- **Read closely** — section contains the contribution, the mechanism, or a finding that maps directly to a synthesis note. The user should read every paragraph.
- **Read selectively** — the section has one or two extractable results buried in methodology or prose. Tell the user what to extract and where (table number, page, paragraph cue) so they can skip the rest.
- **Skim** — orienting/contextual material. The user should read at low resolution to maintain narrative flow but not engage.
- **Skip unless needed** — appendices, robustness checks, related work that doesn't shift anything. Name them so the user knows they exist; don't pretend they're not in the paper.

For sections marked "Read closely," pull out specific findings or table references. Be concrete. The user should be able to navigate to the exact place in the paper from your guide.

Calibration anchor: in a typical 20–40 page empirical paper, expect 2–4 sections marked **Read closely**, 2–3 **Skim**, 1–3 **Skip unless needed**, and the remainder **Read selectively**. If you find yourself recommending "Read closely" for most of the paper, you have not done the triage work this guide exists for.

### 5. What to extract for synthesis notes
A bulleted list mapping the paper's contributions onto the specific synthesis notes they feed. One bullet per note, with the actual extractable claim. This is what the user will use when they open the synthesis notes after reading.

End with a short offer-line: "Want me to draft the Zotero-note bullets and the synthesis-note contributions once you've read it?"

## Style and Tone

- Write to the user, in second person where natural. Not third-person ("the reader") — this is a working document, not a publication.
- Honest assessment over diplomatic hedging. If the paper's framing is loose, name it. If a finding is over-claimed, say so. The user explicitly wants tensions and risks preserved, not smoothed over.
- No bullet-point lists where prose works. The reading-depth headers are structural; everything else should be prose.
- Cite paper sections by `§N` and tables/figures by number. Don't paraphrase what the paper already labels clearly.
- Avoid "the authors find" / "the paper argues" filler — say what they found.
- One quote per paper, under 15 words, only when the exact phrasing matters. Default to paraphrase. (Standing copyright constraint, applies here as everywhere.)
- When naming other vault papers, use citekeys so the guide aligns with the synthesis notes' naming convention.
- Length anchor: a 20–40 page paper gets a guide of roughly 800–1200 words. Scale sub-linearly for longer papers.

## What Not To Do

- **Don't summarize the paper.** The guide replaces a triage decision, not the reading itself.
- **Don't be exhaustive.** A 90-page paper still gets a reading guide that fits on a screen or two.
- **Don't ignore the synthesis notes.** Generic "this paper is about X" framing is failure mode #1. The guide is *valuable* precisely because it routes the paper through the user's existing argument structure.
- **Don't recommend "Read closely" for everything.** That defeats the purpose. Most papers have 2–4 sections that genuinely matter and the rest is supporting infrastructure. Be willing to label things "Skim" or "Skip."
- **Don't propose a Zotero note or a synthesis-note rewrite as part of the guide.** Those are separate workflows. Offer them at the end as a follow-up.
- **Don't fabricate adjacent-paper comparisons.** If the guide says "sits next to [Paper Y]", confirm from the reading map and the synthesis bullets that the comparison actually holds. If you don't have the prior paper's content, name the connection more cautiously or drop it.
- **Don't archive the guide to the vault** unless the user explicitly asks. The Zotero notes and synthesis additions are the durable record; the guide is scaffolding.

## Calibration Examples

A "Read closely" tag is appropriate when:

- The section reports the central finding the paper will be cited for.
- The section introduces a theoretical move the user's framework can borrow (e.g. a decomposition, a typology, a mechanism).
- The section contains a result that directly maps onto a tension in a synthesis note.

A "Skim" tag is appropriate when:

- It's a literature review summarizing work the user already knows from the reading map.
- It's methodology that doesn't shape interpretation.
- It's a discussion section that mostly restates earlier findings.

A "Skip unless needed" tag is appropriate when:

- It's an appendix of robustness checks confirming the main result.
- It's a coding-scheme description that the user only needs if they are writing methodology.
- It's a related-work section with no new sources the user hasn't already mapped.

## Good Future-Chat Summary

If starting from a fresh chat, summarize the workflow like this:

> When the user asks for a reading guide on a paper PDF, fetch the vault context fresh via the obsidian MCP — don't ask them to attach files. Use `obsidian_batch_get_file_contents` for the always-pull set: `THESIS_CONTEXT.md`, `Thesis Overview.md`, `Literature Review/Overview Synthesis and Reading Map.md`, the synthesis notes in `Literature Review/Synthesis/`, and `Glossary.md`. Read the PDF. Produce inline markdown with five parts: title block (H1), Overview (~150 words leading with headline finding then complication), Why this paper matters for the project (with citekey-based references to adjacent papers), Section-by-section reading guide using **Read closely** / **Read selectively** / **Skim** / **Skip unless needed** depth labels at H3, and What to extract for synthesis notes mapping contributions to specific notes. Don't archive. Offer to draft Zotero bullets and synthesis contributions as a follow-up. If the MCP is unavailable, say so and ask the user to attach the missing files; don't improvise around missing context.

## Related Notes

- [[AGENTS]]
- [[THESIS_CONTEXT]]
- [[Thesis Overview]]
- [[Literature Review/README]]
- [[Literature Review/Synthesis/README|Synthesis folder]]
- [[Literature Review/Overview Synthesis and Reading Map]]
- [[ai/synthesis-integration-workflow]]
- [[ai/zotero-import-template-guide]]
- [[Glossary]]
