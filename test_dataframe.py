import os
from dotenv import load_dotenv
from monday_api import get_board_data
from data_cleaning import board_to_dataframe

load_dotenv()

deals = get_board_data(os.getenv("DEALS_BOARD_ID"))

df = board_to_dataframe(deals)

print(df.head())

print("\nColumns:\n")
print(df.columns)