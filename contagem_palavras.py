import re 
import requests
from bs4 import BeautifulSoup


def contagem_palavras(url):

    # Fazer uma requisição para obter o conteúdo da página
    res = requests.get(f'{url}')

    # Criar um objeto BeautifulSoup a partir do conteúdo HTML
    soup = BeautifulSoup(res.content, 'html.parser')

    # Selecionar apenas os parágrafos, intertítulos e listas
    conteudo_entry = soup.find('div', {'class':'entry-content'})

    palavras = []


    # Coletando os conteúdos
    ## Parágrafos
    paragrafo = conteudo_entry.find_all('p')

    for i in paragrafo:
        if str(i).startswith('<p>—'):
            continue
        if str(i).startswith('<p> <script'):
            continue
        if str(i).startswith('<p>'):
            texto_puro = re.sub('<.*?>', '', str(i))
            texto_puro = texto_puro.split()
            palavras.append(texto_puro)

    ## H2, H3, H4
    tags_intertitulo = ['h2', 'h3', 'h4']

    for tipo in tags_intertitulo:
        intertitulo = conteudo_entry.findAll(tipo)

        for i, valor in enumerate(intertitulo):
            if str(valor).startswith('<h2 class="title-post">'):
                continue
            if str(valor).startswith(f'<{tipo}>'):
                intertitulo_puro = intertitulo[i].text
                print(intertitulo_puro)
                intertitulo_palavras = intertitulo_puro.split()
                palavras.append(intertitulo_palavras)
        
    
    ## Listas ordenadas
    lista_ordenada = conteudo_entry.find('ol')

    if lista_ordenada in conteudo_entry:
        lista_ordenada_completa = " ".join([re.sub("</?\w+[^>]*>", " ", str(p)) for p in lista_ordenada])
        lista_ordenada_palavras= lista_ordenada_completa.replace('\n', ' ').replace('\r', '').replace('\t', '').split()
        palavras.append(lista_ordenada_palavras)


    ## Listas não ordenadas
    lista_nao_ordenada = conteudo_entry.find('ul')

    if lista_nao_ordenada in conteudo_entry:
        lista_nao_ordenada_completa = " ".join([re.sub("</?\w+[^>]*>", " ", str(p)) for p in lista_nao_ordenada])
        lista_nao_ordenada_palavras = lista_nao_ordenada_completa.replace('\n', ' ').replace('\r', '').replace('\t', '').split()
        palavras.append(lista_nao_ordenada_palavras)


    ## Olho
    olho_geral = conteudo_entry.findAll('figure', {'class' : 'wp-block-pullquote'})

    if olho_geral in conteudo_entry: # REVER ISSO DAQUI Ó
        olho_geral = olho_geral.find('p').text
        olho_palavras = olho_geral.split()
        palavras.append(olho_palavras)

    ## Bloco de <blockquote>
    block_quote = conteudo_entry.findAll('blockquote', {'class':'wp-block-quote'})

    if block_quote != []:
        for item in block_quote:
            block_quote_geral = item.find('p').text.replace('— ', "")
            block_quote_palavras = block_quote_geral.split()
            palavras.append(block_quote_palavras)
            

    palavras_final = sum(palavras, [])
    contagem = len(palavras_final)
    
    return contagem