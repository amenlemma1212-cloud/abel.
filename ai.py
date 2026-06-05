import streamlit as st
import google.generativeai as genai

# ቁልፉን ከStreamlit Secrets ያነበዋል
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

st.title("የአቤል AI ረዳት 🤖")

# 1. የቻት ታሪክ ማከማቻ (History) በStreamlit ውስጥ መፍጠር
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 2. የድሮዎቹን ንግግሮች በሙሉ በገጹ ላይ ማሳየት
for role, text in st.session_state.chat_history:
    if role == "user":
        st.write(f"**አንተ:** {text}")
    else:
        st.write(f"**AI ረዳት:** {text}")

# 3. አዲስ ጥያቄ መቀበያ ሳጥን
user_input = st.text_input("እንዴት ልረዳህ እችላለሁ?", key="user_message")

if user_input:
    # የአሁኑን ጥያቄ ታሪክ ውስጥ መመዝገብ
    st.session_state.chat_history.append(("user", user_input))
    
    # የGemini ሞዴልን መጥራት
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(user_input)
    
    # የAIን መልስ ታሪክ ውስጥ መመዝገብ
    st.session_state.chat_history.append(("ai", response.text))
    
    # ገጹን በራሱ አድሶ ታሪኩን እንዲያሳይ ማድረግ
    st.rerun()
