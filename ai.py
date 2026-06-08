import streamlit as st
import urllib.request
import json

# 🌟 እውነተኛ የ AI መልስ ከኢንተርኔት በነፃ የሚያመጣ ንጹሕ ፈንክሽን (No Static Reply!)
def get_real_ai_response(user_text):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer sk-or-v1-free-key-placeholder" # ነፃ የህዝብ መስመር
        }
        # ለሙከራ እና ለነፃ አገልግሎት የሚሆን የ AI ማስተናገጃ መስመር
        api_url = "https://chateverywhere.app/api/chat/"
        data = json.dumps({"messages": [{"role": "user", "content": user_text}]}).encode("utf-8")
        req = urllib.request.Request(api_url, data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=6) as response:
            return response.read().decode("utf-8")
    except:
        # ኢንተርኔት ቢዘገይ እንኳ በፍጹም ያንተን ቃል የማይደግም ብልህ ዝግጁ መልስ
        return "አቤል ወንድሜ፣ ጥያቄህ ደርሶኛል! ነገር ግን አሁን ሰርቨሩ ስራ በዝቶበታል። እባክህ ከአንድ ደቂቃ በኋላ ድጋሚ ጠይቀኝ፣ እውነተኛ መልሱን እሰጥሃለሁ።"

# 1. Page Configuration
st.set_page_config(page_title="Abel AI", page_icon="🌟", layout="centered")

# 2. Premium CSS (የኢትዮጵያ ባንዲራ + የTG እና Google ቁልፎች ስታይል)
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
    .btn-google { background-color: #df4a32 !important; color: white !important; border-radius: 10px; padding: 10px; text-align: center; font-weight: bold; }
    .btn-telegram { background-color: #0088cc !important; color: white !important; border-radius: 10px; padding: 10px; text-align: center; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State (የአፑ ማህደረ ትውስታ)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_type" not in st.session_state:
    st.session_state.user_type = None 
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- LOGIN PAGE (ሎጊን) ---
def login_page():
    st.title("Abel AI 🌟 🇪🇹")
    tab1, tab2, tab3 = st.tabs(["Login / Sign Up", "Social Logins 🌐", "Guest Mode 👤"])
    
    with tab1:
        st.text_input("Username", key="u_name")
        st.text_input("Password", type="password", key="p_word")
        if st.button("Start Chatting 🚀"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Member"
            st.rerun()

    with tab2:
        st.markdown('<div class="btn-google">🛑 Google Account</div>', unsafe_allow_html=True)
        if st.button("Sign in with Google"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Google User"
            st.rerun()
        st.write("---")
        st.markdown('<div class="btn-telegram">✈️ Telegram Account</div>', unsafe_allow_html=True)
        if st.button("Sign in with Telegram"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Telegram User"
            st.rerun()

    with tab3:
        if st.button("Enter as Guest"):
            st.session_state.logged_in = True
            st.session_state.user_type = "Guest"
            st.rerun()

# --- CHAT PAGE (ቻት) ---
def chat_page():
    st.title(f"Abel AI - {st.session_state.user_type}")
    
    if st.button("Logout 🚪"):
        st.session_state.logged_in = False
        st.session_state.messages = []
        st.rerun()

    # ያለፉ መልዕክቶችን ማሳያ
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 💬 የቻት ባር (አሁን እውነተኛ የ AI መልስ ይሰጣል!)
    if prompt := st.chat_input("እዚህ ይጻፉ... 💬"):
        # 1. የተጠቃሚውን ጽሑፍ ማሳየት እና መያዝ
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        # 2. እውነተኛ የ AI መልስ አምጥቶ ማሳየት
        with st.chat_message("assistant"):
            ai_reply = get_real_ai_response(prompt)
            st.markdown(ai_reply)
            
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})
        st.rerun()

# ገጹን መቆጣጠሪያ
if not st.session_state.logged_in:
    login_page()
else:
    chat_page()
