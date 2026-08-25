# Day 12 - Project 2 - Create the Classification Prompt

## Goal

Make the LLM produce predictable structured results for lead classification.

## Understand

- System instruction
- Classification examples
- Structured JSON output
- Avoiding unsupported assumptions
- Comparing expected output with actual model output

## Today's Tasks

- Created Classification Prompt v1.
- Defined the system instruction for lead classification.
- Defined category labels: SOC, Desktop, VAPT and Other.
- Defined priority labels: Hot, Warm and Cold.
- Added rules for classification and priority.
- Added 3 input/output examples.
- Added rules to prevent the model from inventing unsupported information.
- Defined structured JSON output fields:
  - category
  - priority
  - reason
  - recommended_next_action
  - draft_reply
- Tested the prompt on 10 dummy leads.
- Compared the model output with the expected classification.

## Prompt Safety Rules

The model must classify leads only using the provided:

- Name
- Course interest
- Message
- City
- Timeline

The model must not invent:

- Phone number
- Salary
- Budget
- Job status
- Experience
- Location details
- Any other personal or business fact

## Test Result

The classification prompt was tested on 10 dummy leads using the Ollama `llama3.2:3b` model.

Result:

10/10 dummy leads were classified successfully with structured JSON output.

### Classification Results

| Lead | Category | Priority | Result |
|---|---|---|---|
| Amit Sharma | SOC | Hot | PASS |
| Rahul Patil | Desktop | Warm | PASS |
| Sneha Joshi | VAPT | Warm | PASS |
| Rohit More | Other | Cold | PASS |
| Priya Deshmukh | SOC | Hot | PASS |
| Akash Pawar | Desktop | Hot | PASS |
| Neha Kulkarni | VAPT | Hot | PASS |
| Vikas Shinde | SOC | Cold | PASS |
| Pooja Patil | Other | Cold | PASS |
| Sagar Jadhav | VAPT | Hot | PASS |

## Output Structure

Each classified lead produces structured JSON containing:

- category
- priority
- reason
- recommended_next_action
- draft_reply

## What I Learned

- A clear system instruction helps control LLM behaviour.
- Examples make the expected classification pattern clearer.
- Structured JSON makes the AI output easier to use in an automation workflow.
- Explicit rules help prevent the model from inventing missing lead information.
- Testing multiple dummy leads helps verify whether the prompt behaves consistently.

## Day 12 Status

- Prompt v1: COMPLETE
- 3 Examples: COMPLETE
- Structured JSON output: COMPLETE
- Unsupported-assumption rules: COMPLETE
- 10 Dummy Lead Tests: COMPLETE
- Test Result: 10/10 PASS

## Self-Check

Day 12 self-check questions and answers are documented separately.

## Deliverables

- `project-2-leads/classification_prompt.md`
- `project-2-leads/test-results.md`
- `notes/Day-12.md`