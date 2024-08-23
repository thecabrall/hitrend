#------------| IMPORTS |-----------#
import requests
import streamlit as st
import json
#------------| COLUNAS |-----------#
cont0 = st.container()
e1,e2 = st.columns(2)
cont1 = st.container()
w1,w2 = st.columns(2)
d1,d2 = st.columns([1,4])
a1,a2,a3,a4,a5,a6 = st.columns([2,2,1,1,1,1])
b1,b2,b3 = st.columns(3)
cont2 = st.container()
c1,c2,c3 = st.columns(3)
cont3 = st.container()
r1,r2,r3,r4,r5,r6,r7,r8 = st.columns([2,2,2,6,1,1,1,1])
#------------| ACESSOS |-----------#

refresh_token = 'TG-66c7559c2b3b8d0001c6601e-1369454405'
conta_chave = 'JEeoXRkjW6nPaopDx58g5KIHnFEHGcp8'
app_id = '6025612515037653'
#-------------------------------------------#

def refresh (): #----------------| FUNÇÃO PARA GERAR NOVO TOKEN
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

with cont0: #---------- | BOTÃO DE GERAR TOKEN
    ref = st.button('Gerar Token')
    with e1: 
        if ref == True:
            validade = st.write('Token válido por 6 horas')
        if ref == KeyError:
            st.warning('ID do produto está incorreto ou Vazio. Confira e faça novamente.')
    # st.text(key)

def ver_prod (txt): #---------------| VISUALIZADOR DE PRODUTO
    with c1:
            imagem = st.image(txt['pictures'][0]['url'])
            with c2:
                titulo = st.write(txt['title'])
                qualid = st.write(txt['condition'])
                estoq = st.write(f'Estoque atual: {produto['initial_quantity']}')
                for atributo in txt['attributes']:
                    if 'SELLER_SKU' in atributo['id']:
                        nome_sku = atributo['value_name']
                        sku = st.write(f'SKU: {nome_sku}')
                with c3:
                    gtin = st.write(f'GTIN: {txt['attributes'][3]['value_name']}')
                    preco = st.write(f'Preço: R$ {txt['price']:.2f}')
                    status_prod = st.write(f'Status: {txt['status']}')
                    with r1: #----------------| ESPAÇO PARA ATUALIZAR STATUS
                        ative_status = st.button('Ativar')
                    with r2:
                        pause_status = st.button('Pausar')
                    with r3:
                        feche_status = st.button('Fechar')
                        payload_dict = { 
                            "status": ""
                            }
                        if pause_status == True:
                            payload_dict["status"] = 'paused'
                            payload = json.dumps(payload_dict)
                            headers = {
                            'Authorization': 'Bearer APP_USR-6025612515037653-082115-8dbc088010ec9bc0f1f11c532d10ceb4-1369454405',
                            'Content-Type': 'application/json',
                            'Accept': 'application/json'
                            }
                            headers['Authorization'] = f'Bearer {key}'
                            response = requests.request("PUT", url, headers=headers, data=payload)
                            with c3:
                                st.write('Pausado!')    
                        if ative_status == True:
                            payload_dict["status"] = 'active'
                            payload = json.dumps(payload_dict)
                            headers = {
                            'Authorization': 'Bearer APP_USR-6025612515037653-082115-8dbc088010ec9bc0f1f11c532d10ceb4-1369454405',
                            'Content-Type': 'application/json',
                            'Accept': 'application/json'
                            }
                            headers['Authorization'] = f'Bearer {key}'
                            response = requests.request("PUT", url, headers=headers, data=payload)
                            with b2:
                                st.write('Ativado!')    
                        if feche_status == True:
                            payload_dict["status"] = 'closed'
                            payload = json.dumps(payload_dict)
                            headers = {
                            'Authorization': 'Bearer APP_USR-6025612515037653-082115-8dbc088010ec9bc0f1f11c532d10ceb4-1369454405',
                            'Content-Type': 'application/json',
                            'Accept': 'application/json'
                            }
                            headers['Authorization'] = f'Bearer {key}'
                            response = requests.request("PUT", url, headers=headers, data=payload)
                            with b2:
                                st.write('Encerrado!') 
    return ver_prod

with e1: #---------------| PESQUISADOR DE ID
    prod = st.text_input('ID Produto')
    url_prod = 'https://api.mercadolibre.com/items/MLB'
    url = f"{url_prod}{prod}"
    response = requests.get(url)
    produto = response.json()
    pesq = st.button('Buscar')
    if pesq == True:
        ver_prod (produto)    

with a1: #----------------| ESPAÇO PARA INSERIR NOVA QNT DE ESTOQUE
    unid = st.text_input('Novo Estoque')
    
    with a1:
        enviar_stock = st.button('Atualizar',key='enviar_stock')
    with b2:
        payload_dict = { 
        "available_quantity": ''
        }

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

with a2: #----------------| ESPAÇO PARA INSERIR NOVO PREÇO
    preco_novo = st.number_input('Novo Preço')
    
    with a2:
        enviar_price = st.button('Atualizar',key='enviar_price')
    with b2:
        payload_dict = { 
        "price": ''
        }
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

with cont1: #------------------| MUDAR NOME DO PRODUTO

    nome = st.text_input('Novo Nome')
    payload_dict = { 
        "title": ''
        }
    with w1:
        enviar_name = st.button('Atualizar',key='enviar_name')
    with w2:
        if enviar_name == True:
            payload_dict['title'] = f'{nome}'
            payload = json.dumps(payload_dict)
            url_prod = 'https://api.mercadolibre.com/items/MLB'
            url = f"{url_prod}{prod}"
            headers = {
            'Authorization': 'Bearer APP_USR-6025612515037653-082115-8dbc088010ec9bc0f1f11c532d10ceb4-1369454405',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
            }
            headers['Authorization'] = f'Bearer {key}'
            response = requests.request("PUT", url, headers=headers, data=payload)
