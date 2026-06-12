import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Abel AI", page_icon="🌟", layout="centered")

# 2. Premium CSS (የኢትዮጵያ ባንዲራ + የTG እና Google ቁልፎች)
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
        background: rgba(255, 255, 255, 0.25) !important;
    }
    h1, h2, h3, p, label, span {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8) !important;
    }
    .btn-google { background-color: #df4a32 !important; color: white !important; border-radius: 10px; padding: 10px; text-align: center; font-weight: bold; margin-bottom: 5px; }
    .btn-telegram { background-color: #0088cc !important; color: white !important; border-radius: 10px; padding: 10px; text-align: center; font-weight: bold; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State (የአፑ ማህደረ ትውስታ)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_type" not in st.session_state:
    st.session_state.user_type = None 
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- LOGIN PAGE ---
def login_page():
    st.title("Abel AI 🌟 🇪🇹")
    tab1, tab2, tab3 = st.tabs(["Login / Sign Up", "Social Logins 🌐", "Guest Mode 👤"])
    
    with tab1:
        st.text_input("Username", key="u_name")
        st.text_input("Password", type="password", key="p_word")
        if st.button("Start Chatting 🚀", key="login_submit_btn"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Member"

    with tab2:
        st.markdown('<div class="btn-google">🛑 Google Account</div>', unsafe_allow_html=True)
        if st.button("Sign in with Google", key="google_submit_btn"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Google User"
        st.write("---")
        st.markdown('<div class="btn-telegram">✈️ Telegram Account</div>', unsafe_allow_html=True)
        if st.button("Sign in with Telegram", key="tg_submit_btn"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Telegram User"

    with tab3:
        if st.button("Enter as Guest", key="guest_submit_btn"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Guest"

# --- CHAT PAGE ---
def chat_page():
    st.title(f"Abel AI - {st.session_state.user_type}")
    
    if st.button("Logout 🚪", key="logout_submit_btn"):
        st.session_state.logged_in = False
        st.session_state.messages = []

    # ቻቱን ማሳያ
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 💬 የቻት ባር (የሰርቨር ኤረር የሚያመጣው ነገር በሙሉ ተወግዷል)
    if prompt := st.chat_input("እዚህ ይጻፉ..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

# ገጹን መቆጣጠሪያ
if not st.session_state.logged_in:
    login_page()
else:
    chat_page()
