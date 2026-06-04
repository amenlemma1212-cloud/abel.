import streamlit as st
import google.generativeai as genai

# ፍጹም ትክክለኛው እና የመጀመሪያው ቁልፍህ ያለምንም ነጥብ እዚህ አለ
api_key = "AIzaSyAQAb8RN6K-vPjqy-Kntwc8codftV1osR0gUJ0PAhtyTKSAGrDhrg"
genai.configure(api_key=api_key)

st.title("የአቤል AI ረዳት 🤖")

user_input = st.text_input("እንዴት ልረዳህ እችላለሁ?")

if user_input:
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(user_input)
    st.write(response.text)
