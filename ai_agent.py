from google import genai
from config import get_setting


def _get_client():
    api_key = get_setting("GEMINI_API_KEY")

    if not api_key:
        return None

    return genai.Client(api_key=api_key)


def _data_context(df):
    preview = df.head(50).to_csv(index=False)
    columns = ", ".join(df.columns)

    return f"""
Columns:
{columns}

Row count: {len(df)}

Data Preview:
{preview}
"""


def answer_question(question, df):
    if df is None or df.empty:
        return "No data available."

    client = _get_client()

    if client is None:
        return "GEMINI_API_KEY not found."

    prompt = f"""
You are an expert Business Intelligence Analyst.

Answer ONLY using the Monday.com Deals data provided below.

If the answer cannot be determined from the data, say so.

Question:
{question}

Data:
{_data_context(df)}
"""

    try:
        response = client.models.generate_content(
            model="models/gemini-3.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"Gemini request failed:\n{e}"