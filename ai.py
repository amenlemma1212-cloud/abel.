import streamlit as st
import time
from datetime import date

# 1. Page Configuration
st.set_page_config(page_title="Abel AI", page_icon="🌟", layout="centered")

# 2. CSS for Ethiopia Flag, Animations, and Glass UI
st.markdown("""
    <style>
    /* አኒሜሽን - ገጹ ሲከፈት ቀስ ብሎ እንዲመጣ (Fade In) */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .main-container {
        animation: fadeIn 1.5s ease-out;
    }

    /* የኢትዮጵያ ባንዲራ ጀርባ */
    .stApp {
        background: linear-gradient(180deg, #009A44 0%, #FED100 50%, #EF4123 100%);
        color: white;
    }

    /* የመግቢያ ሳጥን (Glassmorphism) */
    .login-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
    }

    /* የቻት ባር እና ሜሴጅ መልክ */
    div[data-testid="stChatMessage"], div[data-testid="stChatInput"] {
        border-radius: 30px !important;
        backdrop-filter: blur(10px);
        background: rgba(255, 255, 255, 0.15) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State Init (ማስታወሻዎች)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "messages" not in st.session_state:
    st.session_state.messages = []
if "message_count" not in st.session_state:
    st.session_state.message_count = 0

# --- SIGN IN / SIGN UP PAGE ---
def login_page():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.title("Abel AI 🌟")
    
    tab1, tab2 = st.tabs(["Sign In (ግባ)", "Sign Up (ተመዝገብ)"])
    
    with tab1:
        st.subheader("እንኳን ደህና መጡ! ይግቡ")
        user = st.text_input("Username (ስም)", key="login_user")
        pwd = st.text_input("Password (የይለፍ ቃል)", type="password", key="login_pwd")
        if st.button("Sign In"):
            if user and pwd: # ለጊዜው ማንኛውንም ስም ይቀበላል
                with st.spinner('በመግባት ላይ...'):
                    time.sleep(1) # Animation effect
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("እባክዎ ስም እና የይለፍ ቃል ያስገቡ")

    with tab2:
        st.subheader("አዲስ አካውንት ይፍጠሩ")
        new_user = st.text_input("Username", key="reg_user")
        new_pwd = st.text_input("Password", type="password", key="reg_pwd")
        if st.button("Sign Up"):
            st.success("አካውንትዎ በትክክል ተፈጥሯል! አሁን መግባት ይችላሉ።")
    st.markdown('</div>', unsafe_allow_html=True)

# --- MAIN CHAT PAGE ---
def chat_page():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # የላይኛው ክፍል (Header)
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title("Abel AI 🌟 🇪🇹")
    with col2:
        if st.button("Sign Out"):
            st.session_state.logged_in = False
            st.rerun()

    # ቆጣሪ (Limit 30)
    DAILY_LIMIT = 30
    remains = DAILY_LIMIT - st.session_state.message_count
    st.sidebar.write(f"📅 የቀረዎት ጥያቄ፦ {remains} / {DAILY_LIMIT}")

    # የድሮ መልእክቶች
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # የቻት ባር (Curved & Glass)
    if prompt := st.chat_input("እዚህ ይጻፉ... 💬"):
        if st.session_state.message_count >= DAILY_LIMIT:
            st.error("⚠️ የዕለታዊ ገደብዎ አልቋል።")
        else:
            st.session_state.message_count += 1
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            ai_reply = f"አቤል ወንድሜ፣ መልእክትህን ተቀብያለሁ፦ '{prompt}'"
            with st.chat_message("assistant"):
                st.markdown(ai_reply)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# የትኛው ገጽ ይታይ?
if not st.session_state.logged_in:
    login_page()
else:
    chat_page()
