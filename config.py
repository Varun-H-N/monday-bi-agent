import os

from dotenv import load_dotenv

load_dotenv()

def get_setting(name, default=None):
    try:
        import streamlit as st

        st.write("Available secrets:", list(st.secrets.keys()))

        value = st.secrets.get(name)

        st.write(f"{name} =", "FOUND" if value else "NOT FOUND")

    except Exception as e:
        st.write("Secrets error:", e)
        value = None

    if value:
        return value

    env_value = os.getenv(name, default)

    if env_value:
        st.write(f"{name} loaded from .env")

    return env_value