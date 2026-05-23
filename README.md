# Research Vault Template

A comprehensive, AI-ready Obsidian vault template for academic research, literature reviews, and synthesis. It is designed to help you actively engage with your sources and build cross-paper arguments using a structured, agent-assisted workflow.

## Getting Started

### Important: Create Your Own Repository First

Do not track your project work directly against `Loligplayer33/research-vault-template`. If you are starting a new research vault, use GitHub's **Use this template** button to create a repository under your own account, then clone that new repository.

If you already cloned this repository directly, create your own empty repository and replace `origin` before personalizing the vault:

```bash
git remote -v
git remote set-url origin <your-new-repo-url>
git push -u origin main
```

The initialization workflow checks this automatically at the start with:

```bash
python3 ai/scripts/check_template_remote.py
```

To turn this generic template into your own project workspace, start with the built-in initialization workflow. It is the canonical setup path for this template.

### 1. Start With The Agent Workflow

Open an AI agent with local file access to this repository, such as Cursor at the repository root or Claude Code/Cowork opened in this folder, and prompt it with:

> "Please run the `ai/init-project-workflow.md` workflow to help me set up this vault."

For first-time setup, local file access is highly recommended. Before MCP is installed, an MCP-only agent can explain the vault and guide manual installation, but it may not be able to edit files, create or update setup state, rename notes, create synthesis notes, personalize context files, delete setup state, or run validation. Use an MCP-only agent for orientation if needed; use Cursor, Claude Code/Cowork, or another local-file-access coding agent for the full setup.

The agent-facing workflow will walk you through:

- Choosing whether you want a vault introduction, the full installation/personalization process, or both.
- Understanding the vault folders, context files, and main research workflows.
- Installing or verifying Zotero, Better BibTeX, Obsidian, Zotero Integration, Local REST API & MCP Server, and MCP access.
- Testing the Zotero import commands before relying on them.
- Defining your project title, deliverables, and core problem.
- Establishing your literature review guiding question and synthesis themes.
- Updating the foundational context files (`AGENTS.md`, the project context note, the project overview note, and workflow docs) for your project.

**To open the vault:** Simply open this repository root directory as a vault in Obsidian.

## Technical Installation Reference

The init workflow above should guide you through these steps interactively. Use this section as a reference if you want to install pieces manually or understand what the agent is checking.

### Zotero Setup

1. Download and install [Zotero](https://www.zotero.org/).
2. Install the **Better BibTeX** extension for Zotero:
   - Download the latest `.xpi` file from the [Better BibTeX GitHub Releases](https://github.com/retorquere/zotero-better-bibtex/releases).
   - If downloading with Firefox, right-click and save the `.xpi` instead of opening it in the browser.
   - In Zotero, go to `Tools` > `Plugins` (or `Tools` > `Add-ons` on older Zotero versions).
   - Click the gear icon in the top right and select `Install Plugin From File...` / `Install Add-on From File...`.
   - Select the `.xpi` file you downloaded and restart Zotero.
3. Configure Better BibTeX to keep your citekeys stable. The default settings are usually fine, but choose any custom citekey pattern before importing papers into Obsidian. To verify a citekey, select a Zotero item and look in the details panel on the right, near the top.

### Obsidian And MCP Setup

1. Open this repository directory as a vault in Obsidian.
2. When Obsidian prompts you, **Trust the authors and enable community plugins** (Safe Mode: OFF). 
3. Install the **Zotero Integration** plugin:
   - Go to Obsidian Settings > Community plugins > Browse.
   - Search for "Zotero Integration" and click Install, then Enable.
   - The vault may include templates and configuration, but it does not ship plugin binaries. Install the plugin manually in each new vault.
   - Open Settings > Zotero Integration.
   - Look under **Import Formats**. If "Import overview paper" and "Import Zotero notes" are already configured, skip to the next step. Otherwise, add them manually exactly like this:

| Field | Import overview paper | Import Zotero notes |
|-------|-----------------------|---------------------|
| Name | `Import overview paper` | `Import Zotero notes` |
| Output Path | `Literature Review/imports/{{citekey}}.md` | `Literature Review/zotero_notes/{{citekey}}-zotero-notes.md` |
| Image Output Path | `Literature Review/zotero_notes/{{citekey}}-zotero-notes-assets` | `Literature Review/zotero_notes/{{citekey}}-zotero-notes-assets` |
| Image Base Name | `annotation` | `annotation` |
| Template Path | `Literature Review/templates/overview-paper-template.md` | `Literature Review/templates/zotero-notes-template.md` |
4. Install the **Local REST API & MCP Server** plugin (required for MCP):
   - Go to Obsidian Settings > Community plugins > Browse.
   - Search for "Local REST API & MCP Server" or "Local REST API" and click Install, then Enable.
   - The vault does not ship this plugin binary. Install it manually in each new vault.
   - Go to the plugin's settings to find your API key and port. The secure default port is commonly `27124`; some MCP servers use the insecure local port `27123` only if you explicitly enable it.
   - Scroll down in the plugin settings for the built-in Claude Code MCP configuration example.
   - Install `uv`/`uvx` if your Obsidian MCP server is launched with `uvx`: `brew install uv` or `curl -LsSf https://astral.sh/uv/install.sh | sh`, then verify with `uvx --version`.
   - Configure your MCP server (e.g., in Claude Desktop's `claude_desktop_config.json` or your specific AI environment) to connect to Obsidian using these credentials. Many Python-based MCP configs use `command: "uvx"` plus the server package name in `args`.
   - Treat the Local REST API key and generated TLS material as machine-local secrets. Do not share them or commit a personalized `data.json`.

## Understanding The Workflows

Once initialized, the vault offers several automated workflows to accelerate your reading and synthesis. 

Check out the AI workflow guides located in `ai/` for details on how to invoke them:
- `ai/init-project-workflow.md`: Agent-facing setup and personalization runbook.
- `ai/paper-reading-guide-workflow.md`: Generates a verdict-scaled pre-reading triage guide for a new PDF.
- `ai/synthesis-integration-workflow.md`: Helps integrate completed Zotero notes into your cross-paper synthesis themes and writes checklist artifacts to `ai/outputs/`.
- `ai/zotero-import-template-guide.md`: Explains how the Zotero to Obsidian import pipeline works.

Happy researching!
