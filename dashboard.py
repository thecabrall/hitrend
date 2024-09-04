import streamlit as st


with st.sidebar:
    st.page_link("dashboard.py", label="Início", icon="🔅")
    st.page_link("pages/search.py", label="Procurar Item", icon="🔎")
    st.page_link("pages/sandbox.py", label="Sandbox", icon="🛠️")