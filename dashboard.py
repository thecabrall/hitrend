#------------| IMPORTS |-----------#
import requests
import streamlit as st
import json
#------------| COLUNAS |-----------#
cont1 = st.container()
d1,d2 = st.columns([1,4])
a1,a2,a3 = st.columns(3)
b1,b2,b3 = st.columns(3)
c1,c2,c3 = st.columns(3)

#------------| ACESSOS |-----------#

refresh_token = 'TG-66c62d2df42a0a0001884908-1369454405'
conta_chave = 'JEeoXRkjW6nPaopDx58g5KIHnFEHGcp8'
app_id = '6025612515037653'

#--------------| RENOVAR CHAVE |----------#

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

refresh()
key = refresh()

with d1:
    ref = st.button('Gerar Token')
    with d2: 
        if ref == True:
            validade = st.write('Token válido por 6 horas')

#---------------| VISUALIZAÇÃO DO PRODUTO |------------------#

def ver_prod (txt):
    with c1:
            imagem = st.image(txt['pictures'][0]['url'])
            with c2:
                titulo = st.write(txt['title'])
                qualid = st.write(txt['condition'])
                estoq = st.write(f'Estoque atual: {produto['initial_quantity']}')
                sku = st.write(f'SKU: {txt['attributes'][7]['value_name']}')
                with c3:
                    gtin = st.write(f'GTIN: {txt['attributes'][3]['value_name']}')
                    preco = st.write(f'Preço: R$ {txt['price']:.2f}')
    return ver_prod

#------------| DASHBOARD |-----------#

payload_dict = {
"available_quantity": 0
}

with a1:
    prod = st.text_input('ID Produto')
    url_prod = 'https://api.mercadolibre.com/items/MLB'
    url = f"{url_prod}{prod}"
    response = requests.get(url)
    produto = response.json()
    
with a1:
    pesq = st.button('Ver Produto')

if pesq == True:
    ver_prod (produto)


with a2:
    unid = st.text_input('Novo Estoque')
    
    with a2:
        enviar_stock = st.button('Enviar Estoque')
    with b2:
        if enviar_stock == True:
            payload_dict['available_quantity'] = f'{unid}'
            payload = json.dumps(payload_dict)

            headers = {
            'Authorization': 'Bearer APP_USR-6025612515037653-082115-8dbc088010ec9bc0f1f11c532d10ceb4-1369454405',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
            }
            headers['Authorization'] = f'Bearer {key}'
            response = requests.request("PUT", url, headers=headers, data=payload)


with a3:
    preco_novo = st.number_input('Novo Preço')
    
    with a3:
        enviar_price = st.button('Enviar Preço')
    with b2:
        if enviar_price == True:
            payload_dict['price'] = f'{preco_novo}'
            payload = json.dumps(payload_dict)

            headers = {
            'Authorization': 'Bearer APP_USR-6025612515037653-082115-8dbc088010ec9bc0f1f11c532d10ceb4-1369454405',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
            }
            headers['Authorization'] = f'Bearer {key}'
            response = requests.request("PUT", url, headers=headers, data=payload)


