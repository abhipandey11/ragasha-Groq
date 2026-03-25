import streamlit as st
import requests

st.set_page_config(page_title="RAGASHA", layout="centered")

st.title("🤖 RAGASHA AI Assistant")
st.write("Ask questions from preloaded documents")

query = st.text_input("Enter your question")

if st.button("Ask"):
    if query:
        with st.spinner("Thinking..."):
            res = requests.post(
                " http://127.0.0.1:8000/ask",
                json={"question": query}
            )

            st.success(res.json()["answer"])