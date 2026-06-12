import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Abel AI", page_icon="🌟", layout="centered")

# 2. Premium CSS (የኢትዮጵያ ባንዲራ ገጽታ)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #009A44 0%, #FED100 50%, #EF4123 100%);
        color: white;
    }
    div[data-testid="stChatMessage"] {
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
    </style>
    """, unsafe_allow_html=True)

# 3. Session State (የአፑ ማህደረ ትውስታ)
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- MAIN CHAT PAGE (ያለ ሎጊን በቀጥታ የሚከፈት) ---
st.title("Abel AI 🌟 🇪🇹")

# የቆዩ መልዕክቶችን ማሳያ
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 💬 የቻት ባር (የ AI መልስ ጽሑፍ ሙሉ በሙሉ ተሰርዟል!)
if prompt := st.chat_input("እዚህ ይጻፉ... 💬"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
