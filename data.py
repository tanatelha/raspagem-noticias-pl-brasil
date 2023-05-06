from datetime import date, datetime

# Função para identificar o dia da raspagem

def data_de_hoje():
    data = date.today()

    # método strftime() é usado para formatar a data como uma string no formato "dd/mm/aaaa"
    data_formatada = data.strftime('%d/%m/%Y') 
    
    return data_formatada