# Day 24 — Build Tool 1 & Tool 2 Separately

## Goal

Build reliable tools before connecting an AI agent.

## What I Built

I created two independent tools inside the same n8n workflow:

1. Search FAQ
2. Get Test Leads

Both tools were tested without using AI.

---

## Tool 1 — Search FAQ

### Purpose

Search sample FAQ knowledge and return an answer for a user's question.

### Input

- `question`

### Output

- `answer`
- `found`

### Sample Test

Input:

`What is your refund policy?`

Output:

```json
{
  "answer": "Refunds are available within 7 days.",
  "found": true
}

Missing Input Test

When the question was missing, the tool returned:

{
  "answer": null,
  "found": false,
  "error": "Question is required."
}
Tool 1 Status
Normal test: Passed
FAQ matching: Passed
Missing input handling: Passed
Structured JSON response: Passed
Independent testing without AI: Passed


Tool 2 — Get Test Leads
Purpose

Retrieve dummy/test leads based on lead status and limit.

Input
status
limit
Output
leads
count
Sample Test

Input:

{
  "status": "warm",
  "limit": 3
}

Output contained three warm test leads:

L002 — Priya
L004 — Sneha
L005 — Vikas

The returned count was 3.

Missing Input Test

When the status input was missing, the tool returned:

{
  "leads": [],
  "count": 0,
  "error": "Status is required."
}
Tool 2 Status
Normal test: Passed
Status filtering: Passed
Limit handling: Passed
Missing input handling: Passed
Structured JSON response: Passed
Independent testing without AI: Passed
Important Learning

Tools should be reliable and independently tested before connecting them to an AI agent.

Clear inputs, structured outputs, and missing-input handling make tools easier for an agent to use correctly.