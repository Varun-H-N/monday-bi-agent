import os
from dotenv import load_dotenv
from monday_api import get_board_data

load_dotenv()

print("===== DEALS BOARD =====")
print(get_board_data(os.getenv("DEALS_BOARD_ID")))

print("\n===== WORK ORDERS BOARD =====")
print(get_board_data(os.getenv("WORK_ORDERS_BOARD_ID")))