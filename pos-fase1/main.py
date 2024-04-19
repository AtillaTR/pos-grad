from requests import get
from bs4 import BeautifulSoup

response = get('http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02')
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('td', attrs={'class': "tb_item"})
for td in tables:
    print(td.string)