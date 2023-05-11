import requests
from bs4 import BeautifulSoup

url='https://opendatasus.saude.gov.br/dataset/srag-2021-a-2023'
filetype='.csv'

headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

def get_soup(url):
    return BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')

for link in get_soup(url).find_all('a'):
    csv_link=link.get('href')
    if filetype in csv_link:
        print(csv_link)