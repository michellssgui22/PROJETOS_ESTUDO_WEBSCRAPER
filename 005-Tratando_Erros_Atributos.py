from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'https://www.facebook.com/'
# Aqui utilizei o Face Book como exemplo, pode ser substituído por outras url's
html = urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser')

try:
    resultado = bs.html.tag_nao_existente.tag_vai_da_erro
    print(resultado)
except AttributeError as erro:
    print(f"Erro: {erro}")