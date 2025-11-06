import streamlit as st

st.title("AI Document Summarizer")
st.write("Upload your PDF or text file to summarize it.")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    st.write("File uploaded successfully!")
