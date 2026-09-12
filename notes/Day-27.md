# Day 27 – Safety, Errors & Observability

## Goal

The goal of Day 27 was to make the agent workflow safer, handle errors clearly, and inspect what the agent actually did through execution logs.

## Safety Rules

The Project 4 agent was designed with controlled actions.

### Allowed Actions

- Search the FAQ knowledge base
- Retrieve dummy leads by status
- Generate a follow-up message draft

### Not Allowed

The agent does not have tools for:

- Sending emails or messages
- Deleting data
- Updating records
- Performing irreversible actions

## Human Confirmation

Any action such as sending, deleting, or updating should require human confirmation before execution.

In the current workflow, these actions are not available because only read/search and draft-generation tools are connected.

## Observability

The n8n execution logs were inspected to understand the agent's behaviour.

The logs can show:

- User request
- AI Agent execution
- Selected tool
- Tool input
- Tool output
- Errors or failed executions

This makes it possible to inspect the agent's actions instead of checking only the final response.

## Error and Edge-Case Testing

An edge case was tested using an unsupported lead status.

### Test Request

> "Show me 2 leads with status purple."

There were no leads with the `purple` status.

### Result

The agent clearly responded that no leads with the requested status were found.

**Status:** PASS

The workflow handled the unsupported status without producing an incorrect lead result.

## API Failure Test

During the Project 4 setup, the Ollama connection initially produced a:

`fetch failed`

error.

The issue was investigated and the Ollama connection was fixed.

After the fix, the AI Agent executed successfully and was able to use the connected tools.

This demonstrated the importance of checking the underlying tool/API execution when an agent fails.

## Error Handling

The tools were designed to return structured error information when required input is missing or invalid.

Examples include:

- Missing FAQ question
- Missing lead status
- Invalid or missing lead limit
- Missing lead name for follow-up draft

This helps the agent handle problems without silently producing incorrect results.

## Key Learning

I learned that an AI Agent should not be judged only by its final answer.

Execution logs are important because they show:

1. What the user requested
2. Which tool the agent selected
3. What input was sent to the tool
4. What result the tool returned
5. Whether an error occurred

Safety controls are also important because tools should only be given the permissions required for their intended task.

## Day 27 Self-Check

- [x] Allowed actions identified
- [x] Unsafe/irreversible actions identified
- [x] Human confirmation requirement defined
- [x] Agent execution logs inspected
- [x] Edge case tested
- [x] API failure encountered and fixed
- [x] Tool errors and missing inputs handled
- [x] Final responses checked for clear error handling

## Evidence

Practical evidence includes screenshots of:

- Agent tool execution logs
- The unsupported `purple` status test
- The initial Ollama `fetch failed` error
- The successful execution after fixing the Ollama connection

## Conclusion

Day 27 was completed successfully. The agent workflow now includes safety boundaries, structured error handling, and execution-level observability.