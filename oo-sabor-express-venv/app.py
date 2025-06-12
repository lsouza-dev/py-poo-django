from requests import get
import json
from collections import defaultdict

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = defaultdict(list)
    
    for item in dados_json:
        nome_do_restaurante = item['Company']
        dados_restaurante[nome_do_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })
else:
    print(f'O erro foi {response.status_code}') 

for nome_do_restaurante,dados in dados_restaurante.items():
        nome_do_arquivo = f'.venv/jsons/{nome_do_restaurante}.json'
        
        with open(nome_do_arquivo,'w') as arquivo_restaurante:
             json.dump(dados,arquivo_restaurante,indent=4)


url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
response = get(url)

if response.status_code == 200:
    dados = response.json()
    cotacao = float(dados['USDBRL']['bid'])
    print(f'{dados['USDBRL']['code']} 1 dólar corresponse a R$ {cotacao:.2f}')