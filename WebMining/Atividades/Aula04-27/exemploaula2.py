from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'Oi mundo'

@app.route('/pegarvendas') #endpoint
def vendas():
    dados = pd.read_csv('.zadvertising.csv')
    totaldevendas = dados ['Sales'].sum()
    resposta = {'total_vendas': totaldevendas}
    # nao terminei

    