import streamlit as st

# የገጹ መለያ ስም
st.set_page_config(page_title="Abel Browser", page_icon="🌐", layout="wide")

st.title("Abel Browser 🌐")
st.write("እንኳን ወደ አቤል ብሮውዘር በደህና መጡ!")

# የሊንክ መጻፊያ ሳጥን
url = st.text_input("የዌብሳይት ሊንክ እዚህ ያስገቡ (ለምሳሌ፦ google.com)፦", "https://www.google.com")

if not url.startswith("http"):
    url = "https://" + url

# ዌብሳይቱን በStreamlit ውስጥ መክፈቻ
st.markdown(
    f'<iframe src="{url}" style="width:100%; height:700px; border:none;"></iframe>',
    unsafe_allow_html=True
)
