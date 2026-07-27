from monday_api import get_board_data
from data_cleaning import board_to_dataframe
from preprocessing import clean_dataframe
from ai_agent import answer_question
from config import get_setting


deals = get_board_data(get_setting("DEALS_BOARD_ID"))

df = board_to_dataframe(deals)
df = clean_dataframe(df)

print("===== AI BUSINESS INTELLIGENCE AGENT =====")

while True:

    question = input("\nAsk a question (type exit to quit): ")

    if question.lower() == "exit":
        break

    answer = answer_question(question, df)

    print("\nAnswer:\n")
    print(answer)
