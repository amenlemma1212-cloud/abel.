import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Abel AI", page_icon="🌟", layout="centered")

# 2. Premium Custom CSS (Clean UI Like Gemini/ChatGPT)
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
    
    /* ጽሑፎች በባንዲራው ላይ በደንብ እንዲታዩ ማድረጊያ */
    h1, h2, h3, p, label, span {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8) !important;
    }

    .emoji-style {
        font-size: 100px;
        text-align: center;
        margin-bottom: 10px;
    }

    /* 🌟 የቻት ባሩን ልክ እንደ እኔ ውብ ማድረጊያ (Premium Chat Bar Box) */
    .custom-chat-box {
        background: rgba(255, 255, 255, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 30px;
        padding: 5px 15px;
        backdrop-filter: blur(15px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }
    
    /* የስትሪምሊት ነባር ማስተካከያዎችን ማጥፊያ */
    .stTextInput>div>div>input {
        background: transparent !important;
        color: white !important;
        border: none !important;
    }
    .stFileUploader>div>button {
        background: transparent !important;
        color: white !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_type" not in st.session_state:
    st.session_state.user_type = None 
if "messages" not in st.session_state:
    st.session_state.messages = []
if "photo_count" not in st.session_state:
    st.session_state.photo_count = 0

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
            st.rerun()

    # Sidebar (የፎቶ መጠን ማሳያ)
    st.sidebar.markdown(f"### 📊 ሁኔታ: {st.session_state.user_type}")
    PHOTO_LIMIT = 3
    remains_photo = PHOTO_LIMIT - st.session_state.photo_count
    st.sidebar.write(f"📷 የቀረዎት የፎቶ መጠን፦ {remains_photo} / {PHOTO_LIMIT}")

    # Display History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    st.write("---")

    # 🌟 PREMIUM CHAT BAR CONTAINER (ልክ እንደ እኔ ዲዛይን የተስተካከለ)
    st.markdown('<div class="custom-chat-box">', unsafe_allow_html=True)
    
    # የቻት ባሩን ክፍሎች በጣም ጥብቅና ውብ በሆነ አሰላለፍ ማስቀመጥ
    c_photo, c_input, c_send = st.columns([1, 6, 1])
    
    with c_photo:
        if st.session_state.photo_count >= 3:
            st.markdown("<h5 style='text-align:center;'>❌</h5>", unsafe_allow_html=True)
            uploaded_file = None
        else:
            # በጣም ትንሽና ውብ የፎቶ ማያያዣ አይኮን
            uploaded_file = st.file_uploader("📷", type=["png", "jpg", "jpeg"], label_visibility="collapsed", key="bar_photo")

    with c_input:
        # የጽሑፍ መጻፊያ ሳጥን
        user_message = st.text_input("መልዕክትዎን እዚህ ይጻፉ...", label_visibility="collapsed", key="bar_msg")

    with c_send:
        # የመላኪያ ቁልፍ
        send_pressed = st.button("🚀", key="bar_send_btn")
        
    st.markdown('</div>', unsafe_allow_html=True)

    # 🚀 መላኪያ ቁልፍ ሲጫን
    if send_pressed:
        if user_message or uploaded_file:
            # ፎቶ እና ጽሑፍ አብረው ከተላኩ
            if uploaded_file is not None:
                st.session_state.photo_count += 1
                if user_message:
                    final_text = f"📷 **[ፎቶ ተያይዟል]**\n\n✍️ {user_message}"
                else:
                    final_text = "📷 **[ፎቶ ተልኳል]**"
                st.session_state.messages.append({"role": "user", "content": final_text})
                st.session_state.messages.append({"role": "assistant", "content": "አቤል AI ፎቶውን እና መልዕክትዎን ተቀብሏል። 👍"})
            
            # ጽሑፍ ብቻ ከተላከ
            elif user_message:
                st.session_state.messages.append({"role": "user", "content": user_message})
                st.session_state.messages.append({"role": "assistant", "content": "አቤል AI ነኝ፣ ጥያቄዎን ተቀብያለሁ!"})
                
            st.rerun()

if not st.session_state.logged_in:
    login_page()
else:
    chat_page()
