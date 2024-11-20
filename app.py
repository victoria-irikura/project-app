import pandas as pd
import plotly_express as px
import streamlit as st

car_data = pd.read_csv('https://raw.githubusercontent.com/victoria-irikura/project-app/refs/heads/main/vehicles.csv') # lendo os dados

st.header('Análise do dados de anúncios de vendas de carros')

# criar botão para geração do histograma
hist_button = st.button('Criar histograma')

if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# criar uma caixa de seleção
build_scatter = st.checkbox('Criar um histograma')


if build_scatter: # se a caixa de seleção for selecionada
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão para a coluna odometer')

    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


      