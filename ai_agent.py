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

Data preview, limited to 50 rows:
{preview}
"""


def answer_question(question, df):
    if df is None or df.empty:
        return "No data is available to answer this question."

    client = _get_client()

    if client is None:
        return "GEMINI_API_KEY is missing. Add it to your .env file locally or to Streamlit Cloud secrets."

    model = "gemini-2.5-flash-lite"
    prompt = f"""
You are a business intelligence analyst for Monday.com Deals data.
Answer the user's question using only the data provided below.
If the data is insufficient, say what is missing.
Keep the answer concise and include useful numbers where possible.

Question:
{question}

Data:
{_data_context(df)}
"""

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
        )
    except Exception as exc:
        return f"Gemini request failed: {exc}"

    return getattr(response, "text", "").strip() or "Gemini returned an empty response."
