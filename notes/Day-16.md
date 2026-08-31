# Day 16 - Demo Project 2 + Business Thinking

## Goal

Learn to explain the business value of an AI-assisted workflow, not only the technology.

---

## Project 2 - AI Lead Automation

Today I completed and documented Project 2, an AI-assisted lead automation workflow built using n8n, AI, JavaScript and Google Sheets.

The project contains two separate workflows:

1. Lead Processing Workflow
2. Follow-up Workflow

The two workflows are intentionally kept separate.

---

## 1. Lead Processing Workflow

The main workflow starts when a new lead is received through a Webhook.

### Flow

Webhook  
→ Edit Fields  
→ If  
→ HTTP Request  
→ Code in JavaScript  
→ HTTP Request1  
→ Code in JavaScript1  
→ Code in JavaScript2  
→ Append row in sheet  
→ Wait  
→ If1  
→ Approved / Not Approved  
→ Google Sheets update

### What the workflow does

- Receives lead information
- Prepares the input data
- Processes the lead using AI
- Classifies the lead
- Assigns priority
- Generates a reason and recommended next action
- Creates a draft reply
- Stores the information in Google Sheets
- Waits for human approval
- Continues based on the approval decision

---

## 2. Human Approval

Human approval is kept inside the workflow.

The AI prepares the classification, recommendation and draft response, but the final action is not completely autonomous.

The workflow waits for a human approval decision before continuing.

This helps reduce the risk of incorrect automated actions.

---

## 3. Follow-up Workflow

The follow-up process is a separate workflow.

### Flow

Schedule Trigger  
→ Get row(s) in sheet  
→ Create Lead Summary  
→ If2  
→ Prepare Follow-Up  
→ Append or update row in sheet2

### What the workflow does

- Runs on a schedule
- Reads existing leads from Google Sheets
- Creates a summary of the leads
- Checks follow-up information
- Identifies leads requiring follow-up
- Prepares follow-up information
- Updates the lead record in Google Sheets

---

## 4. Why Two Separate Workflows?

The two workflows are kept separate because they have different purposes.

The first workflow handles:

- New lead processing
- AI-assisted classification
- Draft response
- Human approval

The second workflow handles:

- Scheduled checking
- Follow-up identification
- Follow-up updates

This makes the automation easier to understand, maintain and control.

---

## 5. Business Value

The automation can help reduce repetitive manual work.

It can help a business:

- Process leads faster
- Classify leads consistently
- Identify high-priority leads
- Generate draft responses
- Track follow-ups
- Keep lead information organized
- Reduce repetitive work
- Keep humans involved in important decisions

The main value is not only using AI, but reducing manual work while keeping human control.

---

## 6. What Manual Work Is Reduced?

Before automation, a person may need to:

- Read every lead manually
- Understand the lead's requirement
- Decide the lead category
- Decide the priority
- Prepare a response
- Check follow-up dates
- Update the lead record

The workflow automates much of this repetitive work.

Human approval is still retained for important decisions.

---

## 7. Data Stored

Google Sheets stores lead information such as:

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

## 8. Risks and Limitations

### 1. Wrong Classification

AI may incorrectly classify a lead or assign the wrong priority.

### 2. Privacy

Lead information should be handled securely and only used when necessary.

### 3. Over-Automation

Important decisions should not be completely automated without appropriate human control.

### 4. AI Accuracy

AI-generated recommendations and draft replies may require human review.

---

## 9. Tools Used

- n8n
- AI
- JavaScript
- Google Sheets
- Webhook
- HTTP Request

---

## 10. Screenshots

### Main Lead Approval Workflow

![Main Lead Approval Workflow](screenshots/01-main-lead-workflow.png)

### Follow-up Workflow

![Follow-up Workflow](screenshots/02-follow-up-workflow.png)

### Google Sheets Result

![Google Sheets Result](screenshots/03-google-sheets-result.png)

---

## 11. Project Outcome

I completed an AI-assisted lead management system that connects AI processing, workflow automation and Google Sheets.

The system can:

1. Receive a lead
2. Process and classify the lead
3. Generate a recommended action and draft reply
4. Store the information
5. Wait for human approval
6. Run a separate scheduled follow-up process
7. Update follow-up information

---

## 12. Day 16 Learning

Today I learned that building an AI workflow is not only about connecting tools.

It is also important to understand:

- What business problem the workflow solves
- What manual work it reduces
- Where human approval is required
- What data is stored
- What risks and limitations exist
- How to explain the workflow in simple business language

### Key takeaway

AI automation should reduce repetitive work while keeping appropriate human control.