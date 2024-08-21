import requests
import streamlit as st
import json

#------------| IMPORTS |-----------#

refresh_token = 'TG-66c62d2df42a0a0001884908-1369454405'
conta_chave = 'JEeoXRkjW6nPaopDx58g5KIHnFEHGcp8'
app_id = '6025612515037653'

#------------| ACESSOS |-----------#
def refresh ():
    url = "https://api.mercadolibre.com/oauth/token"

    payload = f'grant_type=refresh_token&client_id=6025612515037653&client_secret=JEeoXRkjW6nPaopDx58g5KIHnFEHGcp8&refresh_token={refresh_token}'
    headers = {
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    dados = response.json()
    data = dados['access_token']
    return data

ref = st.button('Gerar Token')
if ref == True:
    st.text(refresh())
else:
    st.success('Clique para gerar um novo Token.')

def att_estoque (item,qnt):

    url = f"https://api.mercadolibre.com/items/MLB{item}"

    payload = json.dumps({
    "available_quantity": 0
    })
    headers = {
    'Authorization': 'Bearer APP_USR-6025612515037653-082115-8dbc088010ec9bc0f1f11c532d10ceb4-1369454405',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    
    stock = response.json()
    stock['available_quantity'] = qnt
    return att_estoque

prod = st.text_input('ID Produto')
unid = st.text_input('Quantidade')
enviar = st.button('Enviar Estoque')

if enviar == True:
    att_estoque(prod,unid)
else:
    st.success('Preencha os campos para enviar estoque.')