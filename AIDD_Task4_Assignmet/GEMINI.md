⭐ 1. Overview

This document describes how the Study Notes Summarizer & Quiz Generator Agent was created using:

OpenAgents SDK

Streamlit UI

PyPDF for PDF text extraction

Gemini CLI

Context7 MCP Server (Tool provider)

The agent summarizes uploaded PDFs and generates MCQs based on the content.

⭐ 2. MCP Server Connection (Context7)
2.1 What is MCP?

MCP provides tools to AI agents

Connects Gemini CLI with external capabilities

Allows tool calling (documentation, code snippets, APIs, etc.)

2.2 Why Context7?

Provides always-updated docs for:

Python

FastAPI

OpenAgents SDK

Supabase

Modern frameworks

Ensures Gemini never returns outdated code

Enables correct agent-building workflow

2.3 MCP Setup Steps

The following was added to ~/.gemini/settings.json:

"mcpServers": {
  "context7": {
    "httpUrl": "https://api.context7.com/mcp",
    "headers": {
      "CONTEXT7_API_KEY": "YOUR_API_KEY",
      "Accept": "application/json, text/event-stream"
    }
  }
}

2.4 Verify MCP Installation
/mcp


Should show:
✔ context7 connected
✔ tools available

⭐ 3. Project Structure
.
├── app.py               # Streamlit UI
├── agent.py             # Agent logic
├── tools.py             # Functions exposed as tools (if required)
├── requirements.txt / pyproject.toml
├── user_profile.json    # (optional for extended features)
├
└── README.md

⭐ 4. Agent Requirements (Task Instruction Breakdown)
A. PDF Summarizer

User uploads a PDF

Extract text using PyPDF

Agent generates a clean summary

Summary displayed in UI block/cards

B. Quiz Generator

Based on original PDF (not summary)

Generates:

MCQs

OR mixed question types

Presented in readable format

⭐ 5. Technologies Used
Component	Usage
OpenAgents SDK	Agent logic + Tool execution
Streamlit	Web UI for file upload, summary, quiz
PyPDF	Parse / extract text from PDF
Gemini CLI	Prompting & generating agent code
Context7 MCP Server	Documentation + real-time tool provider
⭐ 6. Gemini CLI Prompt (Required Screenshot)

This prompt was executed inside Gemini CLI to generate the project instructions & structure:

Create a Study Notes Summarizer & Quiz Generator agent using:
- OpenAgents SDK
- Streamlit UI
- PyPDF for PDF text extraction
- Context7 MCP tooling
Provide complete structure, agent logic, and clear steps.


➡ Insert screenshot here
./screenshots/gemini_cli_prompt.png

⭐ 7. How the Agent Works (Flow)
Step 1 — Upload PDF

User selects a PDF in Streamlit UI.

Step 2 — Extract Text

PyPDF reads the document → All text combined.

Step 3 — Summarization

OpenAgents + Gemini produce a clean summary.

Step 4 — Quiz Generator

Agent analyzes extracted text → Creates MCQs.

Step 5 — .env

Create .env file for GEMINI_API_KEY

Step 6 — Streamlit UI

Built the Streamlit UI file 