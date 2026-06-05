import streamlit as st
import google.generativeai as genai

# ቁልፉን ከStreamlit Secrets ያነበዋል
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

st.title("የአቤል AI ረዳት 🤖")

# 1. የቻት ታሪክ ማከማቻ (History) መፍጠር
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 2. የድሮዎቹን መልእክቶች በሚያምር የቻት መልክ ማሳየት
for role, text in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(text)

# 3. በገጹ በታችኛው ክፍል አዲስ መጻፊያ ሳጥን
user_input = st.chat_input("እዚህ ጋር ይጻፉ...")

if user_input:
    # የአንተን ጥያቄ ማሳየት እና ታሪክ ውስጥ ማስቀመጥ
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.chat_history.append(("user", user_input))
    
    # ለድሮው ላይብረሪ የሚስማማውን ስም እዚህ ተክተናል
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_input)
    
    # የAI መልስን ማሳየት እና ታሪክ ውስጥ ማስቀመጥ
    with st.chat_message("assistant"):
        st.write(response.text)
    st.session_state.chat_history.append(("assistant", response.text))
