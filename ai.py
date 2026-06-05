import streamlit as st
import google.generativeai as genai

# ቁልፉን ከStreamlit Secrets ያነበዋል
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# 🖼️ ያንተን ፎቶ ለአፑ የጀርባ ስዕል ማድረጊያ CSS ዲዛይን
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://storage.googleapis.com/substrait-prod-user-uploaded-files/ababa%20haile.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    /* ጽሑፎቹ በደንብ እንዲታዩ ከጀርባቸው ጥላ ማድረግ */
    h1, label, p {
        color: #FFFFFF !important;
        text-shadow: 2px 2px 4px #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("የአቤል AI ረዳት 🤖")

user_input = st.text_input("እንዴት ልረዳህ እችላለሁ?")

if user_input:
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(user_input)
    st.write(response.text)
