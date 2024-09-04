#-----------------------| IMPORT (INÍCIO)
import requests
import json
import streamlit as st
#-----------------------| IMPORT (FIM)
#--------------------------------------
#-----------------------| MENU (INÍCIO)
with st.sidebar:
    st.page_link("dashboard.py", label="Início", icon="🔅")
    st.page_link("pages/search.py", label="Procurar Item", icon="🔎")
    st.page_link("pages/sandbox.py", label="Sandbox", icon="🛠️",disabled=True)
#-----------------------| MENU (FIM)