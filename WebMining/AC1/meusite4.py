from flask import Flask, jsonify
import pandas as pd 

app = Flask(__name__)

# contruindo as funcionalidades
@app.route('/')
def hello_word():
    return "A aplicação está no ar"

@app.route('/jogo/')
def pegarjogos():
    dados = pd.read_csv('./futebol.csv',sep=";")
    dados["Placar"] = dados.apply(lambda row: str(row['home_team_goal_count']) + 'x' +str(row["away_team_goal_count"]),axis=1)
    
    dados["Match_ID"] = dados["home_team_name"] + "x" + dados["away_team_name"] + "-" + dados["date_GMT"]
    
    dados_w_ID = dados[['home_team_name',"away_team_name","Placar","date_GMT"]]
    resposta = dados_w_ID.to_dict("index")
    return jsonify(resposta)

@app.route("/Palmeiras/")
def pegarjogoscasaPalmeiras():
    dados = pd.read_csv('./futebol.csv',sep=";")
    golsCasadf = dados.query('home_team_name == "Palmeiras"')
    golsForadf = dados.query('away_team_name == "Palmeiras"')

    golsCasa = golsCasadf.groupby('home_team_name')["home_team_goal_count"].sum()
    golsFora = golsForadf.groupby('away_team_name')["away_team_goal_count"].sum()

    gols_totais = golsCasa.iat[0] + golsFora.iat[0]

    jogosCasadf= golsCasadf.groupby("home_team_name")['home_team_name'].count()
    jogosForadf= golsForadf.groupby("away_team_name")['away_team_name'].count()

    jogos_totais = jogosCasadf.iat[0] + jogosForadf.iat[0]


    resposta ={"Nome do Time":"Palmeiras",
            "Total de gols" : str(gols_totais),
            "Total de jogos" : str(jogos_totais)
            }
    return jsonify(resposta)

@app.route("/Botafogo/")
def pegarjogoscasaBotafogo():
    dados = pd.read_csv('./futebol.csv',sep=";")
    golsCasadf = dados.query('home_team_name == "Botafogo"')
    golsForadf = dados.query('away_team_name == "Botafogo"')

    golsCasa = golsCasadf.groupby('home_team_name')["home_team_goal_count"].sum()
    golsFora = golsForadf.groupby('away_team_name')["away_team_goal_count"].sum()

    gols_totais = golsCasa.iat[0] + golsFora.iat[0]

    jogosCasadf= golsCasadf.groupby("home_team_name")['home_team_name'].count()
    jogosForadf= golsForadf.groupby("away_team_name")['away_team_name'].count()

    jogos_totais = jogosCasadf.iat[0] + jogosForadf.iat[0]


    resposta ={"Nome do Time":"Botafogo",
            "Total de gols" : str(gols_totais),
            "Total de jogos" : str(jogos_totais)
            }
    return jsonify(resposta)
    
@app.route("/Real Madrid/")
def pegarjogoscasaRM():
    dados = pd.read_csv('./futebol.csv',sep=";")
    golsCasadf = dados.query('home_team_name == "Real Madrid"')
    golsForadf = dados.query('away_team_name == "Real Madrid"')

    golsCasa = golsCasadf.groupby('home_team_name')["home_team_goal_count"].sum()
    golsFora = golsForadf.groupby('away_team_name')["away_team_goal_count"].sum()

    gols_totais = golsCasa.iat[0] + golsFora.iat[0]

    jogosCasadf= golsCasadf.groupby("home_team_name")['home_team_name'].count()
    jogosForadf= golsForadf.groupby("away_team_name")['away_team_name'].count()

    jogos_totais = jogosCasadf.iat[0] + jogosForadf.iat[0]


    resposta ={"Nome do Time":"Real Madrid",
            "Total de gols" : str(gols_totais),
            "Total de jogos" : str(jogos_totais)
            }
    return jsonify(resposta)
    
@app.route("/juizes/")
def pegarjogosjuizes():
    dados = pd.read_csv('./futebol.csv',sep=";")
    juizes = dados.groupby("referee", dropna= True)["referee"].count()
    juizesdf = juizes.to_frame(name = 'jogos')
    resposta = juizesdf.to_dict("index")
    return jsonify(resposta)

# dados = pd.read_csv('./advertising.csv')
# ttvendas = dados.Vendas.sum()
# print(ttvendas)


app.run()