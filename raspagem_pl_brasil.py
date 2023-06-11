# bibliotecas que já vem com python
import os #biblioteca para ver chaves em ambiente virtual


# bibliotecas externas: import em ordem alfabética e depois froms em ordem alfabética
import gspread
import requests
from flask import Flask
from bs4 import BeautifulSoup
from datetime import time, timedelta, datetime
from oauth2client.service_account import ServiceAccountCredentials 


# importanto funcoes de outros arquivos do repositório
from contagem_palavras import contagem_palavras


# variáveis de ambiente

GOOGLE_SHEETS_KEY = os.environ["GOOGLE_SHEETS_KEY"] 
GOOGLE_SHEETS_CREDENTIALS = os.environ['GOOGLE_SHEETS_CREDENTIALS']

conta = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_SHEETS_CREDENTIALS)
api = gspread.authorize(conta)
planilha = api.open_by_key(f'{GOOGLE_SHEETS_KEY}') 

sheet_raspagem = planilha.worksheet('raspagem')


# Criação do site
app = Flask(__name__)


@app.route("/")
def index():
  return "Esse é um site."


@app.route("/raspagem-pl")
def raspagem_pl_brasil():
  raspagem = []

  data_de_ontem = data_ontem()

  # sites que serão raspados
  url_pl_brasil = ['https://premierleaguebrasil.com.br/category/futebol-ingles/',
                  'https://premierleaguebrasil.com.br/category/futebol-europeu/']

  for url in url_pl_brasil:
    resposta = requests.get(f'{url}')
    site_pl = BeautifulSoup(resposta.content)

    noticias = site_pl.findAll('article')

    for i in noticias:
      data_hora = i.find('time', {'class' :'ct-meta-element-date' }).text
      data_noticia = data_hora[0:10]
      
      if data_noticia != data_de_ontem:
        continue

      else:  
        texto = i
        manchete = (texto.find('h2', {'class' : 'entry-title'}).text).replace('\n', '')
        autor = texto.find('span', {'itemprop':'name'}).text
        data = data_hora[0:5] # selecionar as primeiras letras
        hora = data_hora[11:16] # selecionar as últimas letras
        link = texto.find('a').get('href')

        palavras = contagem_palavras(link)

      raspagem.append(["Category", manchete, "Angle/Comment", autor, str(data), hora, "Publish article", palavras, link])

  sheet_raspagem.append_rows(raspagem)

  return f'Foram adicionados {len(raspagem)} matérias'