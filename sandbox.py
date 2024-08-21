import requests
import json



prod = input('ID Produto:  ')
unid_str = input('Quantidade:  ')
unid = int(unid_str)
enviar = input('Deseja enviar estoque? (y/n)')

if enviar == 'y' :
    url_prod = 'https://api.mercadolibre.com/items/MLB'
    url = f"{url_prod}{prod}"
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
    stock['variations'] = f'{unid}'
    print(url)
    
else:
    print('Estoque Cancelado.')




