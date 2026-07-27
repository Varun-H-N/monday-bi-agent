import os

from dotenv import load_dotenv


load_dotenv()


def get_setting(name, default=None):
    try:
        import streamlit as st

        value = st.secrets.get(name)
    except Exception:
        value = None

    return value or os.getenv(name, default)
