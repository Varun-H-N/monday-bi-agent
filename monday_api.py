import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

MONDAY_API_KEY = st.secrets.get("MONDAY_API_KEY") or os.getenv("MONDAY_API_KEY")