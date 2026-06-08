import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Abel AI", page_icon="🌟", layout="centered")

# 2. Simplified CSS (Ethiopia Flag + Premium Glass Chat Bar)
st.markdown("""
    <style>
    /* የኢትዮጵያ ባንዲራ ጀርባ */
    .stApp {
        background: linear-gradient(180deg, #009A44 0%, #FED100 50%, #EF4123 100%);
        color: white;
    }

    /* የመስታወት መልክ ለካርዶች እና ለTabs */
    div[data-testid="stChatMessage"], .stTabs {
        border-radius: 15px !important;
        backdrop-filter: blur(10px) !important;
        background: rgba(255, 255, 255, 0.2) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
    }

    /* የቻት ባሩን ወደ ንጹሕ ብሩህ መስታወት (Glass) መቀየር */
    div[data-testid="stChatInput"] {
        border-radius: 25px !important;
        backdrop-filter: blur(15px) !important;
        background: rgba(255, 255, 255, 0.25) !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
    }
    
    div[data-testid="stChatInput"] textarea {
        color: white !important;
    }
    
    /* ጽሑፎች በደንብ እንዲታዩ ማድረጊያ */
    h1, h2, h3, p, label {
        color: white !important;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8) !important;
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

# --- SIGN IN / SIGN UP PAGE ---
def login_page():
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
                st.rerun()
        
        st.write("--- ወይም በዚህ ይግቡ ---")
        if st.button("🌐 Continue with Google", key="google_login_unique"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Google User"
            st.rerun()
            
        if st.button("💬 Continue with Telegram", key="tele_login_unique"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Telegram User"
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
        
        st.write("--- ወይም በዚህ ይመዝገቡ ---")
        if st.button("🌐 Sign Up with Google", key="google_reg_unique"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Google User"
            st.rerun()
            
        if st.button("💬 Sign Up with Telegram", key="tele_reg_unique"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Telegram User"
            st.rerun()

    with tab3:
        st.subheader("በእንግድነት ይግቡ")
        if st.button("Enter as Guest", key="real_guest_btn"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Guest"
            st.rerun()

# --- MAIN CHAT PAGE ---
def chat_page():
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
    st.sidebar.markdown(f"### 📊 ሁኔታ: {st.session_state.user_type}")
    if st.session_state.user_type == "Guest":
        GUEST_LIMIT = 5
        remains = GUEST_LIMIT - st.session_state.message_count
        st.sidebar.write(f"📅 የቀረዎት ጥያቄ፦ {remains} / {GUEST_LIMIT}")
    else:
        st.sidebar.write("♾️ የእርስዎ የጥያቄ መጠን፦ ገደብ የለውም! (No Limit)")

    # Display History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Bar (Glass Mode)
    if prompt := st.chat_input("እዚህ ይጻፉ... 💬"):
        if st.session_state.user_type == "Guest" and st.session_state.message_count >= 5:
            st.error("⚠️ የእንግዳ Mode ገደብዎ አልቋል!")
        else:
            st.session_state.message_count += 1
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            ai_reply = f"አቤል AI ነኝ፣ ጥያቄዎን ተቀብያለሁ! (ጥያቄ ቁጥር {st.session_state.message_count})"
            with st.chat_message("assistant"):
                st.markdown(ai_reply)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
            st.rerun()

# Logic to switch pages
if not st.session_state.logged_in:
    login_page()
else:
    chat_page()
