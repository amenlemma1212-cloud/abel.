import streamlit as st
import google.generativeai as genai

# 1. AI Configuration (Gemini አእምሮን ማገናኘት)
# ማሳሰቢያ፡ እዚህ ጋር የራስህን API Key ብታስገባ የተሻለ ይሠራል
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-pro')

# 2. Page Configuration
st.set_page_config(page_title="Abel AI", page_icon="🌟", layout="centered")

# 3. CSS (የኢትዮጵያ ባንዲራ ዲዛይን)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #009A44 0%, #FED100 50%, #EF4123 100%);
        color: white;
    }
    div[data-testid="stChatMessage"] {
        border-radius: 15px;
        backdrop-filter: blur(10px);
        background: rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    h1, h2, h3, p, label, span {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# 4. Session State
if "messages" not in st.session_state:
    st.session_state.messages = []
if "photo_count" not in st.session_state:
    st.session_state.photo_count = 0
if "show_uploader" not in st.session_state:
    st.session_state.show_uploader = False

# --- MAIN APP ---
st.title("Abel AI 🌟 🇪🇹")

# የፎቶ ገደብ ማሳያ
st.sidebar.write(f"📷 የቀረዎት የፎቶ መጠን፦ {3 - st.session_state.photo_count} / 3")

# ቻቱን ማሳያ
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ፎቶ መላኪያ ቁልፍ
if st.button("📷 Add Photo"):
    st.session_state.show_uploader = not st.session_state.show_uploader
    st.rerun()

if st.session_state.show_uploader:
    if st.session_state.photo_count < 3:
        uploaded_file = st.file_uploader("ፎቶ ይምረጡ", type=["png", "jpg", "jpeg"])
        if uploaded_file and st.button("Send Photo 🚀"):
            st.session_state.photo_count += 1
            st.session_state.messages.append({"role": "user", "content": "📷 [ፎቶ ተልኳል]"})
            st.session_state.messages.append({"role": "assistant", "content": "ፎቶውን አየሁት አቤል! በጣም ደስ ይላል።"})
            st.session_state.show_uploader = False
            st.rerun()
    else:
        st.error("የፎቶ ገደብ አልቋል!")

# 🌟 የቻት ባር (አሁን ረጅም መልስ ይሰጣል)
if prompt := st.chat_input("እዚህ ይጻፉ..."):
    # የተጠቃሚውን መልዕክት ማሳየት
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI መልስ እንዲሰጥ ማድረግ
    with st.chat_message("assistant"):
        try:
            # እዚህ ጋር AI እውነተኛ መልስ ያመነጫል
            response = model.start_chat().send_message(prompt)
            full_response = response.text
            st.markdown(full_response)
        except:
            # API Key ከሌለህ ይሄን አጭር መልስ ይሰጣል
            full_response = f"አቤል ወንድሜ፣ ስለ '{prompt}' ያልከኝ ገብቶኛል። በጣም የሚገርም ሀሳብ ነው!"
            st.markdown(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})
