# AI Engineering – 30-Day Builder

A 30-day hands-on AI Engineering journey focused on building practical AI systems, automation workflows, RAG applications, AI agents, and safe human-in-the-loop systems.

This repository contains four practical projects built and documented throughout the journey.

---

## 🚀 Projects

| Project | Skills / Technologies | Demo | Status |
|---|---|---|---|
| [Project 1 – RAG Assistant](./project-1-rag/) | Python, RAG, Embeddings, LangChain, Ollama, Llama 3.2, Streamlit | Local Streamlit App | ✅ Completed |
| [Project 2 – AI Lead Automation](./project-2-leads/) | n8n, AI, JavaScript, Google Sheets, Webhooks, HTTP Requests | n8n Workflows | ✅ Completed |
| [Project 3 – AI Social Media Assistant](./project-3-social/) | n8n, Ollama, JavaScript, Google Sheets, AI Content Drafting | n8n Workflow | ✅ Completed |
| [Project 4 – Tool-Using AI Agent](./project-4-agent/) | n8n, Ollama, AI Agents, Tool Calling, Multi-Step Tasks, MCP Concepts | n8n AI Agent | ✅ Completed |

---

# 📌 Project 1 – RAG Assistant

A Retrieval-Augmented Generation based question-answering system built with Python, embeddings, Ollama, and Streamlit.

### Key Features

- Document-based question answering
- Embedding generation
- Similarity-based retrieval
- Context-grounded responses
- Ollama / Llama 3.2 integration
- Streamlit interface
- Out-of-context question handling

### Main Learning

I learned how documents can be converted into embeddings, relevant context can be retrieved using similarity search, and that context can be provided to a language model to generate grounded answers.

[View Project 1 →](./project-1-rag/)

---

# 📌 Project 2 – AI Lead Automation

An AI-assisted lead management and automation system built with n8n, AI, JavaScript, and Google Sheets.

### Key Features

- Webhook-based lead intake
- AI-assisted lead classification
- Priority and recommendation generation
- Google Sheets data storage
- Human approval workflow
- Scheduled follow-up automation
- Lead follow-up tracking

### Main Learning

I learned how AI processing can be combined with workflow automation while keeping humans involved before important actions.

[View Project 2 →](./project-2-leads/)

---

# 📌 Project 3 – AI Social Media Assistant

An AI-assisted content workflow that generates LinkedIn post drafts from verified project and learning notes.

### Key Features

- Source-based content generation
- Three post versions
- Technical version
- Beginner-friendly version
- Short version
- Google Sheets content tracking
- Human approval
- Approve / Reject workflow
- Content safety checks

### Main Learning

I learned that AI-generated content should be based on verified source information and reviewed by a human before approval.

[View Project 3 →](./project-3-social/)

---

# 📌 Project 4 – Tool-Using AI Agent

A controlled AI Agent built with n8n and Ollama that can select and use different tools based on the user's request.

### Tools

- FAQ Search Tool
- Dummy Leads Search Tool
- Follow-up Draft Tool

### Key Features

- AI Agent tool selection
- Structured tool inputs and outputs
- Multiple tool integration
- Multi-step tool execution
- Error and edge-case handling
- Execution log observability
- Safety boundaries
- Draft-only follow-up action
- MCP fundamentals

### Example Multi-Step Task

```text
User Request
     ↓
Get Warm Leads
     ↓
Observe Lead Results
     ↓
Select One Lead
     ↓
Generate Follow-up Draft
     ↓
Final Response

🧠 Skills Demonstrated
AI Engineering
Retrieval-Augmented Generation (RAG)
Embeddings
Similarity Search
LLM Integration
AI Agents
Tool Calling
Multi-Step Agent Workflows
MCP Fundamentals

Automation

n8n
Webhooks
HTTP Requests
Scheduled Workflows
Google Sheets Integration
Human-in-the-Loop Automation

Programming

Python
JavaScript
JSON
Structured Data Handling

AI Safety & Reliability

Human Approval
Input Validation
Error Handling
Edge-Case Testing
Observability
Controlled Tool Permissions
Grounded AI Responses

Development Practices

Git
GitHub
Project Documentation
Testing
Debugging
Architecture Documentation