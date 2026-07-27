from google import genai

from config import get_setting


api_key = get_setting("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Add it to .env or Streamlit secrets.")

client = genai.Client(api_key=api_key)

for model in client.models.list():
    print(model.name)
