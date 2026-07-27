import requests

from config import get_setting


API_URL = "https://api.monday.com/v2"


def get_board_data(board_id):
    api_key = get_setting("MONDAY_API_KEY")

    if not api_key:
        raise ValueError("MONDAY_API_KEY not found. Add it to .env or Streamlit secrets.")

    if not board_id:
        raise ValueError("Board ID not found. Add DEALS_BOARD_ID to .env or Streamlit secrets.")

    query = """
    query ($board_ids: [ID!]) {
      boards(ids: $board_ids) {
        columns {
          id
          title
        }
        items_page(limit: 500) {
          items {
            name
            column_values {
              id
              text
            }
          }
        }
      }
    }
    """

    response = requests.post(
        API_URL,
        json={"query": query, "variables": {"board_ids": [str(board_id)]}},
        headers={
            "Authorization": api_key,
            "Content-Type": "application/json",
        },
        timeout=30,
    )

    response.raise_for_status()

    payload = response.json()

    if payload.get("errors"):
        message = payload["errors"][0].get("message", payload["errors"])
        raise RuntimeError(f"Monday API error: {message}")

    return payload
