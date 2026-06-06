import streamlit as st

st.set_page_config(page_title="Abel Browser", page_icon="🌐", layout="centered")

st.title("Abel Browser 🌐")
st.write("እንኳን ወደ አቤል ብሮውዘር በደህና መጡ! ከታች መፈለግ የሚፈልጉትን ሊንክ ያስገቡ።")

# የሊንክ መጻፊያ ሳጥን
url = st.text_input("የዌብሳይት ሊንክ እዚህ ያስገቡ (ለምሳሌ፦ google.com)፦", "https://www.google.com")

if not url.startswith("http"):
    url = "https://" + url

# ተጠቃሚው ቁልፉን ሲነካ በቀጥታ ዌብሳይቱን በአዲስ ታብ ይከፍታል
st.write("---")
st.link_button("🚀 ድረ-ገጹን ለመክፈት እዚህ ይንኩ (Go)", url, use_container_width=True)
