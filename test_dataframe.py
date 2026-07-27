from monday_api import get_board_data
from data_cleaning import board_to_dataframe
from config import get_setting


deals = get_board_data(get_setting("DEALS_BOARD_ID"))

df = board_to_dataframe(deals)

print(df.head())

print("\nColumns:\n")
print(df.columns)
