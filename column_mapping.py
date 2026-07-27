from monday_api import get_board_data
from config import get_setting


data = get_board_data(get_setting("DEALS_BOARD_ID"))

columns = data["data"]["boards"][0]["columns"]

print("Column Mapping\n")

for col in columns:
    print(f"{col['id']}  --->  {col['title']}")
