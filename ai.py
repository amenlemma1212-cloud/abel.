import streamlit as st
import google.generativeai as genai

# ቁልፉን ከStreamlit Secrets ያነበዋል
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

st.title("የአቤል AI ረዳት 🤖")

user_input = st.text_input("እንዴት ልረዳህ እችላለሁ?")

if user_input:
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(user_input)
        st.write(response.text)
    except Exception:
        # ሲቆራረጥ ወይም ገደቡ ሲያልቅ ያንን አስቀያሚ Error አጥፍቶ ይህንን ያሳያል፡
        st.warning("⚠️ abel ai Daily limit is up! Please try again tomorrow.")