# Research Vault Template

A comprehensive, AI-ready Obsidian vault template for academic research, literature reviews, and synthesis. It is designed to help you actively engage with your sources and build cross-paper arguments using a structured, agent-assisted workflow.

## 🚀 Getting Started

To turn this generic template into your own project workspace, follow these setup steps:

### 1. Local Environment Setup

For the literature review workflow to function correctly, you need to configure Zotero and Obsidian:

**Zotero Setup:**
1. Download and install [Zotero](https://www.zotero.org/).
2. Install the **Better BibTeX** extension for Zotero:
   - Download the latest `.xpi` file from the [Better BibTeX GitHub Releases](https://github.com/retorquere/zotero-better-bibtex/releases).
   - In Zotero, go to `Tools` > `Add-ons` (or `Plugins`).
   - Click the gear icon in the top right and select `Install Add-on From File...`.
   - Select the `.xpi` file you downloaded and restart Zotero.
3. Configure Better BibTeX to keep your citekeys stable (the default settings are usually fine).

**Obsidian & MCP (AI) Setup:**
1. Open this repository folder as a Vault in Obsidian.
2. When Obsidian prompts you, **Trust the authors and enable community plugins** (Safe Mode: OFF). 
3. This vault comes pre-configured with the **Zotero Integration** plugin. Make sure Zotero is open in the background so the plugin can connect to it.
4. This vault also comes pre-configured with the **Local REST API** plugin. This is required for AI agents (via the Model Context Protocol, MCP) to read your vault files.
   - Go to Obsidian Settings > **Local REST API**.
   - Copy your API Key and Port.
   - Configure your MCP server (e.g., in Claude Desktop's `claude_desktop_config.json` or your specific AI environment) to connect to Obsidian using these credentials.

### 2. AI Initialization & Personalization

This template includes a built-in AI workflow to help you personalize the vault for your specific research project.

Open your AI agent (e.g., Claude, Cursor, or OpenCode) in this folder and prompt it with:

> "Please run the `init-project-workflow` to help me set up this vault."

The agent will walk you through a step-by-step interview to:
- Define your project title, deliverables, and core problem.
- Establish your literature review guiding questions and synthesis themes.
- Seed your project glossary.
- Automatically rewrite all the foundational files and context guidelines (`AGENTS.md`, `THESIS_CONTEXT.md`, etc.) to perfectly match your project.

### 3. Understanding the Workflows

Once initialized, the vault offers several automated workflows to accelerate your reading and synthesis. 

Check out the AI workflow guides located in the `ai/` folder for details on how to invoke them:
- `ai/paper-reading-guide-workflow.md`: Generates a pre-reading triage guide for a new PDF.
- `ai/synthesis-integration-workflow.md`: Helps integrate your Zotero notes into your cross-paper synthesis themes.
- `ai/zotero-import-template-guide.md`: Explains how the Zotero to Obsidian import pipeline works.

Happy researching!
