# AI Lead Classification Output

The AI should return a structured JSON object for every lead.

## Required Fields

### category
The course category:
- SOC
- Desktop
- VAPT
- Other

### priority
The lead priority:
- Hot
- Warm
- Cold

### reason
A short explanation of why the lead received this category and priority.

### recommended_next_action
The next action that should be taken for the lead.

Examples:
- Contact immediately
- Send course details
- Follow up later
- Ask for more information

### draft_reply
A short professional reply that can be sent to the lead.

## Example

```json
{
  "category": "SOC",
  "priority": "Hot",
  "reason": "The lead is interested in SOC Analyst training and wants to start within one month.",
  "recommended_next_action": "Contact immediately",
  "draft_reply": "Thank you for your interest in our SOC Analyst training. We can share the course details and enrollment information with you."
}