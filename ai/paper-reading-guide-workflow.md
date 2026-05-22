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

Use this note when the user asks for a structured reading guide for a project-relevant paper. The output is a triage tool that helps them decide what to read closely, what to skim, and what to skip, grounded in the synthesis notes the paper will eventually feed. It is not a summary. A summary replaces the paper; this guide orients the user inside it.

## When This Workflow Triggers

Phrasings the user may use to invoke this:

- "Read paper X for my project."
- "Give me a reading guide for X."
- "Help me work through paper X."
- A paper PDF attached with framing along these lines.

If it is unclear whether the user wants this workflow, a full summary, a Zotero-note draft, or the synthesis-integration workflow, ask before producing anything. The synthesis-integration workflow ([[ai/synthesis-integration-workflow]]) runs *after* reading and note-taking; this one runs *before* reading.

## Required Context

The paper PDF is provided by the user in the message. Everything else lives in the Obsidian vault and should be pulled fresh via the Obsidian MCP when available. The user iterates on these files between sessions, so a snapshot from a prior chat or earlier attachment is unsafe to rely on. Do not ask the user to attach vault files when the MCP can retrieve them.

### How to pull (MCP, default path)

Use `obsidian_batch_get_file_contents` to fetch the always-pull set in one call. Pass the exact vault-relative paths listed below. Use `obsidian_get_file_contents` for a single conditional file. Use `obsidian_list_files_in_dir` only if you suspect a new file exists in `Literature Review/Synthesis/` or another structural folder that this workflow does not yet name.

If the MCP is unreachable or returns errors for required files, say so and stop. Ask the user to attach the missing files manually rather than producing the guide without them. Do not improvise around missing context.

### Always pull (vault-relative paths)

1. `AGENTS.md` - agent rules and completion checklist.
2. `PROJECT_CONTEXT.md` - current project framing.
3. `Project Overview.md` - current state map of the deliverables.
4. `Literature Review/Overview Synthesis and Reading Map.md` - reading plan, source priorities, and current cross-source synthesis. Without this, the guide reroutes the user through ground already covered and "Why this matters" collapses into generic relevance claims.
5. All synthesis notes in `Literature Review/Synthesis/`.
6. `Glossary.md` - stable term definitions. Match the glossary's framing rather than improvising definitions.

### Conditionally pull

7. Any optional project-specific structural or synthesis file if the paper touches territory covered by it. Examples: an argument-level synthesis, a theory note, a methods note, or a design-framework note. If you suspect such a note exists but do not know its path, list the relevant folder first and ask before pulling a candidate that may not matter.

### When to ask the user instead of pulling

Only three cases:

- The Obsidian MCP is unavailable for this session.
- A required file errors on retrieval and the cause is not a transient hiccup (try once more before reporting).
- You suspect a vault file you do not know about exists and would change the guide. In that case, list the directory first; if a candidate appears, name it to the user and ask whether to pull it.

Never ask the user to attach the always-pull set as a default. The MCP exists so the workflow does not bottleneck on their attention.

## Pre-Flight Check

Before producing the guide, confirm:

- The paper PDF was actually opened and read, not skimmed from the abstract.
- Always-pull set retrieved fresh this session, not relied on from prior context.
- Optional anchor notes pulled if the paper clearly touches their territory.
- Relevance verdict committed before producing the guide.
- For each section depth label, the rationale traces back to a specific synthesis note's needs, not generic interest.

## Relevance Check

Before producing the guide, commit to a relevance verdict for the paper. The verdict scales the rest of the output and forces honest calibration about how much attention this paper warrants. Producing a full guide for a paper that adds little, just because the reading map flagged it as worth reading, is the failure mode this check exists to catch.

The verdict is one of:

- **High** - the paper makes a substantive contribution to the project: a new mechanism, boundary condition, domain transfer, cross-paradigm test, structural framing the existing library does not cover, or strong counterweight to an established claim. Earns the full section-by-section guide.
- **Moderate** - meaningfully extends, qualifies, or replicates an existing claim in the synthesis without adding a new mechanism or framing. Earns a guide, but more sections are Skim/Skip and total length is shorter.
- **Light** - on-topic but adds little the existing library does not already have at equal or better quality. Earns a compressed artifact, not a section-by-section walk. The compressed artifact is honest about why the paper does not earn more attention.

Decide the verdict by holding the paper against the current state of the vault: `PROJECT_CONTEXT.md`, `Project Overview.md`, the current synthesis notes, and the cross-source synthesis section of the reading map. Ask: against this existing structure, what does the paper actually add? If the answer is "another instance of a point already made by existing sources," the verdict tends Light. If the answer names a specific mechanism, boundary condition, or framing the synthesis does not yet capture, the verdict tends High. Use judgment grounded in vault content; do not apply a fixed checklist.

The verdict is not "is this paper exactly on the project topic." Papers can be High-relevance because they provide contrast cases, methods, adoption evidence, problem-mechanism evidence, boundary conditions, or counterweights. The check is about how much the paper adds against what the user already has.

### When to flag-and-ask before producing the guide

If the paper appears in the reading map as a must-read, minimum viable source, or top-priority source but your verdict is Moderate or Light, surface the tension to the user before producing the guide. The reading map represents a prior judgment; downgrading that source warrants a check rather than silent execution. State the verdict, name the specific gap or redundancy that drove it, and ask whether to proceed at the lower weight or recalibrate.

If the paper is on the broader source list and your verdict is Light, no flag is needed. Produce the compressed artifact and let the verdict reasoning speak for itself.

## Output Format

The format scales with the relevance verdict. The High-verdict format is the canonical five-part structure below. Moderate and Light verdicts use compressed variants described at the end of this section.

Use H2 (`##`) for parts. The section-by-section reading guide uses H3 headers like `### sec. N Section Name - **Read closely**` per paper section.

### 1. Title block

A single H1 with the paper's short citation (`Author et al. (Year): "Short title"`). Nothing else here.

### 2. Overview (~150 words)

What the paper does and finds, in your own words. Lead with the headline finding, then add the structural complication. Mention methodology only if it shapes how the result should be read. This is what the user reads first to decide whether to keep going.

### 3. Why this paper matters for the project

Open with an explicit verdict line in this exact form: **`Relevance: High | Moderate | Light - [one-sentence reason grounded in vault content].`** The reason should name what the paper adds, or does not add, against the existing synthesis, not generic field relevance.

Then a short framing paragraph naming the synthesis notes the paper feeds, followed by a tight bulleted list (one bullet per relevant note) of the contribution it makes. Be specific. When naming adjacent already-read papers, use citekeys so the guide and the synthesis stay aligned on naming. If the paper has limitations or framings the user should be wary of, name them in a closing sentence or two.

If the paper genuinely feeds none of the synthesis notes, say so plainly. That is a useful triage signal, not a failure mode. It should propagate downstream into liberal Skim/Skip labels or a Light verdict that collapses the section-by-section walk entirely.

### 4. Section-by-section reading guide

Walk through the paper in order. For each section, use a header like `### sec. N Section Name - **Read closely**` or `Read selectively`, `Skim`, `Skip unless needed`.

The four reading-depth labels:

- **Read closely** - section contains the contribution, mechanism, theory move, or finding that maps directly to a synthesis note. The user should read every paragraph.
- **Read selectively** - the section has one or two extractable results buried in methodology or prose. Tell the user what to extract and where (table number, page, paragraph cue) so they can skip the rest.
- **Skim** - orienting or contextual material. The user should read at low resolution to maintain narrative flow but not engage deeply.
- **Skip unless needed** - appendices, robustness checks, related work, or implementation details that do not shift anything. Name them so the user knows they exist.

For sections marked "Read closely," pull out specific findings or table references. Be concrete. The user should be able to navigate to the exact place in the paper from your guide.

Calibration anchor by verdict:

- **High** verdict: in a typical 20-40 page empirical paper, expect 2-4 sections marked **Read closely**, 2-3 **Skim**, 1-3 **Skip unless needed**, and the remainder **Read selectively**.
- **Moderate** verdict: expect 1-2 **Read closely** at most; the rest tilts toward **Skim** and **Skip unless needed**. If more than two sections genuinely warrant Read closely on a Moderate-verdict paper, reconsider the verdict before reconsidering the section labels.
- **Light** verdict: this section collapses entirely. Use the Light-verdict format below.

If you find yourself recommending "Read closely" for most of the paper at any verdict, you have not done the triage work this guide exists for.

### 5. What to extract for synthesis notes

A bulleted list mapping the paper's contributions onto the specific synthesis notes they feed. One bullet per note, with the actual extractable claim. This is what the user will use when they open the synthesis notes after reading.

End with a short offer-line: "Want me to draft the Zotero-note bullets and the synthesis-note contributions once you've read it?"

### Compressed format for Moderate and Light verdicts

For **Moderate**-verdict papers, all five parts are produced, but length compresses: roughly 500-800 words, more sections marked Skim/Skip, and the extraction list usually covering one or two synthesis notes rather than many.

For **Light**-verdict papers, the section-by-section walk is dropped entirely. The artifact is:

1. Title block (H1 short citation).
2. Overview (about 100 words, can be shorter than the High default).
3. Why this paper matters - opens with the verdict line as specified above; the body is a short paragraph naming the at-most-one-or-two synthesis notes the paper touches lightly, or stating plainly that the paper does not earn synthesis-note integration.
4. **Read this much, then stop.** A short directive paragraph naming the abstract, one specific section if any, and any single table or finding worth registering. Close with an explicit sentence that a section-by-section walk is not worth the user's time on this paper.

Total Light-verdict artifact: roughly 200-400 words. The compressed format is honest scaffolding: it tells the user where the paper sits and why it does not earn more attention.

## Style and Tone

- Write to the user in second person where natural. Not third-person ("the reader") - this is a working document, not a publication.
- Honest assessment over diplomatic hedging. If the paper's framing is loose, name it. If a finding is over-claimed, say so. Preserve tensions and risks rather than smoothing them over.
- No bullet-point lists where prose works. The reading-depth headers are structural; everything else should be prose unless a compact list is clearer.
- Cite paper sections, tables, and figures by the labels used in the paper. Do not paraphrase what the paper already labels clearly.
- Avoid "the authors find" / "the paper argues" filler. Say what they found or argued.
- One quote per paper, under 15 words, only when exact phrasing matters. Default to paraphrase.
- When naming other vault papers, use citekeys so the guide aligns with the synthesis notes' naming convention.
- Length anchor by verdict: High -> 800-1200 words for a 20-40 page paper; Moderate -> 500-800 words; Light -> 200-400 words. Scale sub-linearly for longer papers within each verdict band.

## What Not To Do

- **Don't summarize the paper.** The guide replaces a triage decision, not the reading itself.
- **Don't be exhaustive.** A 90-page paper still gets a reading guide that fits on a screen or two.
- **Don't ignore the synthesis notes.** Generic "this paper is about X" framing is failure mode #1. The guide is valuable precisely because it routes the paper through the user's existing argument structure.
- **Don't recommend "Read closely" for everything.** That defeats the purpose. Most papers have only a few sections that genuinely matter and the rest is supporting infrastructure.
- **Don't propose a Zotero note or synthesis-note rewrite as part of the guide.** Those are separate workflows. Offer them at the end as a follow-up.
- **Don't fabricate adjacent-paper comparisons.** If the guide says "sits next to [Paper Y]", confirm from the reading map and synthesis bullets that the comparison actually holds. If you do not have the prior paper's content, name the connection more cautiously or drop it.
- **Don't archive the guide to the vault** unless the user explicitly asks. The Zotero notes and synthesis additions are the durable record; the guide is scaffolding.
- **Don't anchor on the reading map's framing of why a paper is important.** The reading map names what to read; the relevance verdict decides how much weight to give it once read. These are different judgments.

## Calibration Examples

A "Read closely" tag is appropriate when:

- The section reports the central finding the paper will be cited for.
- The section introduces a theoretical move the user's framework can borrow, such as a decomposition, typology, or mechanism.
- The section contains a result that directly maps onto a tension in a synthesis note.

A "Skim" tag is appropriate when:

- It is a literature review summarizing work the user already knows from the reading map.
- It is methodology that does not shape interpretation.
- It is a discussion section that mostly restates earlier findings.

A "Skip unless needed" tag is appropriate when:

- It is an appendix of robustness checks confirming the main result.
- It is a coding-scheme description that the user only needs if they are writing methods.
- It is a related-work section with no new sources the user has not already mapped.

## Good Future-Chat Summary

If starting from a fresh chat, summarize the workflow like this:

> When the user asks for a reading guide on a paper PDF, fetch the vault context fresh via the Obsidian MCP; do not ask them to attach files unless the MCP is unavailable or a required read fails. Use `obsidian_batch_get_file_contents` for the always-pull set: `PROJECT_CONTEXT.md`, `Project Overview.md`, `Literature Review/Overview Synthesis and Reading Map.md`, the synthesis notes in `Literature Review/Synthesis/`, and `Glossary.md`. Pull optional anchor notes if the paper clearly touches their territory. Read the PDF. Commit a relevance verdict (High / Moderate / Light) by holding the paper against the current synthesis state. If a must-read or top-priority paper is downgraded to Moderate or Light, flag-and-ask before producing the guide. Produce inline markdown: High verdict -> full five-part guide; Moderate -> compressed five-part guide; Light -> title + overview + verdict + "read this much, then stop." Do not archive. Offer to draft Zotero bullets and synthesis contributions as a follow-up.

## Related Notes

- [[AGENTS]]
- [[PROJECT_CONTEXT]]
- [[Project Overview]]
- [[Literature Review/README]]
- [[Literature Review/Synthesis/README|Synthesis folder]]
- [[Literature Review/Overview Synthesis and Reading Map]]
- [[ai/synthesis-integration-workflow]]
- [[ai/zotero-import-template-guide]]
- [[Glossary]]
