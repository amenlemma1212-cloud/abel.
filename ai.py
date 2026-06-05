import streamlit as st
import google.generativeai as genai

# ቁልፉን ከStreamlit Secrets ያነበዋል
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

st.title("የአቤል AI ረዳት 🤖")

user_input = st.text_input("እንዴት ልረዳህ እችላለሁ?")

if user_input:
    # ለአሮጌው ላይብረሪ 'gemini-pro' በመጠቀም 404 ስህተቱን እንፈታዋለን
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_input)
    st.write(response.text)
