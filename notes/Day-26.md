# Day 26 – Add Tool 3 + Multi-Step Task

## Goal

The goal of Day 26 was to add a third tool to the AI Agent and test a controlled multi-step task where the agent uses more than one tool in sequence.

## Tool 3 – Generate Follow-up Draft

A third tool was added to the AI Agent.

**Purpose:**  
Generate a follow-up message draft for a selected lead.

**Input:**
- `lead_name`

**Output:**
- `lead_name`
- `draft`
- `error` when the lead name is missing

The tool only generates a draft. It does not send any message.

## Multi-Step Task

The following user request was tested:

> "Show me warm leads and prepare a follow-up draft for one of them."

The agent needed to perform two tool calls.

### Tool Call Sequence

1. **Get Dummy Leads by Status**
   - Filter leads by `warm` status.
   - Return the matching leads.

2. **Generate Follow-up Draft**
   - Select one of the returned leads.
   - Generate a follow-up message draft for that lead.

### Flow

User Request
→ Get Warm Leads
→ Observe Lead Results
→ Select One Lead
→ Generate Follow-up Draft
→ Final Response

## Test Result

The multi-step request executed successfully.

The execution log showed two tool calls:

1. `Get dummy leads filtered by status`
2. `Generate a follow-up message draft for a selected lead`

**Status:** PASS

## Safety Control

The follow-up tool is intentionally limited to creating a draft.

It does not:
- Send an email
- Send a message
- Delete data
- Update lead records
- Perform any irreversible action

This keeps the multi-step workflow controlled and safe.

## Observability

The n8n execution log was inspected to verify the order of tool calls.

This confirmed that the agent first retrieved the leads and then used the result to generate the follow-up draft.

## Tool-Call Limit

A separate maximum tool-call limit was not added because this control is optional in the Day 26 requirements. The workflow remains limited to the tools and actions explicitly connected to the agent.

## Key Learning

I learned that an AI Agent can perform a multi-step task by using the output of one tool as context for the next tool.

The important part is to keep each tool focused on one responsibility and prevent tools from performing irreversible actions.

## Day 26 Self-Check

- [x] Third tool added
- [x] Tool 3 tested successfully
- [x] Multi-step task tested
- [x] Multiple tool calls observed in the execution log
- [x] Tool-call sequence verified
- [x] Follow-up action remains draft-only
- [x] No irreversible action is available

## Evidence

A screenshot of the successful multi-step execution is available as practical evidence.

## Conclusion

Day 26 was completed successfully. The AI Agent can now perform a controlled multi-step task by using multiple tools in sequence.