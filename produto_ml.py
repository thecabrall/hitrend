import requests
import streamlit as st
import json

# cont0 = st.container()
e1,e2 = st.columns(2)
cont1 = st.container()
w1,w2 = st.columns(2)
d1,d2 = st.columns([1,4])
a1,a2,a3,a4,a5,a6 = st.columns([2,2,1,1,1,1])
b1,b2,b3 = st.columns(3)
c1,c2,c3 = st.columns(3)
cont3 = st.container(border=True)
r1,r2,r3,r4,r5,r6,r7,r8 = st.columns(8)


def ver_prod (txt): #---------------| VISUALIZADOR DE PRODUTO
    with cont4:
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
   
    return ver_prod