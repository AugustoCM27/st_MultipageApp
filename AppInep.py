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
    
    st.subheader("Colaboradores")
    st.write("Arara, Bia, Isa, Nemo, Ximbinha, Meio, Juvi, Henrique, Felipe, Leonan, Pandinha, João Victor e Augusto")

with tab_analise:
    st.title("Análises e Gráficos")

    st.write("Esse espaço é reservado para as análises e gráficos feitos pela equipe do Projeto INEP")

    grafico = st.selectbox('Qual gráfico você gostaria de visualizar?',
                           ['Distribuições dos Dados - ENEM 2021', 'Mapas do Brasil - ENEM 2021', 'Notas médias por competência - ENEM 2021'])
    if grafico == 'Distribuições dos Dados - ENEM 2021':
        image = 'hist_dados_enem.png'
        st.image(image)
    elif grafico == 'Mapas do Brasil - ENEM 2021':
        image = 'mapas_dados_enem.png'
        st.image(image)
    elif grafico == 'Notas médias por competência - ENEM 2021':
        radio_but = st.radio("Qual competência você deseja visualizar?",
                            ('Ciências Naturais', 'Ciências Humanas', 'Linguagens e Códigos', 'Matemática', 'Redação'))
        if radio_but == 'Ciências Naturais':
            image = 'hist_dados_cn.png'
            st.image(image)
        elif radio_but == 'Ciências Humanas':
            image = 'hist_dados_ch.png'
            st.image(image)
        elif radio_but == 'Linguagens e Códigos':
            image = 'hist_dados_lc.png'
            st.image(image)
        elif radio_but == 'Matemática':
            image = 'hist_dados_mat.png'
            st.image(image)
        elif radio_but == 'Redação':
            image = 'hist_dados_red.png'
            st.image(image)

with tab_contato:
    st.title("Contato")
    st.subheader("Liga de Data Science - UNICAMP")

    st.subheader("Nossas redes sociais")
    st.write("Instagram: [@ligadsunicamp](https://instagram.com/ligadsunicamp?igshid=YmMyMTA2M2Y=)")
    st.write("GitHub: [LigaDS](https://github.com/LigaDS)")
    st.write("LinkedIn: [Liga de Data Science](https://www.linkedin.com/company/liga-de-data-science/about/)")
    st.write("LinkTree: [ligadsunicamp](https://linktr.ee/ligadsunicamp)")
    st.write("WordPress: [ligadsunicamp](https://ligadsunicamp.wordpress.com)")
       

    st.subheader("Onde nos encontrar")
    st.text("Faculdade de Ciências Aplicadas (FCA-UNICAMP)")
    st.text('Endereço: Rua Pedro Zaccaria, 1300, Limeira-SP, 13484-350')
