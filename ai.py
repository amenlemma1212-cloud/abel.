import streamlit as st
from google import genai

# አዲሱን ቁልፍህን በቀጥታ እዚህ አስገብተነዋል
api_key = "AIzaSyAQ.Ab8RN6ILouaV-srQPtX0gsIORtxe11CjLdrck-1CoQ9mlqu0ug"
client = genai.Client(api_key=api_key)

st.title("የአቤል AI ረዳት 🤖")

user_input = st.text_input("እንዴት ልረዳህ እችላለሁ?")

if user_input:
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_input,
    )
    st.write(response.text)
