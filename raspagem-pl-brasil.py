import re 
import requests
from datetime import datetime
from bs4 import BeautifulSoup

from data import data_de_hoje




url_pl_brasil = ['https://premierleaguebrasil.com.br/category/futebol-ingles/',
                 'https://premierleaguebrasil.com.br/category/futebol-europeu/']

def raspagem_pl_brasil():
    data_hoje_funcao = data_de_hoje()
    raspagem = []


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


    raspagem.append(["", manchete, "", autor, str(data_hora), hora, "", link])

    return 'ok'