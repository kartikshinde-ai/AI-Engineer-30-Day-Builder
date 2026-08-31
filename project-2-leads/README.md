# Project 2 - AI Lead Automation

## 1. Project Overview

This project is an AI-assisted lead management system built using n8n, AI, JavaScript and Google Sheets.

The system has two separate workflows:

1. Lead Processing Workflow
2. Follow-up Workflow

The first workflow processes new leads and prepares an AI-assisted response.

The second workflow checks existing leads and identifies leads that need follow-up.

Human approval is kept in the process before the final action.

---

# 2. Problem

Managing leads manually requires repeated work such as:

- Reading lead information
- Understanding the lead's requirement
- Classifying the lead
- Assigning priority
- Preparing a response
- Checking follow-up dates
- Updating lead records

This project automates most of these repetitive tasks while keeping human approval where required.

---

# 3. Workflow 1 - Lead Processing

## Step 1 - Create the Webhook

The workflow starts with a Webhook node.

The Webhook receives the lead information and starts the automation.

### Node

`Webhook`

---

## Step 2 - Prepare Lead Data

An Edit Fields node is used after the Webhook.

This prepares and organizes the incoming lead information before processing.

### Node

`Edit Fields`

---

## Step 3 - Add Initial Condition

An If node is added to check whether the lead should continue through the workflow.

### Node

`If`

The True branch continues the lead-processing workflow.

---

## Step 4 - Send Data to AI Processing

An HTTP Request node is used to send the prepared lead information for AI processing.

### Node

`HTTP Request`

---

## Step 5 - Process the AI Response

A JavaScript Code node is used to process and structure the response.

### Node

`Code in JavaScript`

---

## Step 6 - Continue AI Processing

Another HTTP Request node is used for the next AI-processing step.

### Node

`HTTP Request1`

---

## Step 7 - Structure the Result

Another JavaScript Code node processes the returned information and prepares the required fields.

### Node

`Code in JavaScript1`

---

## Step 8 - Create the Final AI Output

A final JavaScript Code node prepares the information required for storing the lead.

### Node

`Code in JavaScript2`

---

## Step 9 - Store the Lead in Google Sheets

The processed lead information is added to Google Sheets.

### Node

`Append row in sheet`

The sheet stores information such as:

- Name
- Course interest
- Message
- City
- Timeline
- Category
- Priority
- Reason
- Recommended next action
- Draft reply
- Status
- Human approval
- Follow-up information

---

## Step 10 - Wait for Human Approval

A Wait node is used so that the workflow can wait for the human approval decision.

### Node

`Wait`

Human approval prevents the system from taking the final action automatically.

---

## Step 11 - Check Approval Decision

An If node checks the approval decision.

### Node

`If1`

The workflow has two possible paths:

- True → Approved
- False → Not approved

The approved path continues to update the lead record.

---

# 4. Workflow 2 - Follow-up Automation

The follow-up workflow is kept as a separate workflow.

It is NOT directly connected to Workflow 1.

---

## Step 1 - Schedule Trigger

The workflow starts automatically using a Schedule Trigger.

### Node

`Schedule Trigger`

This allows the follow-up process to run on a schedule.

---

## Step 2 - Read Leads from Google Sheets

A Google Sheets node reads the existing lead records.

### Node

`Get row(s) in sheet`

This provides the current lead data to the workflow.

---

## Step 3 - Create Lead Summary

A JavaScript Code node processes the lead records and creates a summary.

### Node

`Create Lead Summary`

The summary contains information such as:

- Total leads
- Hot leads
- Leads by course
- Leads awaiting follow-up

---

## Step 4 - Check Follow-up Date

An If node checks whether a lead requires follow-up.

### Node

`If2`

The workflow checks the follow-up date against the current date.

If follow-up is required, the lead continues through the True branch.

---

## Step 5 - Prepare Follow-up

A JavaScript Code node prepares the follow-up information.

### Node

`Prepare Follow-Up`

It prepares the information that needs to be updated for the lead.

---

## Step 6 - Update Google Sheets

The final Google Sheets node updates the lead record.

### Node

`Append or update row in sheet2`

This updates information such as:

- Follow-up status
- Follow-up reason
- Last contact date
- Next follow-up date
- Other required lead information

---

# 5. Complete Workflow Structure

## Workflow 1

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
Code in JavaScript2  
↓  
Append row in sheet  
↓  
Wait  
↓  
If1  
↓  
Approved / Not Approved  
↓  
Update Google Sheet

---

## Workflow 2

Schedule Trigger  
↓  
Get row(s) in sheet  
↓  
Create Lead Summary  
↓  
If2  
↓  
Prepare Follow-Up  
↓  
Append or update row in sheet2

---

# 6. Why Two Separate Workflows?

The two workflows are intentionally kept separate.

The first workflow handles new lead processing and approval.

The second workflow handles scheduled follow-up checking.

Keeping them separate makes the automation easier to understand, maintain and control.

---

# 7. Business Value

This automation can help a business:

- Reduce repetitive manual work
- Process leads faster
- Classify leads consistently
- Identify high-priority leads
- Generate draft responses
- Track follow-ups
- Keep lead information organized
- Keep humans involved in important decisions

---

# 8. Human Approval

The system is AI-assisted, not completely autonomous.

AI prepares the classification, recommendation and draft response.

Human approval remains in the workflow before the final action.

This reduces the risk of an incorrect automated decision.

---

# 9. Risks and Limitations

### Wrong Classification

AI may incorrectly classify a lead or assign the wrong priority.

### Privacy

Lead information must be handled securely and only used when necessary.

### Over-Automation

Automation should not completely remove human control from important decisions.

### AI Accuracy

AI-generated recommendations and draft replies should be reviewed when necessary.

---

# 10. Data Stored in Google Sheets

The project stores lead information including:

- Name
- Course interest
- Message
- City
- Timeline
- Category
- Priority
- Reason
- Recommended next action
- Draft reply
- Status
- Human approval
- Next follow-up date
- Last contact date
- Follow-up required
- Follow-up reason

---

# 11. Tools Used

- n8n
- Google Sheets
- AI
- JavaScript
- Webhook
- HTTP Request

---

# 12. Project Outcome

The final project demonstrates how AI and workflow automation can be combined to manage leads.

The system can process incoming leads, generate useful AI-assisted information, store the results, wait for human approval and run a separate scheduled follow-up process.

The main goal is not only automation, but using AI to reduce repetitive work while keeping human control.

---

# 13. Demo Flow

For the project demonstration:

1. Show the incoming lead.
2. Show the lead-processing workflow.
3. Show the AI-generated classification and draft reply.
4. Show the Google Sheet record.
5. Show the human approval step.
6. Show the separate follow-up workflow.
7. Show how follow-up information is checked and updated.

---

# 14. Project Learning

Through this project, I learned how to:

- Build multi-step workflows in n8n
- Connect AI processing with automation
- Work with Webhooks
- Use HTTP Requests
- Process data using JavaScript
- Store and update data in Google Sheets
- Add human approval to an automation
- Build scheduled follow-up automation
- Think about business value, risks and limitations of AI automation

# 15. Screenshots

## Main Lead Approval Workflow

![Main Lead Approval Workflow](screenshoot/Main%20Lead%20Approval%20Workflow.png)

## Follow-up Workflow

![Follow-up Workflow](screenshoot/Separate%20Follow-Up%20Workflow.png)

## Google Sheets Result

![Google Sheets Result](screenshoot/Google%20Sheets%20Final%20Result.png)