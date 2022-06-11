import requests

cep = input('Digite o cep: ')
url = 'https://viacep.com.br/ws/%s/json/' % cep
response = requests.get(url)
response_json = response.json()
print(response_json)