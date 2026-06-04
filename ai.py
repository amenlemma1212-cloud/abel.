import streamlit as st
from google import genai

st.title("የአቤል AI ረዳት 🤖")
st.write("እንኳን ወደ አቤል AI በሰላም መጡ!")

user_input = st.text_input("ማወቅ የሚፈልጉትን ነገር እዚህ ይጠይቁኝ:")

if user_input:
    try:
        client = genai.Client()
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_input,
        )
        st.write("### የAI መልስ:")
        st.write(response.text)
    except Exception as e:
        st.error("ችግር ተፈጥሯል፤ እባክህ ድጋሚ ሞክር።")