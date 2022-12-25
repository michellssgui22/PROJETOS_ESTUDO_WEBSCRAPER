from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'https://www.facebook.com/'
# Aqui utilizei o Face Book como exemplo, pode ser substituído por outras url's
html = urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser')

for link in bs.find_all('a'):
    print(link.get('href'))
