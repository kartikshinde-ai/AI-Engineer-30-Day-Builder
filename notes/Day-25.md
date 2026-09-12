# Day 25 – Connect the Agent to Tools

## Goal

The goal of Day 25 was to connect the AI Agent with multiple tools and allow the model to select the correct tool based on the user's request.

## What I Understood

A tool-using agent is different from a fixed workflow.

In a fixed workflow, the steps are predefined and execute in a specific order.

In an agent workflow, the AI Agent receives the user's request, decides which tool is appropriate, executes that tool, observes the result, and then generates the final response.

### Agent Loop

User Request
→ Agent understands the goal
→ Selects the appropriate tool
→ Executes the tool
→ Observes the result
→ Generates the final answer

## Platform Used

- n8n
- Ollama (local LLM)
- n8n AI Agent
- Code Tools

## Tools Connected to the Agent

### Tool 1 – Search FAQ Knowledge Base

**Purpose:**  
Search the sample FAQ knowledge base and return the matching answer.

**Input:**
- `query`

**Output:**
- `answer`
- `found`
- `error` when required input is missing

---

### Tool 2 – Get Dummy Leads by Status

**Purpose:**  
Retrieve dummy leads filtered by status.

**Input:**
- `status`
- `limit`

**Output:**
- `leads`
- `count`
- `error` when the input is invalid

---

### Tool 3 – Generate Follow-up Draft

**Purpose:**  
Generate a follow-up message draft for a selected lead.

**Input:**
- `lead_name`

**Output:**
- `lead_name`
- `draft`
- `error` when the lead name is missing

This tool only creates a draft. It does not send any message.

## Tool Descriptions

Clear tool descriptions were added so that the AI Agent could understand when each tool should be used.

The descriptions specify:
- What the tool does
- When the tool should be used
- What input the tool expects
- What type of task the tool is suitable for

## Testing

The agent was tested with different user requests to verify tool selection.

### Test 1 – FAQ Request

**User request:**
"What is your refund policy?"

**Expected tool:** Tool 1 – Search FAQ Knowledge Base

**Result:**  
The AI Agent selected the FAQ tool and returned the refund policy successfully.

**Status:** PASS

---

### Test 2 – Lead Search

**User request:**
"Show me 2 warm leads."

**Expected tool:** Tool 2 – Get Dummy Leads by Status

**Result:**  
The AI Agent selected the lead tool and returned two warm leads successfully.

**Status:** PASS

---

### Test 3 – Follow-up Draft

**User request:**
"Prepare a follow-up draft for Priya."

**Expected tool:** Tool 3 – Generate Follow-up Draft

**Result:**  
The AI Agent selected the draft tool and generated a follow-up message for Priya.

**Status:** PASS

## Debugging and Fix

While testing Tool 2, the agent initially provided the `limit` value as a string while the schema expected a number.

The tool execution failed because of the schema mismatch.

### Error

`Expected number, received string`

### Fix

The input schema was adjusted to accept the value in the format used by the agent, while the JavaScript code converts the value using:

`Number($json.limit)`

After the fix, the tool executed successfully.

## Observability

The n8n execution logs were used to inspect:
- User request
- Selected tool
- Tool input
- Tool execution
- Tool output

This made it possible to verify what the agent actually did instead of looking only at the final response.

## Key Learning

I learned that connecting tools to an AI Agent is not only about making the tools work. The agent must also have clear descriptions and input schemas so that it can select and use the correct tool.

A well-defined tool makes agent behaviour more predictable and easier to debug.

## Day 25 Self-Check

- [x] Agent connected to multiple tools
- [x] Clear tool descriptions added
- [x] Agent selected the expected tools during testing
- [x] Tool inputs and outputs were verified
- [x] Tool selection and execution were inspected through logs
- [x] A schema mismatch was identified and fixed

## Evidence

Screenshots of the successful Tool 1, Tool 2 and Tool 3 executions are available as practical evidence.

## Conclusion

Day 25 was completed successfully. The AI Agent can now select and use the appropriate tool based on the user's request instead of following only a fixed sequence.