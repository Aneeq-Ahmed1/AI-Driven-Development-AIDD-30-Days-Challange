# 📚 Study Notes Summarizer & Quiz Generator

Live App: [Study Notes Summarizer & Quiz Generator](https://ai-driven-development-aidd-30-days-challange-tbq8kz3jgwzrmnej3.streamlit.app/)

---

## Overview

This project is an AI-powered agent that helps students **summarize PDFs** and **generate quizzes** from study materials. It leverages the following technologies:

* **OpenAgents SDK**
* **Streamlit** (for UI; HTML/CSS optional)
* **PyPDF** (for PDF text extraction)
* **Gemini CLI**
* **Context7 MCP** (tool provider)

The agent simplifies studying by providing concise summaries and automated quizzes for any uploaded PDF.

---

## Features

### A. PDF Summarizer

* Users upload a PDF file.
* Text is extracted using **PyPDF**.
* The agent generates a **clean and meaningful summary**.
* The summary is displayed in a customizable UI style (card, block, container, etc.).

### B. Quiz Generator

* After summarization, users can click **Create Quiz**.
* The agent reads the **original PDF** (not just the summary).
* It generates:

  * **Multiple Choice Questions (MCQs)**
  * Or **mixed-style quizzes**.

> **Note:** These two functionalities are the core requirements, but additional features can be added.

---

## How to Use

1. Open the app via the link above.
2. Upload your PDF document.
3. View the generated summary.
4. Click **Create Quiz** to generate questions from the original PDF.

---

## Tech Stack

* **Python**: Programming language
* **Streamlit**: Web app UI
* **PyPDF**: PDF text extraction
* **OpenAgents SDK**: Agent creation
* **Gemini CLI**: LLM integration
* **Context7 MCP**: Tool provider

---


 Add license info if required)*
