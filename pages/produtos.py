#-----------------------| IMPORT (INÍCIO)
import requests
import streamlit as st
import json
#-----------------------| IMPORT (FIM)
#--------------------------------------
#-----------------------| MENU (INÍCIO)
with st.sidebar:
    st.page_link("dashboard.py", label="Início", icon="🔅")
    st.page_link("pages/search.py", label="Procurar Item", icon="🔎",disabled=True)
    st.page_link("pages/sandbox.py", label="Sandbox", icon="🛠️")
#-----------------------| MENU (FIM)
#--------------------------------------
#-----------------------| SCHEMA (INÍCIO)