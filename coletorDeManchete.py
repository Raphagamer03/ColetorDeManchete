# projeto: coletor de manchetes Globo
# autor: Raphael Teixeira Da Silva
# data : 27/06/2025

import requests
from bs4 import BeautifulSoup

# Define a URL alvo
url = 'https://g1.globo.com/'

# Faz a requisição
response = requests.get(url)

#Se deu certo
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Busca as manchetes nos h2 com classe home_tittle
    manchetes = soup.find_all('a', class_='feed-post-link')
    
    with open('manchetes_g1.txt', 'w', encoding='utf-8') as f:
        for i, m in enumerate(manchetes, start=1):
            titulo = m.get_text(strip=True)
            f.write(f"{i}. {titulo}\n")
            
    print(f"Coleta concluida! {len(manchetes)} manchetes salvas em 'manchetes_cnn.txt' .")
else:
    print(f"Erro ao acessar o site: {response.status_code}")            