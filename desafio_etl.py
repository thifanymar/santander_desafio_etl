

#desafio 1 santander
import requests
import pandas as pd
import datetime

def pegar_cotacao(dias, moeda):
  requisicao = requests.get(f"https://economia.awesomeapi.com.br/json/daily/{moeda}/{dias}")
  requisicao = requisicao.json()
  return requisicao

cotacoes = pegar_cotacao(3,'USD-BRL')

dfCotacao = []
for cotacao in cotacoes:
  cotacao_valor = cotacao['bid']
  cotacao_valor_alto = cotacao['high']
  cotacao_valor_baixo = cotacao['low']
  cotacao_timestamp = cotacao['timestamp']
  cotacao_timestamp = int(cotacao_timestamp)
  dt_object = datetime.date.fromtimestamp(cotacao_timestamp)
  dfCotacao.append({'data':dt_object,'cotacao_valor':cotacao_valor, 'cotacao_valor_alto':cotacao_valor_alto, 'cotacao_valor_baixo':cotacao_valor_baixo, 'cotacao_timestamp':cotacao_timestamp})


print(dfCotacao)
