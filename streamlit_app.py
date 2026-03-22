import streamlit as st

st.title("Mój pierwszy projekt AI 🚀")
name = st.text_input("Jak się nazywasz?")
if name:

    st.write(f"Cześć {name}! Zaraz uruchomimy tu model LLM.")