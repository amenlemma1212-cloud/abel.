import streamlit as st
from google import genai

# Streamlit Secrets ውስጥ ያስገባነውን ቁልፍ እዚህ ያነበዋል
api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

st.title("የአቤል AI ረዳት 🤖")

user_input = st.text_input("እንዴት ልረዳህ እችላለሁ?")

if user_input:
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_input,
    )
    st.write(response.text)
    
