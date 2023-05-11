import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

url='https://opendatasus.saude.gov.br/dataset/srag-2021-a-2023'
filetype='.csv'

headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
lista_links = []
def get_soup(url):
    return BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')

for link in get_soup(url).find_all('a'):
    csv_link=link.get('href')
    if filetype in csv_link:
        lista_links.append(csv_link)

ano = int(input('Digite o ano que deseja entre 2021 e 2023: '))
if ano == 2021:
    url = lista_links[0]
elif ano == 2022:
    url = lista_links[1]
else:
    url = lista_links[2]
sexo = str(input('Digite o sexo que quer filtrar F para Feminino e M para Masculino: '))
response = requests.get(url)



df = pd.read_csv('arquivo.csv', sep=';', encoding='latin1', usecols=['DT_NOTIFIC', 'ID_MUNICIP', 'CS_SEXO'], dtype={'ID_MUNICIP' : 'str', 'CS_SEXO' : 'str'})
df['data'] = pd.to_datetime(df['DT_NOTIFIC'], format='%d/%m/%Y')
casos_sjc = df[(df['ID_MUNICIP'] == 'SAO JOSE DOS CAMPOS') & (df['CS_SEXO'] == sexo) & (df['data'].dt.year == ano)] 
casos_taubate = df[(df['ID_MUNICIP'] == 'TAUBATE') & (df['CS_SEXO'] == sexo) & (df['data'].dt.year == ano)]
casos_jacarei = df[(df['ID_MUNICIP'] == 'JACAREI') & (df['CS_SEXO'] == sexo) & (df['data'].dt.year == ano)]

total_sjc = len(casos_sjc)
total_taubate = len(casos_taubate)
total_jacarei = len(casos_jacarei)


print(f'O total de casos de homens com síndrome respiratória em {ano} em São José dos Campos é: {total_sjc}')
print(f'O total de casos de homens com síndrome respiratória em {ano} em Taubaté é: {total_taubate}')
print(f'O total de casos de homens com síndrome respiratória em {ano} em Jacareí é: {total_jacarei}')

dados_casos = pd.Series([total_sjc, total_taubate, total_jacarei])
plt.bar(dados_casos.index, dados_casos.values, color='red', width=0.6)
plt.xticks(dados_casos.index, ['São José dos Campos', 'Taubaté', 'Jacareí'])
plt.xlabel('Cidade')
plt.ylabel('Número de casos')
plt.title(f'Casos de homens com síndrome respiratória em {ano}')

for i in range(len(dados_casos)):
    plt.text(dados_casos.index[i], dados_casos.values[i] + 4, str(dados_casos.values[i]), ha='center')
plt.show()