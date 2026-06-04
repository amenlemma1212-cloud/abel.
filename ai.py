import streamlit as st
import google.generativeai as genai

# API ቁልፍን ከSecrets ማግኘት
try:
    genai.configure(api_key=st.secrets["api"]["GEMINI_API_KEY"])
except:
    st.error("❌ API Key አልተገኘም። Secrets አረጋግጥ።")
    st.stop()

# ሞዴሉን አዘጋጅ
model = genai.GenerativeModel('gemini-1.5-flash')

def get_ai_response(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        st.error(f"ስህተት: {str(e)}")
        return "ይቅርታ፣ ችግር ተፈጥሯል። እባክህ ቆይተህ እንደገና ሞክር።"
