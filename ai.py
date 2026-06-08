import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Abel AI", page_icon="🌟", layout="centered")

# 2. Advanced CSS (Ethiopia Flag Theme)
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
        backdrop-filter: blur(15px) !important;
        background: rgba(255, 255, 255, 0.25) !important;
    }
    div[data-testid="stChatInput"] textarea {
        color: white !important;
    }
    h1, h2, h3, p, label, span {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8) !important;
    }
    .emoji-style {
        font-size: 100px;
        text-align: center;
        margin-bottom: 10px;
    }
    /* ማህበራዊ ሚዲያ ቁልፎች ዲዛይን */
    .social-btn {
        display: block;
        width: 100%;
        text-align: center;
        background: rgba(255, 255, 255, 0.3);
        border: 1px solid white;
        padding: 10px;
        border-radius: 10px;
        color: white !important;
        text-decoration: none;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State (ማህደረ ትውስታ)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_type" not in st.session_state:
    st.session_state.user_type = None 
if "messages" not in st.session_state:
    st.session_state.messages = []
if "photo_count" not in st.session_state:
    st.session_state.photo_count = 0

# 🌟 ለጥያቄዎች ምርጥ ምክር (Advice) መስጫ ፈንክሽን
def get_ai_advice(user_prompt):
    p = user_prompt.lower()
    # ስለ ኮምፒውተር ወይም ስልክ መሞቅ
    if "hot" in p or "overheat" in p or "fan" in p:
        return "💡 **የአቤል AI ምክር፦** ኮምፒውተርህ በጣም የሚሞቅ ከሆነ በጀርባ የሚሰሩ አላስፈላጊ ፕሮግራሞችን ዝጋ። የላፕቶፕህን ፕሮሰሰር ፍጥነት ለመቆጣጠር በሊኑክስ ላይ 'auto-cpufreq' መጠቀም ትችላለህ። እንዲሁም የአየር ማስወጫ ቀዳዳው እንዳይደፈን ጠረጴዛ ላይ አስቀምጠው።"
    # ስለ ቪዲዮ ኤዲቲንግ ወይም ዩቲዩብ
    elif "video" in p or "edit" in p or "youtube" in p or "phonk" in p:
        return "💡 **የአቤል AI ምክር፦** በዩቲዩብ ቻናልህ ስኬታማ ለመሆን በየቀኑ አጫጭር ቪዲዮዎችን (Shorts) በጥራት ልቀቅ። ለቪዲዮዎችህ ሳቢ 'Whoosh' እና 'Impact' የድምፅ ተፅዕኖዎችን (Sound Effects) ተጠቀም። በስልክህም ቢሆን በCapCut ምርጥ ኤዲት መስራት ትችላለህ!"
    # ስለ ጌም
    elif "game" in p or "roblox" in p or "gta" in p:
        return "💡 **የአቤል AI ምክር፦** ጌም በሚጫወትበት ጊዜ ፍጥነቱ እንዲጨምር የጌሙን ግራፊክስ (Graphics Quality) ወደ 'Low' ቀይረው። እንዲሁም ላፕቶፕህ በቻርጀር መሰካቱን አረጋግጥ፤ ይሄ የግራፊክስ ካርዱ ሙሉ አቅሙን እንዲጠቀም ይረዳዋል።"
    # ስለ ቋንቋ ወይም ትምህርት
    elif "english" in p or "learn" in p or "amharic" in p:
        return "💡 **የአቤል AI ምክር፦** እንግሊዘኛህን ለማሳደግ በየቀኑ አዳዲስ ቃላትን በደብተርህ ላይ መጻፍ እና መለማመድ ትልቅ ለውጥ ያመጣል። በርታ!"
    # ለሌሎች አጠቃላይ ጥያቄዎች
    else:
        return "💡 **የአቤል AI ምክር፦** ሀሳብህ በጣም ጥሩ ነው። ማንኛውንም የቴክኖሎጂ ችግር ለመ
