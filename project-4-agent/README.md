# Project 4 – Tool-Using AI Agent

A controlled AI Agent built with n8n and Ollama that can select and use different tools based on the user's request.

## Overview

This project demonstrates how an AI Agent can move beyond a fixed workflow and make controlled decisions about which tool to use.

The agent can:

- Search a sample FAQ knowledge base
- Retrieve dummy leads by status
- Generate a follow-up message draft
- Perform controlled multi-step tasks using multiple tools
- Handle invalid or unsupported requests
- Provide observable tool execution through n8n logs

The project was built as part of my 30-Day AI Engineering Builder journey.

---

## Problem

A fixed automation workflow follows predefined steps.

However, real-world AI applications often need to decide which action should be performed based on the user's request.

For example:

- A FAQ question should use a knowledge search tool.
- A lead-status request should use a lead search tool.
- A follow-up request should use a draft-generation tool.
- A multi-step request may require more than one tool.

This project explores how an AI Agent can make these tool-selection decisions in a controlled environment.

---

## Goal

The goal was to build an AI Agent that can:

1. Understand the user's request.
2. Select the appropriate tool.
3. Execute the selected tool.
4. Observe the tool output.
5. Use the result when additional steps are required.
6. Return a final response to the user.

### Agent Loop

```text
User Request
     ↓
Understand Goal
     ↓
Choose Tool
     ↓
Execute Tool
     ↓
Observe Result
     ↓
Final Answer


Architecture
The main workflow uses n8n's AI Agent with a local Ollama chat model.

                    ┌──────────────────────┐
                    │     User Request     │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │      AI Agent        │
                    │       (n8n)          │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              ↓                ↓                ↓
       ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
       │   Tool 1    │  │   Tool 2    │  │   Tool 3    │
       │ FAQ Search  │  │ Lead Search │  │Follow-up    │
       │             │  │             │  │Draft        │
       └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
              ↓                ↓                ↓
        FAQ Knowledge      Dummy Leads      Draft Output

The AI Agent uses Ollama as its local chat model.

Tools
Tool 1 – Search FAQ Knowledge Base

Purpose:
Search the sample FAQ knowledge base and return the matching answer.

Input:

{
  "query": "What is your refund policy?"
}

Output:

{
  "answer": "Refunds are available within 7 days.",
  "found": true
}

The tool also handles a missing question by returning a structured error.

Example:

{
  "answer": null,
  "found": false,
  "error": "Question is required."
}
Tool 2 – Get Dummy Leads by Status

Purpose:
Retrieve dummy leads filtered by status.

Supported example statuses include:

hot
warm
cold

Input:

{
  "status": "warm",
  "limit": "2"
}

Output:

{
  "leads": [
    {
      "id": "L002",
      "name": "Priya",
      "status": "warm"
    },
    {
      "id": "L004",
      "name": "Sneha",
      "status": "warm"
    }
  ],
  "count": 2
}

The tool validates the required status and limit before processing the request.

Tool 3 – Generate Follow-up Draft

Purpose:
Generate a follow-up message draft for a selected lead.

Input:

{
  "lead_name": "Priya"
}

Output:

{
  "lead_name": "Priya",
  "draft": "Hi Priya, I hope you're doing well. I wanted to follow up regarding your enquiry and see if you would like any additional information. Please let me know how I can help."
}

This tool only creates a draft.

It does not send emails or messages.

Multi-Step Task:-

The agent was tested with a multi-step request:

"Show me warm leads and prepare a follow-up draft for one of them."

The agent performed the following sequence:

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

The n8n execution log showed the two tool calls in sequence:

Get dummy leads filtered by status
Generate a follow-up message draft for a selected lead

This demonstrated that the agent could use the result of one tool as context for the next step.

Testing:-

The agent and individual tools were tested with different requests.

FAQ Test:-

Request:

What is your refund policy?

Expected:
FAQ Search Tool

Result:
The agent selected the FAQ tool and returned the refund policy successfully.

Status: PASS

Lead Search Test

Request:

Show me 2 warm leads.

Expected:
Dummy Leads Tool

Result:
The agent selected the lead search tool and returned two warm leads.

Status: PASS

Follow-up Draft Test

Request:

Prepare a follow-up draft for Priya.

Expected:
Follow-up Draft Tool

Result:
The agent selected the draft tool and generated a follow-up message.

Status: PASS

Multi-Step Test

Request:

Show me warm leads and prepare a follow-up draft for one of them.

Expected:
Lead Search Tool → Follow-up Draft Tool

Result:
Both tools were executed in sequence successfully.

Status: PASS

Edge-Case Test

Request:

Show me 2 leads with status purple.

There were no leads with the purple status in the dummy dataset.

The agent clearly reported that no leads with the requested status were found.

Status: PASS

Debugging:-

During Tool 2 testing, an input schema mismatch occurred.

The AI Agent provided the limit value as a string while the schema expected a number.

This resulted in an execution error.

Problem
Expected number, received string
Fix

The input handling was adjusted and the JavaScript code converts the value using:

Number($json.limit)

After the fix, the lead-search tool executed successfully.

This demonstrated the importance of matching tool schemas with the actual values produced by the AI Agent.

Error Handling:-

The tools use structured JSON responses for invalid or missing inputs.

Examples include:

Missing FAQ question
Missing lead status
Invalid or missing lead limit
Missing lead name

The goal is to avoid silent failures and provide predictable outputs that the agent can understand.

Safety:-

This project intentionally uses controlled tools.

Allowed Actions
Search FAQ information
Retrieve dummy leads
Generate follow-up message drafts
Restricted Actions

The agent does not have tools for:

Sending emails
Sending messages
Deleting data
Updating records
Performing irreversible actions

Any future sensitive or irreversible action should require human confirmation before execution.

Observability:-

n8n execution logs were used to inspect the agent's behaviour.

The logs help verify:

User request
Agent execution
Selected tool
Tool input
Tool output
Errors
Multi-step tool sequence

This makes it possible to understand what the agent actually did instead of evaluating only the final response.

Local Setup
Requirements:
n8n
Ollama
A locally available Ollama chat model
Web browser
Basic Setup
Start Ollama locally.
Start the local n8n instance.
Open the n8n editor.
Open the Project 4 workflow.
Ensure the Ollama Chat Model is connected to the AI Agent.
Ensure the three tools are connected to the AI Agent.
Open the chat interface.
Send a test request.

No external OpenAI API key is required for this local Ollama setup.

Screenshots:

The project includes practical evidence of the workflow and testing.

Architecture:

Practical Evidence

Screenshots used during development include evidence of:

Tool 1 FAQ execution
Tool 2 lead search execution
Tool 3 follow-up draft execution
Multi-step agent execution
Edge-case/error handling
Ollama connection debugging
Limitations

This project uses sample data and simplified tools.

Current limitations include:

The FAQ knowledge base is small and sample-based.
The lead dataset is dummy data.
The follow-up tool generates drafts only.
No real email or messaging system is connected.
No real CRM is connected.
The project does not perform irreversible actions.
The MCP implementation was studied conceptually and was not added as a separate implementation.

MCP Connection:-

As part of the project, I also learned the basic concept of Model Context Protocol (MCP).

Conceptually, one of the Project 4 tools could be exposed through an MCP Server.

AI Application
      ↓
  MCP Client
      ↓
  MCP Server
      ↓
 FAQ Search Tool
      ↓
 FAQ Knowledge Base

MCP provides a standardized interface for AI applications to interact with tools and resources.

The current n8n workflow does not require changes for this conceptual MCP learning task.

Lessons Learned:-

Through this project, I learned:

AI Agents can dynamically select tools based on user intent.
Clear tool descriptions improve tool selection.
Input schemas are important for reliable tool execution.
Tool outputs should be structured and predictable.
Agents can perform controlled multi-step tasks.
Execution logs are important for observability.
Error handling should be explicit.
Tool permissions should be limited to the required actions.
Irreversible actions should require human confirmation.
MCP provides a standard way for AI applications to work with tools and resources.

Project Status:

Status: Completed

The Project 4 AI Agent successfully demonstrates:

Multi-tool agent behaviour
Tool selection
Structured tool inputs and outputs
Multi-step execution
Error and edge-case handling
Safety boundaries
Execution observability
Basic MCP understanding

Repository Structure

project-4-agent/
├── README.md
├── .env.example
├── .gitignore
└── project-4-agent-architecture.png