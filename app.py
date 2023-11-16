import streamlit as st
from streamlit_extras.stateful_chat import chat, add_message
import pyperclip

with chat(key="my_chat"):
    if prompt := st.chat_input():
        pyperclip.copy(prompt)
        add_message("user", prompt, avatar="🧑‍💻")