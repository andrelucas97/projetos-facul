import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# Produtos
lista_tag = [
    'alcohol free', 'Chemical Free', 'Canadian', 'Natural', 'Vegan'
]

st.sidebar.subheader('Filtros')

tag = st.sidebar.selectbox('Selecione a tag', lista_tag)

st.title(f'Produtos com a tag: {tag}')

response = requests.get(f'https://makeup-api.herokuapp.com/api/v1/products.json?product_tags={tag}')
df = pd.DataFrame(response.json())

df['price'] = pd.to_numeric(df['price'])

gp_marca = df.groupby(by='brand').mean('price')['price']
gp_produto = df.groupby(by='name').mean('price')['price']

fig, ax = plt.subplots()
ax.barh(gp_marca.index, gp_marca)
st.pyplot(fig)

fig2, ax2 = plt.subplots(figsize = (4.5, 10.5))
ax2.barh(gp_produto.index, gp_produto)
st.pyplot(fig2)

st.dataframe(gp_produto)
