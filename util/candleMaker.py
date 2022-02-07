import time
import requests
from datetime import datetime
from controllers.candle import CandleList
from schemas.candle import CandleSchema

URL_POLONIEX = 'https://poloniex.com/public?command=returnTicker'
candle_schema = CandleSchema()

def get_candle_values(periodicidade, currency_pair):
  """Método que recebe periodicidade em segundos, currency_pair como string e
  retorna os valores de abertura, maxima, minima e fechamento"""
  times = 1
  periodicidade = periodicidade * 60
  respostas = []
  candle = {}
  while times <= periodicidade:
    resposta = ''
    try:
      resposta = requests.get(URL_POLONIEX).json()
    except:
      return print("erro")

    ultimo_valor = float(resposta[currency_pair]['last'])
    if ultimo_valor not in respostas:
      respostas.append(ultimo_valor)
    
    if times == 1:
      candle['abertura'] = ultimo_valor
    
    if times == periodicidade:
      candle['fechamento'] = ultimo_valor
      candle['maxima'] = max(respostas)
      candle['minima'] = min(respostas)

    time.sleep(1.0)
    times += 1
  return candle

def candle_maker(periodicidade, currency_pair):
  candle = get_candle_values(periodicidade, currency_pair)
  candle['moeda'] = currency_pair
  candle['periodicidade'] = periodicidade
  candle['datetime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  print(candle)
  try:
    CandleList.post(candle)
  except:
    print('erro ao salvar no banco')
