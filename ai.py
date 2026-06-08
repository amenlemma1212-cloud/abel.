import streamlit as st
import time
from datetime import date

# 1. Page Configuration
st.set_page_config(page_title="Abel AI", page_icon="🌟", layout="centered")

# 2. Advanced CSS for Animations & Glass UI
st.markdown("""
    <style>
    /* አኒሜሽን - ገጹ ከጎን ተንሸራትቶ እንዲመጣ (Slide In) */
    @keyframes slideIn {
        0% { opacity: 0; transform: translateX(-50px); }
        100% { opacity: 1; transform: translateX(0); }
    }
    /* አኒሜሽን - ለቁልፎች (Button Hover Effect) */
    .stButton>button:hover {
        transform: scale(1.05);
        transition: 0.3s;
        background-color: #FED100 !important;
        color: black !important;
    }
    
    .main-container {
        animation: slideIn 0.8s ease-out;
    }

    /* የኢትዮጵያ ባንዲራ ጀርባ */
    .stApp {
        background: linear-gradient(180deg, #009A44 0%, #FED100 50%, #EF4123 100%);
        color: white;
    }

    /* የመስታወት መልክ (Glassmorphism) */
    div[data-testid="stChatMessage"], div[data-testid="stChatInput"], .stTabs {
        border-radius: 25px !important;
        backdrop-filter: blur(15px);
        background: rgba(255, 255, 255, 0.15) !important;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State (ማስታወሻዎች)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_type" not in st.session_state:
    st.session_state.user_type = None # "Member" or "Guest"
if "messages" not in st.session_state:
    st.session_state.messages = []
if "message_count" not in st.session_state:
    st.session_state.message_count = 0

# --- SIGN IN / SIGN UP / GUEST PAGE ---
def login_page():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.title("Abel AI 🌟 🇪🇹")
    st.write("እንኳን ደህና መጡ! ለመቀጠል አማራጭ ይምረጡ።")
    
    tab1, tab2, tab3 = st.tabs(["Sign In", "Sign Up", "Guest Mode 👤"])
    
    with tab1:
        st.subheader("ይግቡ")
        user = st.text_input("Username", key="login_user")
        pwd = st.text_input("Password", type="password", key="login_pwd")
        if st.button("Log In"):
            if user and pwd:
                st.session_state.logged_in = True
                st.session_state.user_type = "Member"
                st.rerun()
            else:
                st.error("ስም እና የይለፍ ቃል ያስገቡ")

    with tab2:
        st.subheader("አዲስ አካውንት ይፍጠሩ")
        st.write("ይመዝገቡና በቀጥታ ማውራት ይጀምሩ!")
        new_user = st.text_input("New Username", key="reg_user")
        new_pwd = st.text_input("New Password", type="password", key="reg_pwd")
        if st.button("Sign Up & Start"):
            if new_user and new_pwd:
                with st.spinner('አካውንት እየተፈጠረ ነው...'):
                    time.sleep(1.5)
                st.session_state.logged_in = True
                st.session_state.user_type = "Member"
                st.rerun()
            else:
                st.error("ሁሉንም ቦታዎች ይሙሉ")

    with tab3:
        st.subheader("በእንግድነት ይግቡ")
        st.write("አካውንት መክፈት አያስፈልግዎትም (ጥያቄዎ ግን ሊገደብ ይችላል)።")
        if st.button("Enter as Guest"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Guest"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- MAIN CHAT PAGE ---
def chat_page():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Header
    col1, col2 = st.columns([4, 1])
    with col1:
        user_label = "👤 Guest" if st.session_state.user_type == "Guest" else "🌟 Member"
        st.title(f"Abel AI ({user_label})")
    with col2:
        if st.button("Exit"):
            st.session_state.logged_in = False
            st.session_state.messages = [] # ታሪክን ማጽዳት
            st.rerun()

    # Daily Limit Logic (Guest gets 5, Members get 30)
    limit = 30 if st.session_state.user_type == "Member" else 5
    remains = limit - st.session_state.message_count
    
    st.sidebar.markdown(f"### 📊 የእርስዎ ደረጃ: {st.session_state.user_type}")
    st.sidebar.write(f"📅 የቀረዎት ጥያቄ፦ {remains} / {limit}")

    # Display History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Bar
    if prompt := st.chat_input("እዚህ ይጻፉ... 💬"):
        if st.session_state.message_count >= limit:
            st.error(f"⚠️ የ {limit} ጥያቄ ገደብዎ አልቋል።")
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
    st.markdown('</div>', unsafe_allow_html=True)

# Logic to switch pages
if not st.session_state.logged_in:
    login_page()
else:
    chat_page()
