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
    
    /* ጽሑፎች በደንብ እንዲታዩ ማድረጊያ */
    h1, h2, h3, p, label {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8) !important;
    }
    
    /* ቪዲዮው መሃል ላይ እንዲሆን ማድረጊያ */
    .video-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
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
if "message_count" not in st.session_state:
    st.session_state.message_count = 0

# --- SIGN IN / SIGN UP PAGE ---
def login_page():
    st.title("Abel AI 🌟 🇪🇹")
    
    # 🇪🇹 የሚውለበለብ የኢትዮጵያ ባንዲራ ቪዲዮ (Cinematic Waving Ethiopia Flag)
    flag_video_html = """
    <div class="video-container">
        <iframe src="https://www.youtube.com/embed/S2lH8H6963w?autoplay=1&loop=1&playlist=S2lH8H6963w&muted=1&controls=0&showinfo=0&rel=0&modestbranding=1" 
                width="100%" height="315" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
        </iframe>
    </div>
    """
    st.markdown(flag_video_html, unsafe_allow_html=True)
    
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
            st.session_state.user_type =
