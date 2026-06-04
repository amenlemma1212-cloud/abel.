import streamlit as st
import google.generativeai as genai

# አዲሱ ንጹሕ ቁልፍህ ሙሉ በሙሉ እዚህ ተስተካክሏል
api_key = "AIzaSyAQAb8RN6Lv7EusIu4JfJ8Fao-gByn94IVyIt6_ZO5m_RZm7WhxcA"
genai.configure(api_key=api_key)

st.title("የአቤል AI ረዳት 🤖")

user_input = st.text_input("እንዴት ልረዳህ እችላለሁ?")

if user_input:
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(user_input)
    st.write(response.text)
