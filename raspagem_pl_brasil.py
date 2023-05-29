import os
from dotenv import load_dotenv

import gspread
import json
import re 
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials 

# importanto funcoes de outros arquivos do repositório
from data import data_de_hoje
from contagem_palavras import contagem_palavras

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# variáveis de ambiente
GOOGLE_SHEETS_KEY = os.environ.get('GOOGLE_SHEETS_KEY')

GOOGLE_SHEETS_CREDENTIALS = os.environ.get('GOOGLE_SHEETS_CREDENTIALS')
with open("credenciais.json", mode="w") as arquivo:
    arquivo.write(GOOGLE_SHEETS_CREDENTIALS)
conta = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json")


api = gspread.authorize(conta)
planilha = api.open_by_key(f'{GOOGLE_SHEETS_KEY}') 
sheet_raspagens = planilha.worksheet('raspagem')



def raspagem_pl_brasil():
    
    raspagem = []
    data_hoje_funcao = data_de_hoje()
    
    # sites que serão raspados
    url_pl_brasil = ['https://premierleaguebrasil.com.br/category/futebol-ingles/',
                     'https://premierleaguebrasil.com.br/category/futebol-europeu/']
    
    for url in url_pl_brasil:
        resposta = requests.get(f'{url}')
        site_pl = BeautifulSoup(resposta.content)

        noticias = site_pl.findAll('article')

        for i in noticias:
            data_hora = i.find('time', {'class' :'ct-meta-element-date' }).text
            data_noticia = data_hora[0:5]

            if data_noticia == data_hoje_funcao:
                manchete = (i.find('h2', {'class' : 'entry-title'}).text).replace('\n', '')
                autor = i.find('span', {'itemprop':'name'}).text
                data = data_hora[0:5] # selecionar as primeiras letras
                hora = data_hora[11:] # selecionar as últimas letras
                link = i.find('a').get('href')

                palavras = contagem_palavras(url)
        
        raspagem.append(["", manchete, "", autor, str(data_hora), hora, "", palavras, link])
    
    sheet_raspagens.append_rows(raspagem)

    return f'{raspagem}'

print(raspagem_pl_brasil())