import os

from dotenv import load_dotenv
from google import genai

from dashboard import founder_summary

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def answer_question(question, df):

    dashboard = founder_summary(df)

    prompt = f"""
You are an AI Business Intelligence Assistant.

You are helping the founder understand the business.

Use ONLY the information below.

{dashboard}

Rules:
1. Answer only from the provided business data.
2. If the answer is not available, reply:
   "I cannot determine that from the available data."
3. Keep answers clear and concise.
4. Give business insights whenever possible.

User Question:
{question}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"