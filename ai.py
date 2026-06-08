import streamlit as st
from datetime import date

# 1. የአፑ ስም እና ምልክት ማስተካከል
st.set_page_config(page_title="Abel AI", page_icon="🌟", layout="centered")

# 2. በCSS የኢትዮጵያ ባንዲራ ጀርባ እና የGlass/Curved ቻት ባር መሥራት
st.markdown("""
    <style>
    /* የኢትዮጵያ ባንዲራ የጀርባ ቀለም (አረንጓዴ፣ ቢጫ偏ቀይ) */
    .stApp {
        background: linear-gradient(180deg, #009A44 0%, #FED100 50%, #EF4123 100%);
        color: white;
    }
    
    /* ጽሑፎች በደንብ እንዲታዩ ነጭ እና ጥቁር ጥላ ማድረግ */
    h1, p, label, .stMarkdown {
        color: white !important;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);
    }
    
    /* የቻት መልእክት ሳጥኖችን የመስታወት መልክ (Glass effect) መስጠት */
    div[data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.2) !important;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 20px !important; /* የሰንጠረዡን ጠርዝ ክብ (Curved) ማድረግ */
        padding: 10px;
        margin: 5px 0;
    }
    
    /* የቻት ባሩን (Input Bar) ክብ እና የመስታወት መልክ ማድረግ */
    div[data-testid="stChatInput"] {
        background: rgba(255, 255, 255, 0.15) !important;
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        border-radius: 30px !important; /* ሳጥኑን በጣም ክብ (Curved) ያደርገዋል */
    }
    
    /* በውስጡ ያለውን የጽሑፍ መጻፊያ ክፍል ማስተካከል */
    div[data-testid="stChatInput"] textarea {
        color: white !important;
        border-radius: 30px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Abel AI 🌟 🇪🇹")
st.write("እንኳን ወደ አቤል AI በደህና መጡ! አሁን በኢትዮጵያ ባንዲራ አሸብርቋል።")
st.write("---")

# 3. የቻት ታሪክ (Chat History) ማስታወሻ
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. የዕለታዊ ገደብ ማስታወሻ (ዕለታዊ ገደብ ወደ 30 ተቀይሯል)
DAILY_LIMIT = 30
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

# 5. የቻት ባር (Chat Bar)
if prompt := st.chat_input("እዚህ ይጻፉ... 💬"):
    
    # ገደቡ ካለቀ መልእክት እንዳይቀበል መከልከል
    if st.session_state.message_count >= DAILY_LIMIT:
        st.error("⚠️ አቤል ወንድሜ፣ የዛሬው የ 30 ጥያቄ ዕለታዊ ገደብህ አልቋል! ነገ ተመለስ።")
    else:
        # የጥያቄ ቆጣሪውን 1 መጨመር
        st.session_state.message_count += 1
        
        # የተጠቃሚውን መልእክት ማሳየት
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # AIው የሚመልሰው መልስ
        ai_reply = f"አቤል ወንድሜ፣ መልእክትህን ሰምቻለሁ፦ '{prompt}'። \n\n(ይህ ዛሬ የጠየቅኸው {st.session_state.message_count}ኛ ጥያቄህ ነው)"

        # የAIውን መልስ ማሳየት
        with st.chat_message("assistant"):
            st.markdown(ai_reply)
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})
        
        # ገጹን በራሱ ጊዜ ማደስ
        st.rerun()
