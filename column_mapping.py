import os
from dotenv import load_dotenv
from monday_api import get_board_data

load_dotenv()

data = get_board_data(os.getenv("DEALS_BOARD_ID"))

columns = data["data"]["boards"][0]["columns"]

print("Column Mapping\n")

for col in columns:
    print(f"{col['id']}  --->  {col['title']}")