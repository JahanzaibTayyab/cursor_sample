import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash-exp")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Streamlit UI configuration
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("💬 Gemini Chatbot")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate Gemini response
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append(
            {"role": "assistant", "content": response.text}
        )
