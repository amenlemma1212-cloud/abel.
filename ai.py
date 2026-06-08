import streamlit as st
import time
import base64

# 1. Page Configuration
st.set_page_config(page_title="Abel AI", page_icon="🌟", layout="centered")

# 2. የድምፅ አሠራር ተግባር (Welcome Sound Function)
def play_welcome_sound():
    # "Welcome to Abel AI" የሚለውን ድምፅ በኦዲዮ ሊንክ ማዘጋጀት
    text = "Welcome to Abel AI"
    # በነፃ የኦዲዮ ሊንክ መፍጠሪያ መጠቀም
    tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&tl=en&client=tw-ob&q={text.replace(' ', '+')}"
    
    # ድምፁ በጀርባ በራሱ እንዲከፈት (Autoplay) ማድረጊያ HTML
    audio_html = f"""
        <audio autoplay>
            <source src="{tts_url}" type="audio/mpeg">
        </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# 3. Advanced CSS for Animations, Background & Glass UI
st.markdown("""
    <style>
    /* አኒሜሽን - ገጹ ሲከፈት በታላቅ ሁኔታ በግልጽ እንዲመጣ (Zoom In Effect) */
    @keyframes zoomIn {
        0% { opacity: 0; transform: scale(0.8); }
        100% { opacity: 1; transform: scale(1); }
    }
    /* አኒሜሽን - ከጎን ተንሸራትቶ መግቢያ (Slide In) */
    @keyframes slideIn {
        0% { opacity: 0; transform: translateX(-50px); }
        100% { opacity: 1; transform: translateX(0); }
    }
    
    .main-container {
        animation: zoomIn 0.8s ease-out;
    }
    .chat-container {
        animation: slideIn 0.6s ease-out;
    }

    /* የቁልፎች አኒሜሽን (Button Hover) */
    .stButton>button:hover {
        transform: scale(1.08) translateY(-2px);
        transition: 0.2s ease-in-out;
        background-color: #FED100 !important;
        color: black !important;
        box-shadow: 0px 5px 15px rgba(255, 255, 255, 0.4);
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

# 4. Session State (ማስታወሻዎች)
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
                st.session_state.play_sound = True # ድምፁ እንዲከፈት መፍቀድ
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
                    time.sleep(1)
                st.session_state.logged_in = True
                st.session_state.user_type = "Member"
                st.session_state.play_sound = True # ድምፁ እንዲከፈት መፍቀድ
                st.rerun()
            else:
                st.error("ሁሉንም ቦታዎች ይሙሉ")

    with tab3:
        st.subheader("በእንግድነት ይግቡ")
        st.write("አካውንት ሳይከፍቱ ይሞክሩ (የ 5 ጥያቄ ገደብ አለው)።")
        if st.button("Enter as Guest"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Guest"
            st.session_state.play_sound = True # ድምፁ እንዲከፈት መፍቀድ
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- MAIN CHAT PAGE ---
def chat_page():
    # መግቢያው ሲከፈት ድምፅ አንድ ጊዜ ብቻ እንዲጫወት ማድረግ
    if st.session_state.play_sound:
        play_welcome_sound()
        st.session_state.play_sound = False # ድምፁ ደጋግሞ እንዳይረብሽ መዝጋት

    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    # Header
    col1, col2 = st.columns([4, 1])
    with col1:
        user_label = "👤 Guest" if st.session_state.user_type == "Guest" else "🌟 Member"
        st.title(f"Abel AI ({user_label})")
    with col2:
        if st.button("Exit"):
            st.session_state.logged_in = False
            st.session_state.messages = [] 
            st.session_state.message_count = 0
            st.rerun()

    # Sidebar
    st.sidebar.markdown(f"### 📊 የእርስዎ ደረጃ: {st.session_state.user_type}")
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

    # Chat Bar
    if prompt := st.chat_input("እዚህ ይጻፉ... 💬"):
        if st.session_state.user_type == "Guest" and st.session_state.message_count >= 5:
            st.error("⚠️ የእንግዳ Mode የ 5 ጥያቄ ገደብዎ አልቋል! እባክዎ አካውንት ይፍጠሩ።")
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
    
