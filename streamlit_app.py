import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Read secrets (works locally and on Streamlit Cloud)
DEALS_BOARD_ID = st.secrets.get("DEALS_BOARD_ID") or os.getenv("DEALS_BOARD_ID")

from monday_api import get_board_data
from data_cleaning import board_to_dataframe
from preprocessing import clean_dataframe
from ai_agent import answer_question
from dashboard import founder_summary

st.set_page_config(
    page_title="AI Business Intelligence Agent",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Business Intelligence Agent")
st.write("Ask questions about your Monday.com Deals data using Google Gemini AI.")

@st.cache_data
def load_data():
    deals = get_board_data(DEALS_BOARD_ID)
    df = board_to_dataframe(deals)
    df = clean_dataframe(df)
    return df

try:
    df = load_data()

    st.subheader("Business Dashboard")
    dashboard = founder_summary(df)
    st.text(dashboard)

    st.subheader("Ask AI")

    question = st.text_input(
        "Enter your question",
        placeholder="Example: Which owner has the highest pipeline?"
    )

    if st.button("Ask AI"):

        if not question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Thinking..."):
                answer = answer_question(question, df)

            st.subheader("Answer")
            st.write(answer)

except Exception as e:
    st.error(f"Error: {e}")