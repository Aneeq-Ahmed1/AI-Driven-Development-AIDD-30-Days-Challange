🚀 Overview

This project showcases how I successfully connected the Hosted GitHub MCP Server with the Google Gemini CLI. After the integration, Gemini can interact with my GitHub repositories, list files, check metadata, and use 90+ MCP tools — all without Docker or any local MCP setup.

This is the simplest, fastest way to give your AI access to GitHub.

✨ What This Project Includes

✔ Secure .env token handling
✔ Fully configured settings.json for MCP
✔ Gemini connected to GitHub MCP Server
✔ Verification using mcp list
✔ AI successfully reading GitHub repositories

📁 Project Structure
📦 mcp-github-integration
│
├── 📄 .env               # GitHub Token stored securely
├── 📄 settings.json      # MCP Server configuration
└── 📄 README.md          # You're reading it!

🔐 1. Secure Token Setup (.env)

Create .env file:

GITHUB_TOKEN=ghp_xxxxxxxxxxxxx


⚠ Make sure not to expose this token publicly.
⚠ Blur it in screenshots.

⚙️ 2. MCP Configuration (settings.json)

This is the exact configuration used to connect Gemini with GitHub MCP:

{
  "mcpServers": {
    "github": {
      "server": "mcp+https://mcp-github.fly.dev",
      "credentials": {
        "GITHUB_TOKEN": {
          "type": "env",
          "env": "GITHUB_TOKEN"
        }
      }
    }
  }
}


✔ No installation needed
✔ Token auto-loaded
✔ Remote MCP server (hosted)

🔄 3. Restart Gemini CLI

Close terminal → Open Gemini again
The MCP server loads automatically.

🟢 4. Connection Verification
Run:
mcp list

Expected Output:
🟢 github — Ready (90+ tools)


🎉 This confirms your GitHub MCP connection is successful.

🧪 5. Test the AI Connection

Ask Gemini:

List my GitHub repositories


If it shows your repo list → 🎯 Integration Complete

🛠️ AI Capabilities After Integration

After successful MCP connection, Gemini can:

📂 List repositories

📄 Read files

🧭 Navigate directories

📝 View commits & branches

🧰 Use 90+ GitHub automation tools

🤖 Act like a GitHub assistant

📸 Submission Checklist

Make sure to upload:

✔ .env file (token blurred)

✔ settings.json screenshot

✔ mcp list output

✔ Gemini response showing your GitHub repos

👨‍💻 Developed By
Aneeq Ahmed

AI-Driven Development — Task 6 Submission

🌐 Instructor Team

Prepared By: Asma Yaseen
Supervised By: Sir Hamzah Syed

🎉 Completed Successfully!
