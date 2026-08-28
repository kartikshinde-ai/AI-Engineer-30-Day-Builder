# Day 15 – AI Lead Automation with Approval & Follow-Up Workflow

## Objective

Today I completed and tested the AI Lead Automation workflow using n8n, Google Sheets, AI processing and a separate scheduled follow-up workflow.

The main goal was to automate the lead handling process from lead submission to AI-generated response, human approval and follow-up tracking.

---

## 1. Main Lead Approval Workflow

The first workflow handles incoming leads and processes them through multiple stages.

### Workflow Flow

Webhook
→ Edit Fields
→ If
→ HTTP Request
→ Code in JavaScript
→ HTTP Request
→ Code in JavaScript
→ Code in JavaScript2
→ Append row in sheet
→ Wait
→ If
→ Approved / Not Approved
→ Update corresponding Google Sheet row

### What happens in this workflow?

1. A lead is received through the Webhook.
2. Edit Fields prepares the required lead information.
3. The If node checks the required condition before continuing.
4. HTTP Request nodes communicate with the local/API service used in the workflow.
5. JavaScript Code nodes process and prepare the data.
6. The processed lead is stored in Google Sheets.
7. The workflow reaches the Wait node for human approval.
8. The approval decision is checked using the If node.
9. If the lead is approved, the workflow continues through the approval branch.
10. The Google Sheet is updated with the approval information.

---

## 2. Human Approval

A major part of this workflow is the Human Approval step.

The workflow does not automatically assume that every AI-generated response should be sent or processed.

Instead, it pauses at the Wait node.

The approval information contains fields such as:

- Approval Decision
- submittedAt
- formMode

The If node checks the Approval Decision.

For example:

Approved
→ Continue with the approved branch

This creates a human-in-the-loop automation system.

---

## 3. Google Sheets Integration

Google Sheets is used as the central data store for the lead information.

The sheet contains fields such as:

- name
- course_interest
- message
- city
- timeline
- category
- priority
- reason
- recommended_next_step
- draft_reply
- status
- human_approved
- next_followup_date
- last_contact_date
- follow_up_required
- follow_up_reason

The workflow reads and writes lead information directly to the sheet.

---

## 4. Separate Follow-Up Workflow

The follow-up automation is kept as a separate workflow.

It is NOT directly connected to the main Lead Approval Workflow.

### Follow-Up Workflow

Schedule Trigger
→ Get row(s) in sheet
→ Create Lead Summary
→ If2
→ Prepare Follow-Up
→ Append or Update Row in Sheet2

---

## 5. Schedule Trigger

The Follow-Up Workflow starts using a Schedule Trigger.

This means the workflow can automatically run at the scheduled time without requiring the main lead workflow to start it.

The Schedule Trigger gets the current lead data from Google Sheets.

---

## 6. Create Lead Summary

The Create Lead Summary node processes the rows received from Google Sheets.

During testing, the workflow processed multiple lead items and generated summary information such as:

- total_leads
- hot_leads
- by_course
- awaiting_follow_up

This gives the follow-up workflow structured information that can be used for further processing.

---

## 7. Follow-Up Date Condition

The If2 node checks whether the follow-up date is due.

The condition compares the lead's `next_followup_date` with the current date.

The important logic is:

If the lead's follow-up date is today's date
→ True branch

Otherwise
→ False branch

During testing, the condition initially went to the False branch because the test date did not match the current date.

After correcting the test data/date and executing the workflow again, the condition correctly went to the True branch.

---

## 8. Prepare Follow-Up

When the If2 condition is True, the lead moves to the Prepare Follow-Up node.

This node prepares the required follow-up information for the lead.

The prepared data is then passed to the Google Sheets update node.

---

## 9. Append or Update Row in Sheet2

The final step of the follow-up workflow is:

`Append or Update Row in Sheet2`

This node stores the prepared follow-up information back into Google Sheets.

The row is matched using the `name` column.

The test execution successfully processed the lead data through this node.

---

## 10. Testing and Debugging

During today's testing, I faced an issue where the If2 node was sending the data to the False branch.

### Problem

The condition was comparing:

`next_followup_date`

with:

`today's date`

The test data did not initially match the expected date format/value.

### Debugging

I checked:

- Google Sheets data
- next_followup_date
- current date
- If2 condition
- True/False branches
- output data

I corrected the test date and executed the workflow again.

### Result

The If2 node correctly sent the data to the True branch.

The data then successfully passed through:

`Prepare Follow-Up`

and

`Append or Update Row in Sheet2`

---

## 11. Final Architecture

There are two independent workflows.

### Workflow 1 – Lead Approval

Webhook
→ Lead Processing
→ AI/API Processing
→ Google Sheets
→ Wait for Human Approval
→ Approval Decision
→ Google Sheets Update

### Workflow 2 – Follow-Up Automation

Schedule Trigger
→ Read Google Sheets
→ Create Lead Summary
→ Check Follow-Up Date
→ Prepare Follow-Up
→ Update Google Sheets

The two workflows remain separate.

The Follow-Up Workflow does not need to be directly connected to the Lead Approval Workflow because it independently reads the latest data from Google Sheets on its scheduled execution.

---

## 12. What I Learned Today

### Human-in-the-loop Automation

I understood how an automation can pause and wait for a human decision before continuing.

### Conditional Logic

I learned how an If node can control workflow execution based on data conditions.

### Date-Based Automation

I understood how a follow-up workflow can compare a stored follow-up date with the current date and decide whether a lead requires follow-up.

### Google Sheets as a Data Store

I understood how different workflows can use the same Google Sheet as a shared source of information without directly connecting the workflows.

### Debugging

I learned that when an If node goes to the wrong branch, I should first inspect the actual input value, data type and condition rather than assuming the node itself is broken.

---

## 13. Final Result

Today I completed and tested the AI Lead Automation system.

The system now demonstrates:

- Lead capture
- Lead processing
- AI/API-based processing
- Google Sheets storage
- Human approval
- Approval-based branching
- Scheduled follow-up checking
- Date-based conditional logic
- Follow-up preparation
- Google Sheets update

The main Lead Approval Workflow and Follow-Up Workflow are intentionally kept as separate workflows.

---

## 14. Key Takeaway

The important concept I understood today is that automation does not always need to be one large connected workflow.

A better architecture can use separate workflows that communicate through a shared data source such as Google Sheets.

The first workflow handles lead processing and approval, while the second workflow independently checks the stored lead data and handles follow-ups based on the scheduled date.