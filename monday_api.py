import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("MONDAY_API_TOKEN")
API_URL = os.getenv("MONDAY_API_URL")

headers = {
    "Authorization": API_TOKEN,
    "Content-Type": "application/json"
}

def get_board_data(board_id):
    query = f"""
    {{
      boards(ids: {board_id}) {{
        id
        name

        columns {{
          id
          title
        }}

        items_page {{
          items {{
            id
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
        headers=headers
    )

    return response.json()