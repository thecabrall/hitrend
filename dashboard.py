import requests
import streamlit as st

#------------|IMPORTS|-----------#
CLIENT_ID= '6025612515037653'
CLIENT_SECRET= 'JEeoXRkjW6nPaopDx58g5KIHnFEHGcp8'
REDIRECT_URI = 'http://localhost:8501/'





url = 'https://api.mercadolibre.com/'
response = requests.get(url)
data = response.json()

print(data)