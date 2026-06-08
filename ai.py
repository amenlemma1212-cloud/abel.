import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Abel AI", page_icon="🌟", layout="centered")

# 2. Advanced CSS (Ethiopia Flag + Premium Glass Chat Bar + Social Icons)
st.markdown("""
    <style>
    @keyframes zoomIn {
        0% { opacity: 0; transform: scale(0.9); }
        100% { opacity: 1; transform: scale(1); }
    }
    @keyframes slideIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .main-container { animation: zoomIn 0.5s ease-out; }
    .chat-container { animation: slideIn 0.4s ease-out; }

    /* የኢትዮጵያ ባንዲራ ጀርባ */
    .stApp {
        background: linear-gradient(180deg, #009A44 0%, #FED100 50%, #EF4123 100%) !important;
        background-attachment: fixed !important;
        color: white !important;
    }

    /* የመስታወት መልክ ለካርዶች */
    div[data-testid="stChatMessage"], .stTabs {
        border-radius: 20px !important;
        backdrop-filter: blur(15px) !important;
        background: rgba(255, 255, 255, 0.2) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
    }

    /* 🌟 የቻት ባሩን ወደ ንጹሕ ብሩህ መስታወት (Premium Glass) መቀየር */
    div[data-testid="stChatInput"] {
        border-radius: 30px !important;
        backdrop-filter: blur(25px) !important;
        -webkit-backdrop-filter: blur(25px) !important;
        background: rgba(255, 255, 255, 0.25) !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
    }
    
    div[data-testid="stChatInput"] textarea {
        color: white !important;
        background: transparent !important;
    }
    
    /* ጽሑፎች በባንዲራው ላይ በደንብ እንዲታዩ ማድረጊያ */
    h1, h2, h3, p, label {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State (ማስታወሻዎች)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_type" not in st.session_state:
    st.session_state.user_type = None 
if "messages" not in st.session_state:
    st.session_state.messages = []
if "message_count" not in st.session_state:
    st.session_state.message_count = 0
if "play_sound" not in st.session_state:
    st.session_state.play_sound = False

# --- 🌟 WELCOME SOUND (HTML AUTOPLAY) ---
if st.session_state.play_sound:
    tts_url = "https://translate.google.com/translate_tts?ie=UTF-8&tl=en&client=tw-ob&q=Welcome+to+Abel+AI"
    st.markdown(f'<iframe src="{tts_url}" allow="autoplay" style="display:none;"></iframe>', unsafe_allow_html=True)
    st.session_state.play_sound = False

# --- SIGN IN / SIGN UP PAGE ---
def login_page():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.title("Abel AI 🌟 🇪🇹")
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
                st.session_state.play_sound = True
                st.rerun()
        
        st.write("--- ወይም በዚህ ይግቡ ---")
        if st.button("🌐 Continue with Google", key="google_login_unique"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Google User"
            st.session_state.play_sound = True
            st.rerun()
            
        if st.button("💬 Continue with Telegram", key="tele_login_unique"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Telegram User"
            st.session_state.play_sound = True
            st.rerun()

    with tab2:
        st.subheader("አዲስ አካውንት ይፍጠሩ")
        new_user = st.text_input("New Username", key="reg_user")
        new_pwd = st.text_input("New Password", type="password", key="reg_pwd")
        if st.button("Sign Up & Start", key="real_signup_btn"):
            if new_user and new_pwd:
                st.session_state.logged_in = True
                st.session_state.user_type = "Member"
                st.session_state.play_sound = True
                st.rerun()
        
        st.write("--- ወይም በዚህ ይመዝገቡ ---")
        if st.button("🌐 Sign Up with Google", key="google_reg_unique"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Google User"
            st.session_state.play_sound = True
            st.rerun()
            
        if st.button("💬 Sign Up with Telegram", key="tele_reg_unique"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Telegram User"
            st.session_state.play_sound = True
            st.rerun()

    with tab3:
        st.subheader("በእንግድነት ይግቡ")
        if st.button("Enter as Guest", key="real_guest_btn"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Guest"
            st.session_state.play_sound = True
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

# --- MAIN CHAT PAGE ---
def chat_page():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    # Header
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title(f"Abel AI ({st.session_state.user_type})")
    with col2:
        if st.button("Exit", key="real_exit_btn"):
            st.session_state.logged_in = False
            st.session_state.messages = [] 
            st.session_state.message_count = 0
            st.rerun()

    # Sidebar
