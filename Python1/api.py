# APPLICATION PROGRAM INTERFACE
'''
import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacao_dic = cotacoes.json()

# print(cotacao_dic, ident = True)
cotacao_dolar = cotacao_dic['USDBRL']['bid']
print(cotacao_dolar)

cotacao_euro = cotacao_dic['EURBRL']['bid']
print(cotacao_euro)

cotacao_BITCOIN = cotacao_dic['BTCBRL']['bid']
print(cotacao_BITCOIN)
  '''
  
import pandas as pd
from flask import Flask
from flask.json import jsonify

#tabela = pd.read_csv('advertising.csv')
#total_vendas = tabela['Vendas'].sum()
#print(total_vendas)
#print(tabela)

app = Flask(__name__)


@app.route('/')
def homepage():
  navbar = '<a href="/contatos">Contato</a> | <a     href="/totalvendas">Total Vendas</a>'
  return f'Esta é a homepage do site{navbar}'


@app.route('/contatos')
def contatos():
  return 'Esta é a página de contatos'


@app.route('/totalvendas')
def vendas():
  tabela = pd.read_csv('advertising.csv')
  total_vendas = tabela['Vendas'].sum()
  return jsonify(total_vendas)


app.run(host='0.0.0.0')

       
       
       