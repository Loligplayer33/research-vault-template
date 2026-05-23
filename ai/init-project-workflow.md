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

This workflow is also the canonical installation runbook. Given this file and the vault context, an agent should be able to walk a user through the complete setup: Zotero, Better BibTeX, Obsidian, Zotero Integration, Local REST API, MCP access, vault personalization, and validation.

## Agent-Facing Contract

This file is written for the agent, not as a user-facing checklist. Do not dump the whole file into the chat. Translate each phase into a small set of concrete instructions, wait for confirmation, then continue.

Success means:

- The user received the level of orientation they asked for: introduction only, full installation/personalization, or both.
- The Git remote was checked so normal users do not accidentally track project work against the upstream template repository.
- The user has Zotero, Better BibTeX, Obsidian, Zotero Integration, Local REST API, and an MCP path configured or clearly marked as a follow-up.
- The agent can read the vault through MCP, or the setup state clearly says MCP is still pending.
- Zotero Integration can create both the main paper note and raw Zotero note with citekey-based paths.
- If the user requested personalization, the vault context files reflect the user's project rather than generic placeholders, or the setup state clearly says file updates are pending until an agent with file access continues.
- If the user requested literature setup, the literature review has an initial guiding question, synthesis themes, and reading map, or the setup state clearly says those file updates are pending until an agent with file access continues.
- Future agents can start from `AGENTS.md`, the current project context file, the current project overview file, `Literature Review/README.md`, and `ai/README.md` without re-interviewing the user.

## Execution Rules for the Agent

1. **One step at a time:** Ask one question or one small set of tightly related questions, wait for the user's response, execute the file changes for that step, and then move to the next step. Maintain the current phase pointer. If the user says to continue, resume where the conversation left off unless they clearly ask to skip ahead.
2. **Persistent State Tracking:** Track setup state from the start, but adapt to the access available. If the agent has local file access or working MCP access, create `ai/INIT_STATE.md` as the durable checklist and update it after each phase. If the agent does not yet have file access because MCP is not configured, keep the same checklist in the chat and tell the user it will be written to `ai/INIT_STATE.md` as soon as file access is available. Delete the file only after the user confirms setup is complete.
3. **Continuous Validation:** When the agent has local file access or working MCP file access, run `python3 ai/scripts/validate_ai_docs.py` after modifying structural files, workflow docs, paths, or naming conventions. Do not move to the next phase until the script passes. If the agent does not yet have file access, clearly mark validation as pending in the chat-backed checklist and run it as soon as file access becomes available.
4. **Update Python Scripts if Renaming:** If the user chooses to rename foundational files like the project context note or project overview note, you MUST update the hardcoded paths in `ai/scripts/validate_ai_docs.py` to match the new names.
5. **No Secret Capture:** Never ask the user to paste long-lived API keys into vault notes. It is okay to ask whether they configured a key, but secrets belong in their MCP client config or local plugin config, not shared documentation.
6. **Manual-App Boundary:** Some installation steps happen in Zotero, Obsidian, or the user's MCP client and cannot be performed by the agent. Guide the user precisely, then ask them to confirm the result before continuing.
7. **Template Hygiene:** Keep the template project-neutral. Do not introduce thesis-specific themes, source lists, author examples, supervisor details, private paths, or personal names.
8. **Path Convention:** Unless this workflow says otherwise, paths are vault-relative from the repository root. Run validation from the root with `python3 ai/scripts/validate_ai_docs.py`.
9. **Adaptive Conversation:** At the beginning, ask whether the user wants a vault introduction, the full installation/personalization process, or both. Follow that choice. Do not force installation questions on a user who only asked for orientation.
10. **File-Access Gate:** Any step that creates, edits, renames, deletes, validates, or inspects vault files requires local file access or working MCP file access. If neither exists, collect the user's answers, keep a chat-backed checklist, mark the file work as pending, and stop before claiming that phase is complete.
11. **Silent Feedback Capture:** If the user says "note for later" or "do not respond to this", record the feedback in `ai/INIT_STATE.md` or [[ai/init-project-feedback]] when file access exists, then continue without summarizing the note back.
12. **No Invented Project Content:** Examples are allowed as examples only. Never write invented project details, deliverables, source lists, or claims into project files. If the user asks for help answering, offer sample formulations and wait for the user's chosen wording.
13. **Developer/Test Mode:** If the user is testing the template as a developer, explicitly mark this in `ai/INIT_STATE.md`. In developer mode, wrong-vault MCP, retained test imports, retained `ai/INIT_STATE.md`, or deferred Phase 7 cleanup can be valid if clearly recorded.
14. **Repository Ownership Check:** For normal users, run `python3 ai/scripts/check_template_remote.py` before personalization. If it says `origin` still points to `Loligplayer33/research-vault-template`, guide the user to create their own repository or use GitHub's "Use this template" flow before continuing with project-specific edits. Developers intentionally editing the template may continue in developer/test mode.

---

## Phase 0: Mode Selection & Workspace Orientation

**Goal:** Before anything else, make sure this vault belongs to the user's own repository, then decide the conversation path and confirm the correct folder.

### 0A. Repository Ownership Check

This check happens at the very start, before orientation or personalization.

If the agent has local file access, run:

```bash
python3 ai/scripts/check_template_remote.py
```

Handle the result:

- **Pass:** Continue setup. Mark `Git remote status: own project remote`.
- **No Git repository or no origin:** Guide the user to create their own repository and connect it before project-specific setup. Do not personalize files until they confirm this is intentional.
- **Origin points to `Loligplayer33/research-vault-template`:** Stop normal setup. Tell the user they are still connected to the upstream template repository. Guide them to either use GitHub's **Use this template** button or replace `origin` with their own repository URL.
- **Template developer:** If the user explicitly says they are the template developer and intend to edit the template repository, mark `Mode: developer-test` and continue.

If the agent has no local file access, ask the user to run the command locally or check `git remote -v` before continuing.

### 0B. Mode Selection & Workspace Orientation

Ask the user:
1. Do you want an explanation of how this vault works before we begin setup?
2. Are we setting up a fresh copy of this template, or updating an already initialized project?
3. Are you opening this repository directory as your Obsidian vault?

Explain:
- This repository root IS the Obsidian vault. Open this folder directly in Obsidian.
- The agent may edit template/project files, but external app setup in Zotero, Obsidian, and the MCP client requires user confirmation.
- Strong recommendation: for first-time setup, use an agent with local file access to this repository, for example Cursor opened at the repository root or Claude Code/Cowork opened with this repository as its working folder. Before MCP exists, an MCP-only agent may not be able to create `ai/INIT_STATE.md`, edit vault files, rename notes, create synthesis notes, update workflow docs, delete setup state, or run validation. It can still give an introduction and installation guidance, but full setup is smoother and safer with local file access.

Branching rule:
- If the user wants an explanation, run the Vault Introduction Track below **step by step**, then continue to Phase 1.
- If the user does not want an explanation, skip to Phase 1.

**Execution:**
- Start state tracking with the checklist below.
- If the agent has file access, create `ai/INIT_STATE.md` now.
- If the agent does not have file access yet, keep this checklist in the conversation and mark `State file: pending until MCP or local file access is available`.
- As soon as file access becomes available, write the current checklist state to `ai/INIT_STATE.md`.

```markdown
# Initialization State

- [ ] Phase 0: Mode selection and workspace orientation
- [ ] Vault introduction track: pending / skipped / complete
- [ ] Phase 1: Local app installation
- [ ] Phase 2: MCP setup and verification
- [ ] Phase 3: Zotero import pipeline verification
- [ ] Workspace orientation: pending / skipped / complete
- [ ] Phase 4: Core project details
- [ ] Phase 5: Literature review and synthesis setup
- [ ] Phase 6: Workflow calibration
- [ ] Phase 7: Agent context finalization & Cleanup

## Setup Notes

- MCP status: pending
- Zotero import test: pending
- Validation status: pending until file access is available
- File update status: active / pending until file access is available
- File renames: none
- Manual follow-ups: none
- State file: active / pending until file access is available
- Mode: normal / developer-test
- Current phase pointer: Phase 0
- Deferred cleanup: none
- Git remote status: pending
```

- If file access exists, run `python3 ai/scripts/validate_ai_docs.py` and fix any template health issue before continuing.
- If file access does not exist, mark `Validation status: pending until file access is available` and postpone validation until MCP or local file access is available.
- Update `ai/INIT_STATE.md` if it exists; otherwise update the chat-backed checklist.

---

## Vault Introduction Track

**Goal:** Give the user a practical mental model of the vault before setup or research work begins.

Run this track if the user wanted an explanation. **Crucial Rule:** Do NOT dump all these points into a single message. Explain **one section at a time**, ask if it makes sense or if they have questions, wait for their reply, and then move to the next section.

### What to explain

#### 1. The vault structure

- The repository root IS the Obsidian vault. Open this folder directly in Obsidian.
- **The context files agents read first**:
  - `AGENTS.md` - canonical agent rules, project summary, and conventions.
  - `CLAUDE.md` - symlink to `AGENTS.md`.
  - the project context note - project framing, deliverables, import logic, and workflow assumptions.
  - the project overview note - one-page current-state map: what the project is, what is done, what is open, and what to do next.
  - `Glossary.md` - stable definitions, acronyms, contested terms, and open conceptual questions. This file starts empty and grows organically during research; setup should not populate it.

#### 2. The literature review folder

- `Literature Review/README.md` - the main workflow guide for reading, importing, and synthesizing papers.
- `Literature Review/Overview Synthesis and Reading Map.md` - the canonical reading plan, source priorities, current phases, and cross-source orientation.
- `Literature Review/Synthesis/` - thematic synthesis notes where cross-paper argument develops.
  - Each synthesis note should contain `Current Argument`, `Working Thoughts`, `Synthesized Position`, and `Paper Contributions`.
  - These notes are user-owned argument space. Agents should not rewrite substantive sections unless asked.
- `Literature Review/imports/` - default landing zone for thin main paper notes imported from Zotero.
- `Literature Review/zotero_notes/` - stable home for raw Zotero notes, PDF annotations, and annotation assets.
- `Literature Review/Papers/` - curated location for organized paper headers after import. Once you have processed an imported note, you can move it here.
- `Literature Review/templates/` - Zotero Integration templates for main paper notes and raw Zotero notes.
- `Literature Review/Sources by Domain.md` - source bank for papers discovered while reading but not yet fully processed.

#### 3. The AI workflow folder

- `ai/README.md` - index of agent handoff notes and cross-vault anchors.
- `ai/init-project-workflow.md` - this setup and onboarding workflow.
- `ai/zotero-import-template-guide.md` - explains the Zotero Integration commands, templates, output paths, and asset handling.
- `ai/paper-reading-guide-workflow.md` - used before reading a paper. It produces an inline, verdict-scaled reading guide so the user knows what to read closely, skim, or skip.
- `ai/synthesis-integration-workflow.md` - used after reading and Zotero-note completion. It produces an HTML checklist under `ai/outputs/` for integrating paper contributions into synthesis notes.
- `ai/templates/synthesis-checklist-template.html` - base HTML template for synthesis integration checklists.
- `ai/outputs/` - generated checklist artifacts.
- `ai/scripts/validate_ai_docs.py` - validator for required files, wikilinks, symlinks, plugin config paths, and template hygiene.

#### 4. The core paper workflow

Explain the normal loop:

1. Add a paper to Zotero.
2. Before close reading, use `ai/paper-reading-guide-workflow.md` when the user wants triage help. It connects the paper to the current project context, reading map, synthesis notes, and existing arguments so the user knows what to read closely, skim, or skip.
3. Read and annotate in Zotero.
4. Run `Import overview paper` to create `Literature Review/imports/{citekey}.md`.
5. Run `Import Zotero notes` to create `Literature Review/zotero_notes/{citekey}-zotero-notes.md`.
6. Treat the main note as a thin wrapper/navigation hub to the Zotero notes and linked material. It may hold light context, but the durable reading record lives in Zotero/Zotero notes and cross-paper argument lives in synthesis notes.
7. Integrate from the Zotero notes into the relevant synthesis notes.
8. If requested, use `ai/synthesis-integration-workflow.md` to generate a checklist that guides the integration.

#### 5. The two main AI-assisted research workflows

- **Paper reading guide**:
  - Trigger: before reading, when the user has a PDF and wants help triaging it.
  - Output: inline markdown, not saved by default.
  - It assigns a relevance verdict (`High`, `Moderate`, `Light`) and tells the user what to read closely, skim, or skip.
- **Synthesis integration**:
  - Trigger: after reading, when Zotero notes are complete.
  - Output: HTML checklist in `ai/outputs/{citekey}-synthesis-checklist.html`.
  - It maps the paper into synthesis notes with PC/WT/SP/META items and records skipped notes deliberately.
  - Abbreviations: PC = Paper Contributions, WT = Working Thoughts, SP = Synthesized Position, META = cleanup/linking/caveat tasks.

#### 6. What setup will personalize

Explain that the full setup process will:

- Verify Zotero, Better BibTeX, Obsidian, Local REST API, MCP, and Zotero imports.
- Replace generic placeholders with the user's project title, deliverables, and research question.
- Optionally create or update synthesis themes.
- Optionally seed the reading map.
- Finalize agent context so future chats can start quickly.

### How to close the introduction

Ask:
1. Does this all make sense?
2. Shall we move on to Phase 1 (Local App Installation)?

---

## Phase 1: Local App Installation

**Goal:** Ensure Zotero, Better BibTeX, Obsidian, and the required Obsidian plugins are installed.

### 1A. Zotero

Ask the user to confirm:
1. Zotero is installed.
2. Zotero can open normally.
3. The user has at least one test paper or reference available for the later import test.

If Zotero is not installed, guide the user:
1. Download Zotero from `https://www.zotero.org/`.
2. Install and open Zotero.
3. Add one test item. A Zotero "item" is any entry in the library (a paper, book, etc.). The easiest way is to drag a PDF paper into the Zotero window, or use the magic wand icon with a DOI. This is needed so the import pipeline can be tested later.

### 1B. Better BibTeX for Zotero

Explain why this is required:
- Better BibTeX provides stable citekeys.
- This vault uses citekey-based filenames like `Literature Review/imports/{{citekey}}.md` and `Literature Review/zotero_notes/{{citekey}}-zotero-notes.md`.
- Citekeys should remain stable after notes have been imported.
- The Zotero Integration plugin depends on Zotero citekeys for this workflow.

Guide the user:
1. Download the latest Better BibTeX `.xpi` from `https://github.com/retorquere/zotero-better-bibtex/releases`.
2. If downloading with Firefox, right-click the `.xpi` and save it instead of opening it in the browser.
3. In Zotero, open `Tools > Plugins` (or `Tools > Add-ons` on older Zotero versions).
4. Click the gear icon and choose `Install Plugin From File...`.
5. Select the downloaded `.xpi`.
6. Restart Zotero if prompted.
7. Confirm Better BibTeX appears in Zotero's plugin list.

Recommended Better BibTeX checks:
- Open Zotero preferences and find the Better BibTeX settings.
- Keep citekey generation stable. Defaults are acceptable for most projects.
- If the user wants a custom citekey pattern, decide it now before importing literature.
- Do not change citekey rules casually after Obsidian notes have been generated.
- Verify at least one Zotero item shows a citekey before continuing. To find it, select the Zotero item and look in the item details panel on the right, near the top.

### 1C. Obsidian

Guide the user:
1. Install Obsidian from `https://obsidian.md/`.
2. Open this repository directory as your Obsidian vault.
3. When prompted, trust the vault author and allow community plugins.
4. Open `Settings > Community plugins`.
5. If you see a button that says "Turn on community plugins", click it. If you see "Restricted mode is on", turn it off.

### 1D. Zotero Integration Plugin

Explain why this is required:
- Zotero Integration imports Zotero metadata, notes, and PDF annotations into Obsidian using the templates in `Literature Review/templates/`.
- The vault may include templates and a preconfigured `data.json`, but it does not ship plugin binaries. The user must install and enable the plugin manually in each vault.

Guide the user:
1. In Obsidian, open `Settings > Community plugins > Browse`.
2. Search for `Zotero Integration`.
3. Click **Install**, then **Enable**.
4. Keep Zotero open while using the plugin.
5. Open `Settings > Zotero Integration`.
6. Look under the **Import Formats** section. Check if "Import overview paper" and "Import Zotero notes" are already there.
   - **If they are present:** Great, the template config loaded automatically. You can skip step 7.
   - **If they are missing:** Add them manually using the exact values from this table:

| Field | Import overview paper | Import Zotero notes |
|-------|-----------------------|---------------------|
| Name | `Import overview paper` | `Import Zotero notes` |
| Output Path | `Literature Review/imports/{{citekey}}.md` | `Literature Review/zotero_notes/{{citekey}}-zotero-notes.md` |
| Image Output Path | `Literature Review/zotero_notes/{{citekey}}-zotero-notes-assets` | `Literature Review/zotero_notes/{{citekey}}-zotero-notes-assets` |
| Image Base Name | `annotation` | `annotation` |
| Template Path | `Literature Review/templates/overview-paper-template.md` | `Literature Review/templates/zotero-notes-template.md` |

If the plugin UI or field names differ from this file, use the Zotero Integration Data Explorer on a test item to inspect available template variables before editing templates.

### 1E. Local REST API & MCP Server Plugin

Explain why this is required:
- Local REST API & MCP Server exposes the vault to AI tools through a local API and MCP server.
- It is commonly used by Obsidian MCP servers so agents can read and update vault files.
- API keys and generated TLS material are local secrets and must not be committed or pasted into shared notes.
- The vault does not ship this plugin binary. The user must install it manually in Obsidian.

Guide the user:
1. In Obsidian, open `Settings > Community plugins > Browse`.
2. Search for `Local REST API & MCP Server` or `Local REST API`.
3. Install and enable it.
4. Open `Settings > Local REST API & MCP Server`.
5. Note the port. The secure HTTPS default is commonly `27124`; insecure HTTP is commonly `27123` if explicitly enabled.
6. Copy the API key only into your MCP client configuration. **WARNING:** Do not paste your existing MCP config into the chat here, as it may contain API keys from other services. Do not save the API key into any vault notes.
7. If configuring Claude Code, scroll down in the plugin settings and use the included MCP configuration example as the reference shape.

**Execution:**
- Do not modify plugin secrets.
- If file access exists, run `python3 ai/scripts/validate_ai_docs.py`.
- Update `ai/INIT_STATE.md` if it exists; otherwise update the chat-backed checklist.

---

## Phase 2: MCP Setup and Verification

**Goal:** Ensure the user's AI agent can access the Obsidian vault through MCP.

Ask which MCP client/environment the user uses:
1. Cursor
2. Claude Desktop
3. Another MCP-compatible client
4. No MCP yet

Explain the generic configuration requirements:
- Obsidian must be open.
- The Local REST API & MCP Server plugin must be enabled in the target vault.
- For common Python-based Obsidian MCP servers, the user needs `uvx`, which is installed with `uv`.
  - macOS/Linux install option: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Homebrew install option: `brew install uv`
  - Verify with: `uvx --version`
  - If a GUI MCP client cannot find `uvx`, run `which uvx` and use the absolute path in that client's MCP config.
  - If `uvx` is unavailable, the MCP client will not be able to launch servers configured with `command: "uvx"`.
- The MCP server must know the Local REST API host, port, and API key.
- Common environment variable names used by Obsidian MCP servers include:
  - `OBSIDIAN_API_KEY`
  - `OBSIDIAN_HOST` or `OBSIDIAN_API_BASE_URL`
  - `OBSIDIAN_PORT`
- Common local URLs are:
  - `https://127.0.0.1:27124` for the secure Local REST API server
  - `http://127.0.0.1:27123` only if the insecure server is enabled

Do not assume one MCP server implementation. Different users may use different Obsidian MCP servers. The concrete default to suggest when the user has no preference is `mcp-obsidian` via `uvx`, because it works with the Local REST API plugin and uses the API key/host/port model. If the user already chose another MCP server, adapt to that server's documentation. The test is the same: the agent must be able to list files and read a known note from the vault.

Suggested Claude Desktop shape for `mcp-obsidian` via `uvx`:

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "uvx",
      "args": ["mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "[your-local-api-key]",
        "OBSIDIAN_HOST": "127.0.0.1",
        "OBSIDIAN_PORT": "27124"
      }
    }
  }
}
```

For Cursor or another MCP client, use the same command, args, and environment variables in that client's MCP settings. If the user's chosen MCP server is not Python/`uvx`-based, use that server's documented command instead. Still verify the same things: Obsidian is open, Local REST API is enabled, the API key is configured outside the vault, and the agent can read known vault files.

Verification prompts for the user or agent:
1. Can the MCP list the vault root files?
2. Can it read `AGENTS.md`?
3. Can it read the current project context file (the default context note, or the renamed context file if Phase 4 renamed it)?
4. Can it read `Literature Review/README.md`?
5. Can it read `ai/init-project-workflow.md`?
6. Does the content match this vault, not another Obsidian vault? Check the project title or template placeholders, not just file names.

If MCP points to the wrong vault:
- Tell the user which evidence suggests the wrong vault.
- Ask them to open the intended vault in Obsidian and reload MCP if MCP is required.
- If the agent has direct local file access and the user wants to continue, continue via direct file access and record MCP as a follow-up.

If MCP is not available:
- Continue initialization using direct file access if the agent has it.
- Mark MCP as "manual follow-up needed" in `ai/INIT_STATE.md` if it exists; otherwise mark it in the chat-backed checklist.
- Do not claim the vault is fully MCP-ready.

**Execution:**
- Update `ai/INIT_STATE.md` with MCP status if it exists; otherwise update the chat-backed checklist.
- If MCP now gives the agent file access and `ai/INIT_STATE.md` does not exist yet, create it from the chat-backed checklist before continuing.
- Do not store API keys in vault notes.

---

## Phase 3: Zotero Import Pipeline Verification

**Goal:** Confirm the user can import a paper shell and raw Zotero notes before personalizing the research workflow too far.

Ask the user:
1. Do you have a disposable test Zotero item we can import?
2. Does it have a Better BibTeX citekey?
3. Does it have a PDF annotation or Zotero child note, if you want to test raw-note import?

Guide the user:
1. In Obsidian, run the Zotero Integration command `Import overview paper`.
2. Select the test Zotero item.
3. Confirm it creates `Literature Review/imports/{citekey}.md`.
4. Run `Import Zotero notes`.
5. Select the same test item.
6. Confirm it creates `Literature Review/zotero_notes/{citekey}-zotero-notes.md`.
7. If annotation images are exported, confirm they go under `Literature Review/zotero_notes/{citekey}-zotero-notes-assets`.
8. Open the main note and confirm it links to the raw Zotero note.

If test imports were only for setup verification, ask the user to delete the test notes (`Literature Review/imports/{citekey}.md` and `Literature Review/zotero_notes/{citekey}-zotero-notes.md`) in Obsidian by right-clicking and choosing Delete. Do not attempt to delete them via agent file commands.

Troubleshooting:
- If the command cannot find Zotero items, confirm Zotero is open and Better BibTeX is installed.
- If filenames use titles instead of citekeys, fix the import format output paths before continuing.
- If assets appear at the vault root, fix the import image path to use the stable `zotero_notes` asset folder.
- If templates render raw `{{...}}` tokens unexpectedly, inspect the Zotero Integration template settings and the Data Explorer for current field names.

**Execution:**
- If plugin settings are changed in Obsidian but the agent has no file access, ask the user to confirm the expected paths manually and mark validation as pending.
- If plugin settings are changed and the agent has file access, run `python3 ai/scripts/validate_ai_docs.py`.
- Update `ai/INIT_STATE.md` if it exists; otherwise update the chat-backed checklist.

---

## Phase 4: Discovery & Core Project Details

**Goal:** Capture only the user's explicit project details and write them into the core context files. This phase can stay minimal. The user can expand the framing in a later agent chat after setup.

Ask one question at a time:

1. Working title.
   - Ask: "What do you call this project right now?"
   - Offer examples only as examples, not content to write.
2. Main research question or core problem.
   - Ask for one or two sentences.
   - If the user is unsure, offer formulation help and wait for their chosen wording.
3. Key deliverables.
   - Ask what they plan to produce.
   - Examples: systematic literature review, taxonomy, framework, prototype, manuscript, article draft, dataset, design artifact.
4. Project type.
   - Examples: seminar paper, thesis, dissertation chapter, capstone, independent research project, product research project.
5. Core file names.
   - Defaults: keep the standard project context note and standard project overview note.
   - If the user wants project-specific names, ask for the exact filenames.

Do not ask about external locations during setup. Those can be documented later if the user brings them up.

The user may answer all Phase 4 questions at once. If they do, process only what they explicitly provided.

**Execution:**
- If the agent does not have file access, do not claim personalization is complete. Record the user's answers in the chat-backed checklist, mark `File update status: pending until file access is available`, and tell the user to continue this phase with Cursor, Claude Code/Cowork, or another agent that can edit the repository.
- If the agent has file access, inject only the provided answers into the placeholder brackets inside the project context note and project overview note, or their renamed equivalents. Leave unknowns blank, placeholdered, or explicitly "not specified yet"; do not invent missing details.
- If the user requested file renames and the agent has file access, execute the renames, update all internal wikilinks in the vault that point to them, and update `ai/scripts/validate_ai_docs.py` to check for the new filenames.
- If file access exists, update `AGENTS.md` only where the project-level summary or renamed paths require it.
- Do not modify `Glossary.md` during setup.
- Add a short note in the project context or overview inviting the user to start a follow-up chat to expand framing if the file remains sparse.
- If file access exists, run validation script. Update `ai/INIT_STATE.md` if it exists; otherwise update the chat-backed checklist.

---

## Phase 5: Literature Review & Synthesis Setup

**Goal:** Optionally seed the literature-review scaffolding. This phase is useful but not required. The user may skip it, provide only a guiding question, name only one or two themes, or leave the reading map empty for now.

First explain:
- This phase creates optional scaffolding for future reading.
- Synthesis notes and the reading map can be populated later.
- The reading map is optional and can be removed if the user does not want it.
- The agent will only create notes and source lists the user explicitly names or confirms.

Ask one question at a time unless the user volunteers a complete answer:

1. Do you want to seed the literature-review scaffolding now, or skip this phase for later?
2. If yes: What is the primary guiding question for the literature review?
3. Are there themes, dimensions, or arguments you already know you want to track?
   - Offer 2-3 examples based on Phase 4 answers, but ask before creating notes from them.
4. Do any synthesis notes need special roles, such as "The Problem", "Theory", "Methods", "Design Strategies", "Outcomes", or "Open Questions"?
5. Do you have initial must-read papers, authors, venues, or domains?
6. If sources were named: which are must-read versus broader/contextual?
7. If must-read sources were named: do you want a minimum viable reading set called out in the reading map so future agents can use the verdict flag-and-ask rule?

**Execution:**
- If the user skips, mark Phase 5 skipped and do not create synthesis notes or reading-map content.
- If the agent does not have file access, do not claim literature setup is complete. Record the guiding question, themes, source priorities, and requested note roles in the chat-backed checklist, mark `File update status: pending until file access is available`, and pause file updates until an agent with file access continues.
- If file access exists, create a new markdown file only for each user-confirmed theme or special role inside `Literature Review/Synthesis/`. Use the structure in `Literature Review/Synthesis/README.md`:
  - Frontmatter
  - Intro paragraph
  - Current Argument
  - Working Thoughts
  - Synthesized Position
  - Paper Contributions
  - Related
- If file access exists, update `Literature Review/Overview Synthesis and Reading Map.md` only with provided or confirmed material:
  - guiding question, if provided
  - phases or priority groups, if provided
  - must-read / minimum viable sources, if provided
  - broader source lists, if provided
  - confirmed synthesis themes
- If file access exists, update `Literature Review/README.md` only enough to reflect confirmed guiding question and theme structure.
- If file access exists, update `Literature Review/Sources by Domain.md` only with domains or source banks the user named.
- If file access exists, run validation script. Update `ai/INIT_STATE.md` if it exists; otherwise update the chat-backed checklist.

---

## Phase 6: Workflow Calibration

**Goal:** Ensure the user understands how the working workflows should behave after initialization.

Before asking preferences, briefly re-explain the two AI workflows:

- Paper reading guide: used before close reading. It reads the paper against the current project context, reading map, and synthesis notes, then tells the user what to read closely, skim, or skip. It is needed to keep reading effort aligned with the current argument rather than treating every paper as equally important.
- Synthesis integration: used after reading and Zotero-note completion. It reads the Zotero notes and synthesis notes, then creates an HTML checklist for moving only the paper's relevant contributions into synthesis notes. It is needed to prevent duplication of Zotero notes and to keep cross-paper synthesis deliberate.

Ask the user:
1. Do you want paper reading guides to remain ephemeral inline chat artifacts by default?
2. Do you want synthesis integration checklists saved under `ai/outputs/` by default?
3. Should the relevance verdict labels stay `High`, `Moderate`, and `Light`, or do you want project-specific names?
4. Are there any project-specific anchor notes future agents should conditionally pull before reading-guide or synthesis-integration work?

*Wait for response.*

**Execution:**
- If the agent does not have file access, record the requested workflow calibration in the chat-backed checklist and mark workflow file updates as pending.
- If file access exists, update `ai/paper-reading-guide-workflow.md` only if the user wants project-specific calibration.
- If file access exists, update `ai/synthesis-integration-workflow.md` only if the user wants project-specific anchor-note rules or verdict language.
- Keep generic template mechanics intact unless this is now a private initialized project.
- If file access exists, update `ai/README.md` if output policies change.
- If file access exists, run validation script. Update `ai/INIT_STATE.md` if it exists; otherwise update the chat-backed checklist.

---

## Phase 7: Agent Context Finalization & Cleanup

**Agent Action:** Finalize the AI instructions so future agent sessions understand the project natively.

**Execution (No user input required for this step):**
- If the agent does not have file access, do not claim finalization is complete. Produce a concise handoff summary in chat containing all gathered setup answers, pending file updates, pending validation, and recommended next agent with file access.
- If file access exists, rewrite the `## Project Context` section inside `AGENTS.md` using a crisp, synthesized summary of everything learned in the setup phases.
- If file access exists, ensure `AGENTS.md` explicitly mentions:
  - the project title and type
  - core question or problem
  - deliverables
  - synthesis themes
  - important external folders or repositories, if any
  - whether MCP is fully configured or still a manual follow-up
- If file access exists, keep root `AGENTS.md` as a short entry point unless the user wants more detail there.
- If file access exists, run `python3 ai/scripts/validate_ai_docs.py` one final time.

**Agent Action:** Present a completion summary.
- Tell the user initialization is complete, or clearly list any manual setup still pending.
- Print the final checklist of what was accomplished.
- Do not mark Phase 7 complete until cleanup has actually run or the user explicitly defers cleanup.
- Delete `ai/INIT_STATE.md` only if it exists and only after feedback has been moved to a durable note when needed and the user confirms no follow-up setup steps are needed.
- Ask whether disposable Zotero test imports should be deleted if they are still present.
- In developer/test mode, it is acceptable to keep `ai/INIT_STATE.md`, test imports, or local workspace state temporarily, but record that cleanup was deferred.
- Keep `ai/init-project-workflow.md` and its reference in `ai/README.md` for reusable template vaults. Only offer to archive or remove the setup runbook if this is now a private initialized project and the user explicitly wants that.
- Ask which paper, source list, or project task they want to tackle first.

## Related Notes

- [[AGENTS]]
- current project context file
- [[ai/README]]
- [[ai/init-project-feedback]]
- [[ai/zotero-import-template-guide]]
- [[ai/paper-reading-guide-workflow]]
- [[ai/synthesis-integration-workflow]]
- [[Literature Review/README]]
- [[Literature Review/Synthesis/README|Synthesis folder]]
