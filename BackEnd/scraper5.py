import requests

url = 'https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2023/INFLUD23-03-04-2023.csv'
response = requests.get(url)

if response.status_code == 200:
    with open('arquivo.csv', 'wb') as f:
        f.write(response.content)
        print('Arquivo baixado com sucesso')
else:
    print('Falha ao baixar o arquivo')
    