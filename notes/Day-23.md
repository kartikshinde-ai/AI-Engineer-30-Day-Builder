# Day 23 — Project 4: Understand Tool-Using Agents

## Goal

Understand how a tool-using AI agent can move from a fixed workflow to controlled agent decisions.

## Agent Loop

The basic agent loop is:

Goal → Choose Tool → Execute → Observe → Answer

An AI agent first understands the user's goal, chooses the appropriate tool, executes it, observes the result, and then provides an answer.

## Fixed Workflow vs AI Agent

A fixed n8n workflow follows a predefined sequence of steps.

Example:

Trigger → Node 1 → Node 2 → Node 3 → Output

An AI agent can choose which tool to use based on the user's request and the available tool descriptions.

Example:

User Goal → Choose Tool → Execute → Observe → Answer

## Tool Definitions

### Tool 1 — Search FAQ

Purpose:

Search the FAQ knowledge for an answer to a user's question.

Accepts:

- `question` — user's question

Returns:

- `answer` — matching FAQ answer
- `found` — true or false

---

### Tool 2 — Get Test Leads

Purpose:

Retrieve dummy/test leads based on their status.

Accepts:

- `status` — lead status such as hot, warm, or cold
- `limit` — maximum number of leads to return

Returns:

- `leads` — matching test leads
- `count` — number of leads found

---

### Tool 3 — Create Follow-Up Draft

Purpose:

Create a follow-up message draft for a selected lead.

Accepts:

- `lead_name` — name of the test lead
- `lead_context` — relevant context about the lead

Returns:

- `draft` — follow-up message draft

The tool only creates a draft. It does not automatically send messages or emails.

## 10 Routing Examples

| # | User Request | Selected Tool |
|---|---|---|
| 1 | What is your refund policy? | Search FAQ |
| 2 | How can I reset my password? | Search FAQ |
| 3 | What are your support hours? | Search FAQ |
| 4 | Show me all hot leads. | Get Test Leads |
| 5 | Find 5 warm leads. | Get Test Leads |
| 6 | Show me the latest cold leads. | Get Test Leads |
| 7 | Create a follow-up draft for Rahul. | Create Follow-Up Draft |
| 8 | Prepare a follow-up message for this lead. | Create Follow-Up Draft |
| 9 | Write a follow-up draft based on this lead's enquiry. | Create Follow-Up Draft |
| 10 | Find warm leads and show me up to 3. | Get Test Leads |

## Agent Architecture

The Project 4 agent architecture follows:

User
→ Agent
→ Tool Selection
→ Available Tools
→ Execute Tool
→ Observe Result
→ Final Answer

Available tools:

- Search FAQ
- Get Test Leads
- Create Follow-Up Draft

Architecture diagram:

`project-4-agent/project-4-agent-architecture.png`

## What I Understood

A fixed workflow follows a predefined sequence.

A tool-using agent can decide which available tool is appropriate for a user's request.

The agent can use the result of a tool to form its final answer.

## Self-Check

### Q1. What is the basic agent loop?

Answer:

Goal → Choose Tool → Execute → Observe → Answer

### Q2. What is the difference between a fixed workflow and an AI agent?

Answer:

A fixed workflow follows a predefined sequence of steps, while an AI agent can choose the appropriate tool based on the user's request.

### Q3. What are the three tools defined for Project 4?

Answer:

1. Search FAQ
2. Get Test Leads
3. Create Follow-Up Draft

### Q4. Can the Create Follow-Up Draft tool automatically send a message?

Answer:

No. It only creates a follow-up draft.

## Day Completion

Day 23 completed.

Completed:

- 3 tool definitions
- 10 routing examples
- Agent architecture diagram
- Agent loop understanding
- Fixed workflow vs AI agent understanding