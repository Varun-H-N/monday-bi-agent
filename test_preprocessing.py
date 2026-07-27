from monday_api import get_board_data
from data_cleaning import board_to_dataframe
from preprocessing import clean_dataframe
from config import get_setting


deals = get_board_data(get_setting("DEALS_BOARD_ID"))

df = board_to_dataframe(deals)

df = clean_dataframe(df)

print(df.info())

print(df.head())
