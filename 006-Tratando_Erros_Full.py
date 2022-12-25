from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError


def getTitulo(url):
    try:
        html = urlopen(url)
    except HTTPError as erro:
        print(f"Erro HTTP: {erro}")
        return None
    except URLError as erro:
        print(f"Erro URL: {erro}")
        return None
    except:
        print(f"Ocorreu um erro na página.")
        return None   
    

    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        titulo = bsObj.body.h1
    except ArithmeticError as erro:
        print(f"Erro ao acessar a tag: {erro}")
        return None
    except:
        print("Ocorreu um erro ao acessar o conteúdo da página.")
        return None
    
    return titulo

titulo = getTitulo(input("Informe a URL: "))

if titulo is not None:
    print(titulo)
else:
    print('Título não encontrado.')