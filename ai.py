import streamlit as st
from google import genai

# ፍጹም ትክክለኛው ቁልፍህ ያለምንም ነጥብ እዚህ አለ
api_key = "AIzaSyAQAb8RN6J21lJ_Jd4uGOd_6ALrYR2koKefO0S4_ou8cnzl7kSnOQ"
client = genai.Client(api_key=api_key)

st.title("የአቤል AI ረዳት 🤖")

user_input = st.text_input("እንዴት ልረዳህ እችላለሁ?")

if user_input:
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_input,
    )
    st.write(response.text)
