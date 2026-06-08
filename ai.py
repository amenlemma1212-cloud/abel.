import streamlit as st
from datetime import date

# 1. የአፑ ስም፣ ምልክት እና የጀርባ ቀለም (Black & Blue Theme) ማስተካከል
st.set_page_config(page_title="Abel AI", page_icon="🌟", layout="centered")

# በCSS የጀርባውን ቀለም ጥቁር እና ሰማያዊ ማድረግ
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #001f3f 100%);
        color: white;
    }
    h1, p, label, .stMarkdown {
        color: white !important;
    }
    div[data-testid="stChatMessage"] {
        background-color: rgba(0, 43, 91, 0.5) !important;
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Abel AI 🌟")
st.write("እንኳን ወደ አቤል AI በደህና መጡ!")
st.write("---")

# 2. የቻት ታሪክ (Chat History) ማስታወሻ
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. የዕለታዊ ገደብ ማስታወሻ (Daily Limit Setup - በቀን 10 መልእክት ብቻ)
DAILY_LIMIT = 10
today = str(date.today())

if "usage_date" not in st.session_state:
    st.session_state.usage_date = today
    st.session_state.message_count = 0

# ቀኑ ከተቀየረ ገደቡን ወደ 0 መመለስ
if st.session_state.usage_date != today:
    st.session_state.usage_date = today
    st.session_state.message_count = 0

# የድሮ ንግግሮችን ማሳየት
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# የቀረው መልእክት ብዛት ማሳያ
remains = DAILY_LIMIT - st.session_state.message_count
st.sidebar.write(f"📅 ዛሬ የቀረዎት የጥያቄ ብዛት፦ {remains} / {DAILY_LIMIT}")

# 4. የቻት ባር (Chat Bar)
if prompt := st.chat_input("እዚህ ይጻፉ... 💬"):
    
    # ገደቡ ካለቀ መልእክት እንዳይቀበል መከልከል
    if st.session_state.message_count >= DAILY_LIMIT:
        st.error("⚠️ አቤል ወንድሜ፣ የዛሬው የዕለታዊ ጥያቄ ገደብህ አልቋል! ነገ ተመለስ።")
    else:
        # የጥያቄ ቆጣሪውን 1 መጨመር
        st.session_state.message_count += 1
        
        # የተጠቃሚውን መልእክት ማሳየት
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # AIው የሚመልሰው መልስ
        all_words = [m["content"] for m in st.session_state.messages if m["role"] == "user"]
        ai_reply = f"አቤል ወንድሜ፣ መልእክትህን ሰምቻለሁ፦ '{prompt}'። \n\n(ይህ ዛሬ የጠየቅኸው {st.session_state.message_count}ኛ ጥያቄህ ነው)"

        # የAIውን መልስ ማሳየት
        with st.chat_message("assistant"):
            st.markdown(ai_reply)
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})
        
        # ገጹን በራሱ ጊዜ አድሶ የቆጣሪውን ቁጥር እንዲቀንስ ማድረግ
        st.rerun()
