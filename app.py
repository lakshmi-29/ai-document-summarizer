import streamlit as st
from transformers import pipeline
import PyPDF2

st.title("AI Document Summarizer")
st.write("Upload your PDF and text file to summarize it.")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'txt'])

if uploaded_file:
    file_content = ""
    if uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            file_content += page.extract_text()
    else:
        file_content = str(uploaded_file.read(), "utf-8")

    st.subheader("Original Content")
    st.write(file_content[:1000] + "...")  # show first 1000 chars

    # Summarization
    st.subheader("Summary")
    summarizer = pipeline("summarization")
    summary = summarizer(file_content[:1000], max_length=150, min_length=30, do_sample=False)
    st.write(summary[0]['summary_text'])
