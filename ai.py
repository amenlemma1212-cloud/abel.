import streamlit as st

st.set_page_config(page_title="Abel AI", page_icon="😎", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e1e2f, #252545);
        color: white;
    }
    div[data-testid="stChatMessage"] {
        background-color: #2e2e4f !important;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
    }
    div[data-testid="stChatInput"] input {
        background-color: #3e3e66 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Abel AI 😎")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask Abel AI anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    ai_reply = f"Hello Abel, you said: {prompt}"
    
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    with st.chat_message("assistant"):
        st.markdown(ai_reply)
