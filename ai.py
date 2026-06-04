import streamlit as st
import google.generativeai as genai

# በጣም አስተማማኝ በሆነው የድሮ መንገድ ቁልፉን እዚህ አስገብተነዋል
api_key = "AIzaSyAQAb8RN6J21lJ_Jd4uGOd_6ALrYR2koKefO0S4_ou8cnzl7kSnOQ"
genai.configure(api_key=api_key)

st.title("የአቤል AI ረዳት 🤖")

user_input = st.text_input("እንዴት ልረዳህ እችላለሁ?")

if user_input:
    # ሞዴሉን ወደ gemini-1.5-flash ቀይረነዋል (ይህ በጣም የተረጋጋ ነው)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(user_input)
    st.write(response.text)
