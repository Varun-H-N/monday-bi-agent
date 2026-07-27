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

Data preview (first 50 rows):
{preview}
"""


def _get_available_model(client):
    """
    Returns the first Gemini model that supports generateContent.
    """
    try:
        models = client.models.list()

        for model in models:
            name = model.name

            # Keep only Gemini models
            if "gemini" not in name.lower():
                continue

            # Check if generateContent is supported
            methods = getattr(model, "supported_generation_methods", [])

            if "generateContent" in methods:
                return name

    except Exception as e:
        raise Exception(f"Unable to list Gemini models: {e}")

    raise Exception("No compatible Gemini model found.")


def answer_question(question, df):
    if df is None or df.empty:
        return "No data is available to answer this question."

    client = _get_client()

    if client is None:
        return (
            "GEMINI_API_KEY is missing. "
            "Add it to Streamlit Secrets or your .env file."
        )

    prompt = f"""
You are a Business Intelligence Analyst.

Answer ONLY using the provided Monday.com Deals data.

If the answer is not available in the data, clearly say so.

Keep the answer concise.

Question:
{question}

Data:
{_data_context(df)}
"""

    try:
        model = _get_available_model(client)

        response = client.models.generate_content(
            model=model,
            contents=prompt,
        )

        return response.text.strip()

    except Exception as e:
        return f"Gemini request failed:\n\n{e}"