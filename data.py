from datetime import datetime, date, timedelta

# Função para identificar o dia anterior da raspagem

def data_ontem():
  data_hoje = datetime.now().date()
  data_ontem = data_hoje - timedelta(days=1)

  data_formatada = data_ontem.strftime(f"%d/%m/%Y")

  return data_formatada