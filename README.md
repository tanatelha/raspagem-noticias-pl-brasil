# Raspador de notícias da PL Brasil 💻⚽
Esse código tem como objetivo raspar as reportagens do portal de notícias [Premier League Brasil](https://premierleaguebrasil.com.br/), focado em futebol europeu. Vale ressaltar que o raspador foi construído *a pedido dos responsáveis pelo portal*.

## Composição
Para utilizar esse robô, você irá precisar de alguns processos:
* **Google Sheets:** Para usar o sheets, é necessário pedir acesso ao Google, que pode ser feito [neste link](https://console.cloud.google.com/). O resultado final será dois conteúdos: um e-mail genérico do Google, que será usado para você compartilhar a planilha do sheets com ele, e uma chave de acesso, enviada por meio de um arquivo .json. Dica: além de ativar o Google Sheets, você deve ativar também o Google Drive
* **Render:** é uma plataforma de nuvem, em que podemos usar para rodar o código e automatizar seu funcionamento. No Ben, essa foi a ferramenta utilizada, mas você pode escolher a de sua preferência

## Arquivos
* **app.py:** contém aplicação do robo raspador com os sites criado no Flask para automatização
* **data.py:** contém uma função que identifica o dia anterior ao dia em questão
* **contagem_palavras.py:** contém um código que calcula a quantidade de palavras de cada texto
* **requirements.txt:** é um arquivo de texto que possui todas as bibliotecas que precisam ser instaladas para rodar o código dentro da nuvem

## Contato
Para outras dúvidas e sugestões, envie um e-mail para tanatelha.dados@gmail.com ;)
