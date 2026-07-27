import os

from dotenv import load_dotenv

from monday_api import get_board_data
from data_cleaning import board_to_dataframe
from preprocessing import clean_dataframe
from insights import *

load_dotenv()

deals = get_board_data(os.getenv("DEALS_BOARD_ID"))

df = board_to_dataframe(deals)
df = clean_dataframe(df)

print("\nTOTAL PIPELINE VALUE\n")
print(total_pipeline_value(df))

print("\nDEALS BY STAGE\n")
print(deals_by_stage(df))

print("\nOWNER PERFORMANCE\n")
print(deals_by_owner(df))

print("\nTOP 5 DEALS\n")
print(top_5_deals(df))

print("\nSECTOR ANALYSIS\n")
print(sector_wise_value(df))

print("\nPRODUCT ANALYSIS\n")
print(product_wise_value(df))