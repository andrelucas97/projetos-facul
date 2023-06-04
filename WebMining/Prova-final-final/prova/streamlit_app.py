import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px
import os.path

st.write(
    '''
    **NFL WebApp**
    '''
)

st.sidebar.header('Gráficos sobre dados de cada jogador da NFL')

def get_data():
    file = 'nfl.stats.csv'  
    path = os.path.join(os.path.dirname(__file__), file)
    return pd.read_csv(path, sep = ',')

df = get_data()

indicador = ['Touchdown', 'Interceptação', 'Média Touchdown', 'Média Interceptações', 'Longest', 'Sack']

escolha_indicador = st.sidebar.selectbox('Escolha o indicador', indicador)

if escolha_indicador == 'Touchdown':

    df = df.set_index(df['PlayerName'].astype(str))

    st.header('Touchdown:' )
    st.write('Número de Touchdowns feito por cada jogador')
    st.bar_chart(df['TD'])

elif escolha_indicador == 'Interceptação':
    df = df.set_index(df['PlayerName'].astype(str))

    st.header('Interceptações:' )
    st.write('Número de Interceptações feito por cada jogador')

    st.bar_chart(df['INT1'])

elif escolha_indicador == 'Média Touchdown':

    st.header('Média Touchdown:' )
    st.write('Uma média de Touchdown por jogador em grafico Box plot' )

    df2 = df.copy()
    stock = df['TD'].drop_duplicates()
    df = df.set_index(df['TD'].astype(str))

    def grafico_plotly(base):
        fig = px.box(base.TD)
        return st.plotly_chart(fig)
    

    grafico_plotly(df2)

    q1, q3 = np.percentile(df2['TD'], [25, 75])
    iqr = q3 - q1
    lim_inf = q1 - (1.5 * iqr)
    lim_sup = q3 + (1.5 * iqr)

    outL = df2.loc[(df2['TD'] < lim_inf) | (df2['TD'] > lim_sup)]

    if len(outL) > 0:
        st.write('Este gráfico Box Plot possui outliers')
    else:
        st.write('Este gráfico Box Plot não possui outliers')

elif escolha_indicador == 'Média Interceptações':

    st.header('Média Interceptações:' )
    st.write('Uma média de Interceptações por jogador em grafico Box plot' )


    df2 = df.copy()
    stock = df['INT1'].drop_duplicates()
    df = df.set_index(df['INT1'].astype(str))

    def grafico_plotly2(base):
        fig2 = px.box(base.INT1)
        return st.plotly_chart(fig2)

    grafico_plotly2(df2)

    q1, q3 = np.percentile(df2['INT1'], [25, 75])
    iqr = q3 - q1
    lim_inf = q1 - (1.5 * iqr)
    lim_sup = q3 + (1.5 * iqr)

    outL = df2.loc[(df2['INT1'] < lim_inf) | (df2['INT1'] > lim_sup)]

    if len(outL) > 0:
        st.write('Este gráfico Box Plot possui outliers')
    else:
        st.write('Este gráfico Box Plot não possui outliers')

elif escolha_indicador == 'Longest':

    st.header('Longest:' )
    st.write('Jogada mais longa de cada jogador' )


    df2 = df.copy()
    stock = df['Lng'].drop_duplicates()
    df = df.set_index(df['Lng'].astype(str))

    def grafico_plotly3(base):
        fig3 = px.bar(df, x = 'PlayerName', y = 'Lng')
        return st.plotly_chart(fig3)
    
    grafico_plotly3(df2)

elif escolha_indicador == 'Sack':
    sack_order = df.groupby('PlayerName')['Sck'].sum().sort_values(ascending=False).iloc[:10]

    df2 = df.copy()
    df = df[df['PlayerName'].isin(sack_order.index)]

    def grafico_plotly4(base):
        fig4 = px.bar(df, x = 'PlayerName', y = 'Sck')
        return st.plotly_chart(fig4)
    
    st.header('Sack:' )   
    st.write('Ação de derrubar o quarterback (QB) adversário atrás da linha de scrimmage antes que ele possa lançar a bola')
    st.write('Dados dos 10 jogadores que tiveram uma pontuação mais alta no "Sack"')

    grafico_plotly4(df2)
    sack_order

    
