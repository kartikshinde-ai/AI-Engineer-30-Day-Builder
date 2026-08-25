import csv
import json
from pathlib import Path

from langchain_ollama import OllamaLLM


# Load classification prompt
prompt_path = Path("classification_prompt.md")
classification_prompt = prompt_path.read_text(encoding="utf-8")

# Load dummy leads
csv_path = Path("data/dummy_leads.csv")

with csv_path.open(newline="", encoding="utf-8") as file:
    leads = list(csv.DictReader(file))

# Use Ollama model
llm = OllamaLLM(model="llama3.2:3b")

# Test first 10 leads
for lead in leads[:10]:
    lead_text = f"""
Name: {lead["name"]}
Course Interest: {lead["course_interest"]}
Message: {lead["message"]}
City: {lead["city"]}
Timeline: {lead["timeline"]}
"""

    prompt = f"""
{classification_prompt}

Lead data:
{lead_text}
"""

    response = llm.invoke(prompt)

    print("\n" + "=" * 60)
    print(f"Lead: {lead['name']}")
    print(response)