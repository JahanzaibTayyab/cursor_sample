# Gemini Chatbot

A simple chatbot built with Streamlit and Google's Gemini AI.

## Setup

1. Clone the repository
2. Create a `.env` file and add your Gemini API key:
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```
3. Install dependencies:
   ```bash
   uv add streamlit google-generativeai python-dotenv
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Features

- Real-time chat interface
- Message history persistence during session
- Clean and intuitive UI
- Powered by Google's Gemini AI model

## Requirements

- Python 3.8+
- Streamlit
- Google Generative AI
- python-dotenv
