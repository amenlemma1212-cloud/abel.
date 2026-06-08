import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Abel AI", page_icon="🌟", layout="centered")

# 2. Advanced CSS (Ethiopia Flag Theme + Premium Glass UI)
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
    </style>
    """, unsafe_allow_html=True)

# 3. Session State (ማስታወሻዎች)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_type" not in st.session_state:
    st.session_state.user_type = None 
if "messages" not in st.session_state:
    st.session_state.messages = []
# 📷 የፎቶ መቁጠሪያ (Limit: 3)
if "photo_count" not in st.session_state:
    st.session_state.photo_count = 0
# 🌟 የፎቶ ማያያዣ መክፈቻ ቁልፍ ሁኔታ
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

    # 🌟 1. የፎቶ ምልክት ቁልፍ (ስትጫነው ብቻ የፎቶ መላኪያውን ይከፍታል)
    if st.button("📷 Add Photo (ፎቶ አያይዝ)", key="toggle_upload_btn"):
        st.session_state.show_uploader = not st.session_state.show_uploader
        st.rerun()

    # 🌟 2. ቁልፉ ሲጫን ብቻ የሚታይ የፎቶ መምረጫ ሳጥን
    if st.session_state.show_uploader:
        if st.session_state.photo_count >= 3:
            st.error("⚠️ የፎቶ መላኪያ የ 3 ጊዜ ገደብዎ አልቋል!")
        else:
            uploaded_file = st.file_uploader("ፎቶዎን ይምረጡ", type=["png", "jpg", "jpeg"], key="hidden_img_up")
            if uploaded_file is not None:
                if st.button("Send Selected Photo 🚀", key="submit_hidden_img"):
                    st.session_state.photo_count += 1
                    st.session_state.messages.append({"role": "user", "content": "📷 [ፎቶ ተልኳል]"})
                    st.session_state.messages.append({"role": "assistant", "content": "አቤል AI ፎቶውን አይቶታል። በጣም ያምራል! 👍"})
                    st.session_state.show_uploader = False # ከተላከ በኋላ ሳጥኑን መልሶ መዝጋት
                    st.rerun()

    # 🌟 3. ኦሪጅናል ውቡ የስትሪምሊት ቻት ባር (Original Chat Input)
    if prompt := st.chat_input("እዚህ ይጻፉ... 💬"):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        ai_reply = "አቤል AI ነኝ፣ ጥያቄዎን ተቀብያለሁ!"
        with st.chat_message("assistant"):
            st.markdown(ai_reply)
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})
        st.rerun()

if not st.session_state.logged_in:
    login_page()
else:
    chat_page()
