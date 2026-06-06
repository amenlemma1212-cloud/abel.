import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Abel Browser", page_icon="🌐", layout="centered")

st.title("Abel Browser 🌐")
st.write("እንኳን ወደ አቤል ብሮውዘር በደህና መጡ!")

# የሊንክ መጻፊያ ሳጥን
url = st.text_input("የዌብሳይት ሊንክ እዚህ ያስገቡ (ለምሳሌ፦ google.com)፦", "google.com")

# ሊንኩን ማስተካከል
if not url.startswith("http"):
    full_url = "https://" + url
else:
    full_url = url

st.write("---")

# የ Go ቁልፍ
if st.button("🚀 ለመክፈት እዚህ ይንኩ (Go)", use_container_width=True):
    # ይህች ትንሽ የጃቫስክሪፕት ኮድ አፑን ሰብራ በቀጥታ ዌብሳይቱን እንድትከፍት ታደርጋለች
    js = f"<script>window.open('{full_url}', '_blank');</script>"
    components.html(js, height=0)
