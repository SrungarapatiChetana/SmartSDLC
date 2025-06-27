import streamlit as st
import requests

st.title("Smart SDLC - AI Requirement Analyzer")

uploaded_file = st.file_uploader("Upload Requirement Text File", type=["txt"])

if uploaded_file:
    st.success("File uploaded successfully!")

    if st.button("Analyze"):
        files = {'file': uploaded_file}
        response = requests.post("http://localhost:8000/analyze/", files=files)

        if response.status_code == 200:
            st.subheader("Extracted Requirements")
            st.write(response.json()['analysis'])
        else:
            st.error("Analysis failed.")
