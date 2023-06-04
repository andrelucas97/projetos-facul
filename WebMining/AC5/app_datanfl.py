import streamlit as st
import pandas as pd
import plotly.express as px 
import numpy as np

st.write(
    '''
    **NFL Web App**
    '''
)

def get_data():
    path = 'nfl.stats.csv'
    return pd.read_csv(path)

df = get_data()

#1 Gráfico de Caixa
st.sidebar.header('Gráfico de Caixa')
indicador = ['Todos']
indicador = st.sidebar.selectbox('Exibe todos os jogadores',indicador)
indicador=='Todos'

df = df.dropna(subset=['PassYds'])
q1 = np.percentile(df['PassYds'], 25)
q3 = np.percentile(df['PassYds'], 75)
iqr = q3 - q1
upper_limit = q3 + 1.5 * iqr
lower_limit = q1 - 1.5 * iqr

fig = px.box(df, x='PlayerName', y='PassYds', title="Gráfico de Caixa")
outliers = df[(df['PassYds'] > upper_limit) | (df['PassYds'] < lower_limit)]
st.plotly_chart(fig)
if not outliers.empty:
    outliers = ','.join(list(outliers['PlayerName']))
    st.markdown(f"O gráfico de caixa mostra que os Jogadores {outliers} possuem outliers")
else:
    st.markdown("O gráfico de caixa não possui outliers")

#2 Gráfico de Barras
st.sidebar.header('Gráfico de Barras')
st.sidebar.header('Selecione dois jogadores')
player1 = st.sidebar.selectbox('Jogador 1', df['PlayerName'].unique())
player2 = st.sidebar.selectbox('Jogador 2', df['PlayerName'].unique())

df1 = df[df['PlayerName']==player1]
df2 = df[df['PlayerName']==player2]
fig = px.bar(df1.append(df2), x='PlayerName', y='PassYds', color='PlayerName', barmode='group',title="Gráfico de Barras")
st.plotly_chart(fig)
st.markdown("O gráfico de barras compara dois jogadores em relação ao total de jardas percorridas com passes completos")

#3 Gráfico de Dispensão
fig = px.scatter(df, x='Cmp', y='YdsAtt', color='PlayerName',title="Gráfico de Dispensão")
st.plotly_chart(fig)
st.markdown("O gráfico de dispensão mostra a relação entre número de passes completados e jardas percorridas pelos jogadores")

#4 Gráfico de Pizza 
top5_jogadores = df.nlargest(5, 'Att')
fig = px.pie(top5_jogadores.groupby('PlayerName')['Att'].sum().reset_index(), values='Att', names='PlayerName',title="Gráfico de Pizza")
st.plotly_chart(fig)
st.markdown("O gráfico de pizza mostra o top 5 jogadores com mais tentativas de passe")

#5 Gráfico de Colunas
top10_jogadores = df.nlargest(10, 'TD')
fig = px.bar(top10_jogadores, x='PlayerName', y='TD', color='PlayerName',title="Gráfico de Colunas")
fig.update_layout(xaxis_title='Jogador', yaxis_title='Touchdowns')
st.plotly_chart(fig)
st.markdown("O gráfico de colunas mostra o top 10 jogadores com mais quantidades de touchdowns")

#6 Gráfico de Barras Empilhadas
top10_jogadores = df.nlargest(10, 'Att')
fig = px.bar(top10_jogadores, x='PlayerName', y=['Att', 'Lng'], title='Gráfico de Barras Empilhadas')
fig.update_layout(barmode='stack')
st.plotly_chart(fig)
st.markdown("O gráfico de barras empilhadas mostra o top 10 jogadores com o número de tentativa de passes --VS-- maior jogada em jardas realizada")
