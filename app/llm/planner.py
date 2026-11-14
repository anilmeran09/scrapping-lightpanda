
import json

from app.llm.client import ask_llm


def generate_plan(instruction: str, page_info: str) -> dict:

    prompt = f"""
You are a web scraping planner.

Your task is to create a CSS extraction plan.

USER INSTRUCTION:
{instruction}

WEBSITE INFORMATION:
{page_info}

Return ONLY valid JSON with this structure:

{{
  "container_selector": "CSS selector",
  "fields": {{
    "field_name": "CSS selector"
  }},
  "pagination": {{
    "enabled": false,
    "next_selector": null
  }}
}}

Rules:
1. Use CSS selectors only.
2. Do not invent selectors without evidence.
3. Use selectors visible in the supplied page information.
4. If pagination is not present, set enabled to false.
5. Do not execute actions or submit forms.
"""

    result = ask_llm(prompt)

    return json.loads(result)
