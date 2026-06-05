import streamlit as st
import google.generativeai as genai
import base64

# ቁልፉን ከStreamlit Secrets ያነበዋል
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# 🖼️ ፎቶውን ከፋይሉ ስም አንብቦ ወደ ዲዛይን መቀየሪያ ኮድ
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

try:
    # በGitHub ላይ ያለውን "ababa haile.jpg" በቀጥታ ያነባል
    img_base64 = get_base64_image("ababa haile.jpg")
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        /* ጽሑፎቹ በደንብ እንዲታዩ ከጀርባቸው ጥላ ማድረግ */
        h1, label, p {{
            color: #FFFFFF !important;
            text-shadow: 2px 2px 4px #000000;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
except:
    pass

st.title("የአቤል AI ረዳት 🤖")

user_input = st.text_input("እንዴት ልረዳህ እችላለሁ?")

if user_input:
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(user_input)
    st.write(response.text)
