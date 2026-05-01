import streamlit as st
from youtube_agent import bulid_youtube_agent

st.set_page_config(page_title="YouTube Video Analyzer",page_icon="🤖")

agent = bulid_youtube_agent()

st.title("🧠 AI YouTube Video Analyzer")

url = st.text_input("Paste the URL :")


if st.button("Analyze"):
    with st.spinner(text="Analyzing"):
        try:
            response = agent.run(f"Analyze Video : {url}")
            st.subheader("Analysis Report of the video")
            st.write(response.content)  
        except Exception as e:
            st.exception(e)