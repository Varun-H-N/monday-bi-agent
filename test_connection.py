from monday_api import get_board_data
from config import get_setting


print("===== DEALS BOARD =====")
print(get_board_data(get_setting("DEALS_BOARD_ID")))

print("\n===== WORK ORDERS BOARD =====")
print(get_board_data(get_setting("WORK_ORDERS_BOARD_ID")))
