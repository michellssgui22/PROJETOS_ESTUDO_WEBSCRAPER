from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

#Tratando erro de HTTP
try: 
    html = urlopen('https://www.facebook.com/erroProvocado')
    print(f"HTNL 1: {html}")
except HTTPError as erro:
    print(erro)
    
#Tratando erro de URL
try: 
    html = urlopen('https://www.facebo.com/')
    print(f"HTNL 2: {html}")
except URLError as erro:
    print(erro)

