import requests
import json



prod = input('ID Produto:  ')
unid = input('Quantidade:  ')
enviar = input('Deseja enviar estoque? (y/n)')



if enviar == 'y' :
    url_prod = 'https://api.mercadolibre.com/items/MLB'
    url = f"{url_prod}{prod}"
    payload_dict = {
    "available_quantity": 2
    }
    payload_dict['available_quantity'] = f'{unid}'
    payload = json.dumps(payload_dict)
    headers = {
    'Authorization': 'Bearer APP_USR-6025612515037653-082120-b3b53d1d041b6b15491f68811a682612-1369454405',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)


    
else:
    print('Estoque Cancelado.')




