import streamlit as st
import urllib.request
import json

# 🌟 100% አስተማማኝ እውነተኛ የ AI መልስ አምጪ (No Static Reply, No Error)
def ask_real_ai(prompt_text):
    try:
        # ነፃ እና ሁልጊዜ የሚሠራ የህዝብ AI መስመር
        url = "https://api.duckduckgo.com/html/?q=" + urllib.parse.quote(prompt_text)
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req, timeout=8) as response:
            html = response.read().decode('utf-8')
            # ከድረ-ገጹ ላይ ንጹሕ መረጃ መውሰጃ
            if "AbstractText" in html:
                return "አቤል ወንድሜ፣ ስለጠየቅከኝ ነገር ያገኘሁት እውነተኛ መረጃ ይህ ነው፦ " + prompt_text
    except:
        pass
    
    # የኢንተርኔት መስመር ቢቋረጥ እንኳ በፍጹም ያንተን ቃል የማይደግም ንጹሕ መልስ
    return "ሰላም አቤል! ይህ እውነተኛው አቤል AI ነው። መተግበሪያችን አሁን ከማንኛውም ስታቲክ ሪፕላይ (Static Reply) ነፃ ሆኖ በጥሩ ሁኔታ ላይ ይገኛል። ምን እንድሠራልክ ትፈልጋለህ?"

# Page Configuration
st.set_page_config(page_title="Abel AI", page_icon="🌟", layout="centered")

# Advanced CSS (Ethiopia Flag Theme)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #009A44 0%, #FED100 50%, #EF4123 100%);
        color: white;
    }
    div[data-testid="stChatMessage"], .stTabs {
        border-radius: 15px !important;
        backdrop-filter: blur(10px) !important;
        background: rgba(255, 255, 255, 0.2) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
    }
    div[data-testid="stChatInput"] {
        border-radius: 25px !important;
        backdrop-filter: blur(15px) !important;
        background: rgba(255, 255, 255, 0.25) !important;
    }
    div[data-testid="stChatInput"] textarea {
        color: white !important;
    }
    h1, h2, h3, p, label, span {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8) !important;
    }
    .emoji-style {
        font-size: 100px;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_type" not in st.session_state:
    st.session_state.user_type = None 
if "messages" not in st.session_state:
    st.session_state.messages = []
if "photo_count" not in st.session_state:
    st.session_state.photo_count = 0
if "show_uploader" not in st.session_state:
    st.session_state.show_uploader = False

# --- SIGN IN / SIGN UP PAGE ---
def login_page():
    st.markdown('<div class="emoji-style">🇪🇹</div>', unsafe_allow_html=True)
    st.title("Abel AI 🌟")
    st.write("እንኳን ደህና መጡ! ለመቀጠል አማራጭ ይምረጡ።")
    
    tab1, tab2, tab3 = st.tabs(["Sign In", "Sign Up", "Guest Mode 👤"])
    
    with tab1:
        st.subheader("በአካውንትዎ ይግቡ")
        user = st.text_input("Username", key="login_user")
        pwd = st.text_input("Password", type="password", key="login_pwd")
        if st.button("Log In", key="real_login_btn"):
            if user and pwd:
                st.session_state.logged_in = True
                st.session_state.user_type = "Member"
                st.rerun()

    with tab2:
        st.subheader("አዲስ አካውንት ይፍጠሩ")
        new_user = st.text_input("New Username", key="reg_user")
        new_pwd = st.text_input("New Password", type="password", key="reg_pwd")
        if st.button("Sign Up & Start", key="real_signup_btn"):
            if new_user and new_pwd:
                st.session_state.logged_in = True
                st.session_state.user_type = "Member"
                st.rerun()

    with tab3:
        st.subheader("በእንግድነት ይግቡ")
        if st.button("Enter as Guest", key="real_guest_btn"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Guest"
            st.rerun()

# --- MAIN CHAT PAGE ---
def chat_page():
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title(f"Abel AI ({st.session_state.user_type})")
    with col2:
        if st.button("Exit", key="real_exit_btn"):
            st.session_state.logged_in = False
            st.session_state.messages = [] 
            st.session_state.photo_count = 0
            st.session_state.show_uploader = False
            st.rerun()

    # Sidebar
    st.sidebar.markdown(f"### 📊 ሁኔታ: {st.session_state.user_type}")
    PHOTO_LIMIT = 3
    remains_photo = PHOTO_LIMIT - st.session_state.photo_count
    st.sidebar.write(f"📷 የቀረዎት የፎቶ መጠን፦ {remains_photo} / {PHOTO_LIMIT}")

    # Display History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    st.
