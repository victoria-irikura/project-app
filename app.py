import pandas as pd
import plotly_express as px
import streamlit as st

car_data = pd.read_csv('https://raw.githubusercontent.com/victoria-irikura/project-app/refs/heads/main/vehicles.csv') # lendo os dados

st.header('Análise do dados de anúncios de vendas de carros')

st.write('Histograma de km rodados pelos veículos')
# criar botão para geração do histograma
hist_button = st.button('Criar histograma')

if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

st.write('Gráfico de dispersão tipo de veículo vs preço')
# criar uma caixa de seleção
build_scatter = st.checkbox('Criar gráfico de dispersão')

if build_scatter: # se a caixa de seleção for selecionada
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão para a coluna tipo de veículo')

    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="type", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


      