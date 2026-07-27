from google import genai

from config import get_setting


def answer_question(question, df):
    api_key = get_setting("GEMINI_API_KEY")

    if not api_key:
        return "GEMINI_API_KEY not found."

    try:
        client = genai.Client(api_key=api_key)

        models = client.models.list()

        model_names = []

        for m in models:
            model_names.append(m.name)

        return "Available Models:\n\n" + "\n".join(model_names)

    except Exception as e:
        return f"Error:\n{e}"