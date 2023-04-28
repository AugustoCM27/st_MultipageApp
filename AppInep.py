import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(
    page_title='Liga DS - Projeto INEP',
    page_icon='🐼'
)

tab_home, tab_analise, tab_contato = st.tabs(['Página Inicial 🏠',
                                              'Análises 📊',
                                              'Contato 📞'])
with tab_home:
    st.title('Bem-vindo(a) ao Projeto INEP 😎')

    st.subheader('Ficamos felizes com o seu interesse em nosso projeto! Conheça mais sobre ele e veja nossos resultados!')

    st.write("O Projeto INEP é uma iniciativa da Liga de Data Science - Unicamp,"
            " na qual o objetivo é analisar e compreender as informações fornecidas"
            " pelas bases de dados do ENEM ao longo do tempo, utilizando-se da linguagem de programação"
            " Python. Em paralelo, buscamos aprender e aprimorar conceitos de programação e DA a medida que atingimos nossos objetivos e"
            " superamos desafios!")
    st.write("Esperamos que você goste do conteúdo!")
    
    image_logo = 'logo_ds.png'
    st.image(image_logo)

with tab_analise:
    st.title("Análises e Gráficos")

    st.write("Esse espaço é reservado para as análises e gráficos feitos pela equipe do Projeto INEP")

    grafico = st.selectbox('Qual gráfico você gostaria de visualizar?',
                           ['Distribuições dos Dados - ENEM 2021', 'Mapas do Brasil - ENEM 2021', 'Notas médias por UF - ENEM 2021'])
    if grafico == 'Distribuições dos Dados - ENEM 2021':
        image = 'hist_dados_enem.png'
        st.image(image)
    elif grafico == 'Mapas do Brasil - ENEM 2021':
        image = 'mapas_dados_enem.png'
        st.image(image)
    elif grafico == 'Notas médias por UF - ENEM 2021':
        image = 'hist_notas_enem_estado.png'
        st.image(image)

with tab_contato:
    st.title("Contato")
    st.subheader("Liga de Data Science - UNICAMP")

    st.subheader("Nossas redes sociais")
    st.write("Instagram: [@ligadsunicamp](https://instagram.com/ligadsunicamp?igshid=YmMyMTA2M2Y=)")
    st.write("GitHub: (adicionar aqui)")
    st.write("LinkedIn: (adicionar aqui)")

    st.subheader("Onde nos encontrar")
    st.text("Faculdade de Ciências Aplicadas (FCA-UNICAMP)")
    st.text('Endereço: Rua Pedro Zaccaria, 1300, Limeira-SP, 13484-350')
