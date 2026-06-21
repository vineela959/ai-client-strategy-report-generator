import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_strategy(client_name, industry, goals):

    prompt = f"""
You are a business strategy analyst.

Create a client strategy report.

Client Name:
{client_name}

Industry:
{industry}

Goals:
{goals}

Generate:

1. Executive Summary
2. Industry Overview
3. Market Insights
4. Business Opportunities
5. Recommended Strategy
6. Action Plan

Make it professional and detailed.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content