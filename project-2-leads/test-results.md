# Lead Classification Test Results

## Test 1

**Lead:** Amit Sharma  
**Input:** SOC Analyst, wants to learn SOC and start career soon, Pune, 1 month

**Expected Output:**
- Category: SOC
- Priority: Hot

**Actual Output:**
{
  "category": "SOC",
  "priority": "Hot",
  "reason": "The lead is interested in SOC and wants to start soon.",
  "recommended_next_action": "Contact the lead and provide SOC course information.",
  "draft_reply": "Thanks for your interest in SOC Analyst training. We can share the relevant course information with you."
}

**Result:** PASS

## Test 2

**Lead:** Rahul Patil

**Input:** Desktop Support, wants to learn desktop support for an entry-level job, Nashik, 2 months

**Expected Output:**

- Category: Desktop
- Priority: Warm

**Actual Output:**

{
  "category": "Desktop",
  "priority": "Warm",
  "reason": "The lead is interested in Desktop Support but has a two-month timeline.",
  "recommended_next_action": "Share Desktop Support course information and follow up later.",
  "draft_reply": "Thanks for your interest in Desktop Support. We can share the relevant course information with you."
}

**Result:** PASS

## Ollama Classification Run

Tested the first 10 dummy leads using `classify_leads.py`
with the `llama3.2:3b` Ollama model.

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

### Run Result

10/10 dummy leads were classified successfully with structured JSON output.