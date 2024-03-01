import requests

url = 'https://viacep.com.br/ws/'
ceps = []

for _ in range(5):
    cep = input('Insira o CEP (ou digite "sair" para encerrar): ')
    if cep.lower() == 'sair' or len(ceps) >= 5:
        break
    ceps.append(cep)
    
formato = '/json/'

for cep in ceps:
    r = requests.get(url + cep + formato)
    if r.status_code == 200:
        print()
        print('XML:', r.text)
        print()
    else: 
        print('Não houve sucesso na requisição para o CEP', cep)


