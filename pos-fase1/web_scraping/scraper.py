from requests import get
from bs4 import BeautifulSoup
from collections import defaultdict
import json
import pandas as pd

url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'

def get_producao(url:str) -> str:
    try:
        response = get(url)
        return response.text
    except Exception as e :
        print(e)

def formating_list(elements_list:list) -> list:
    cleaned_list = [element.strip().replace(' ', '')for element in elements_list]
    
    return cleaned_list

def extract_itens(response:str) -> dict:
    soup = BeautifulSoup(response, 'html.parser')
    tds = soup.find_all('td', attrs={'class': "tb_subitem"})

    keys = [tds[pos].string for pos in range(0,len(tds)) if pos%2==0]
    values = [tds[pos].string for pos in range(0, len(tds)) if pos%2!=0]
    cleaned_keys = formating_list(keys)
    cleaned_values = formating_list(values)
    data = defaultdict(list)
    for chave, valor in zip(cleaned_keys, cleaned_values):
        data[chave].append(valor)

# Convertendo o defaultdict para um dicionário regular, se necessário
    data_dict = dict(data)
    print(data_dict)

if __name__ == '__main__':
    response = get_producao(url)
    extract_itens(response)