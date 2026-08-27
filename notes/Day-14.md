# Day 14 — AI Lead Automation with Human Approval

## 1. Today's Goal

The main goal of Day 14 was to complete and publish the AI Lead Automation workflow with a human approval step.

The workflow performs the following tasks:

- Receives lead information through a Webhook.
- Processes and classifies the lead using AI.
- Stores the lead information in Google Sheets.
- Waits for human approval.
- Checks whether the lead is approved or rejected.
- Updates the existing Google Sheets row accordingly.
- Tests both approval cases.
- Publishes the final workflow.

---

## 2. Final Workflow

```text
Webhook
   ↓
Edit Fields
   ↓
If
   ↓
HTTP Request
   ↓
Code in JavaScript
   ↓
HTTP Request1
   ↓
Code in JavaScript1
   ↓
Append row in sheet
   ↓
Wait
   ↓
If1
   ├── True → Append or update row in sheet
   │
   └── False → Append or update row in sheet1

3. Google Sheets Integration

The workflow stores lead information in a Google Sheet.

The sheet contains the following columns:

name
course_interest
message
city
timeline
category
priority
reason
recommended_next_action
draft_reply
status
human_approved

The lead information is first added to the sheet before the workflow waits for human approval.

4. Removing the Create Spreadsheet Node

Initially, the workflow contained a Create spreadsheet node.

However, the spreadsheet was already available, so creating a new spreadsheet during the workflow was unnecessary.

Therefore, the connection to the Create spreadsheet node was removed and the node was kept disconnected.

The workflow was changed to:

Code in JavaScript1
        ↓
Append row in sheet
        ↓
Wait

This simplified the workflow and avoided unnecessary spreadsheet creation.


5. Human Approval using Wait Node

The Wait node is used to pause the workflow until a human submits the approval form.

The form is called:

Lead Approval Review

The purpose of the form is to review the AI-generated lead classification and draft reply before taking further action.

The human reviewer can select:

APPROVED
REJECTED

After submitting the form, the workflow continues from the Wait node.


6. Approval Decision using If1

After the Wait node, the workflow uses the If1 node to check the human approval decision.

The workflow has two branches.

True Branch — Approved
If1 → True
     ↓
Append or update row in sheet

When the lead is approved:

status = APPROVED
human_approved = Yes

The existing lead row is updated in Google Sheets.

False Branch — Rejected
If1 → False
     ↓
Append or update row in sheet1

When the lead is rejected:

status = REJECTED
human_approved = No

The existing lead row is updated in Google Sheets.


7. Append or Update Row

The Append or Update Row operation is used after human approval.

The name column is used as the matching column.

This allows the workflow to find the existing lead and update its information instead of unnecessarily creating another row.

For example:

Before approval:
status = NEW

After approval:
status = APPROVED
human_approved = Yes

For rejection:

Before rejection:
status = NEW

After rejection:
status = REJECTED
human_approved = No


8. Testing

The workflow was tested with both possible human decisions.

Test 1 — Approved

The approval form was submitted with:

APPROVED

The Google Sheet was successfully updated:

status = APPROVED
human_approved = Yes
Test 2 — Rejected

The approval form was submitted with:

REJECTED

The Google Sheet was successfully updated:

status = REJECTED
human_approved = No

Both cases were successfully tested.


9. Troubleshooting

During testing, a Google Sheets connection error occurred:

The connection cannot be established,
this usually occurs due to an incorrect host (domain) value

The error showed:

getaddrinfo ENOTFOUND sheets.googleapis.com

Network/DNS connectivity was checked separately.

The connection was later working again, and the workflow was successfully executed.


10. Final Cleanup

Before publishing the workflow:

Removed the unnecessary spreadsheet creation connection.
Connected Code in JavaScript1 directly to Append row in sheet.
Verified the Wait node.
Verified the If1 approval branches.
Verified the Google Sheets update nodes.
Tested both Approved and Rejected cases.
Confirmed that the workflow executed successfully.


11. Final Workflow Status

The workflow was successfully published.

Final automation:

Lead Submission
      ↓
AI Processing
      ↓
Lead Classification
      ↓
Google Sheets
      ↓
Human Approval
      ↓
Approved / Rejected
      ↓
Google Sheets Update

This creates a complete human-in-the-loop AI lead automation workflow.   