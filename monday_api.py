import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

MONDAY_API_KEY = st.secrets.get("MONDAY_API_KEY") or os.getenv("MONDAY_API_KEY")

API_URL = "https://api.monday.com/v2"

HEADERS = {
    "Authorization": MONDAY_API_KEY,
    "Content-Type": "application/json"
}

def get_board_data(board_id):
    query = f"""
    query {{
      boards(ids: {board_id}) {{
        items_page {{
          items {{
            name
            column_values {{
              id
              text
            }}
          }}
        }}
      }}
    }}
    """

    response = requests.post(
        API_URL,
        json={"query": query},
        headers=HEADERS
    )

    response.raise_for_status()

    return response.json()