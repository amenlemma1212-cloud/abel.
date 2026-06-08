import streamlit as st

# የአፑ ስም እና ምልክት
st.set_page_config(page_title="Abel AI", page_icon="🌟", layout="centered")

st.title("Abel AI 🌟")
st.write("እንኳን ወደ አቤል AI በደህና መጡ! አሁን ሁሉንም ነገር አስታውሳለሁ።")
st.write("---")

# 1. የቻት ታሪክ (Chat History) ማስታወሻ መፍጠር (እንዳይረሳ)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. የድሮ የንግግር ታሪኮችን በስክሪኑ ላይ ማሳየት
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. የቻት ባር (Chat Bar) ከነ ምልክቱ (Enter Icon)
if prompt := st.chat_input("እዚህ ይጻፉ... 💬"):
    
    # የተጠቃሚውን መልእክት ማሳየት
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # መልእክቱን ወደ ታሪክ (History) መጨመር
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AIው የሚመልሰው ቀላል መልስ (ታሪክ እያስታወሰ)
    all_words = [m["content"] for m in st.session_state.messages if m["role"] == "user"]
    ai_reply = f"አቤል ወንድሜ፣ የላክኸውን መልእክት ሰምቻለሁ፦ '{prompt}'። \n\nእስካሁን ያወራናቸው ነገሮች በሙሉ በታሪኬ ውስጥ ተቀምጠዋል፦ {' ➡️ '.join(all_words)}"

    # የAIውን መልስ ማሳየት
    with st.chat_message("assistant"):
        st.markdown(ai_reply)
        
    # የAIውን መልስ ወደ ታሪክ መጨመር
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
