import streamlit as st
import matplotlib.pyplot as plt
#import Pages

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
    
    #st.write("Testando se o aplicativo atualiza automaticamente")

with tab_analise:
    st.title("Análises e Gráficos")

    st.write("Esse espaço é reservado para as análises e gráficos feitos pela equipe do Projeto INEP")

    grafico = st.selectbox('Qual gráfico você gostaria de visualizar?',
                           ['Gráfico 1', 'Gráfico 2', 'Gráfico 3'])
    if grafico == 'Gráfico 1':
        x = [0, 1, 2, 3, 4, 5]
        y = [0, 1, 4, 9, 16, 25]
        fig = plt.figure()
        plt.plot(x, y, color='red')
        plt.title("Título de teste")
        plt.xlabel('x')
        plt.ylabel('y')
        st.pyplot(fig)
    elif grafico == 'Gráfico 2':
        x = [0, 1, 2, 3, 4, 5]
        y = [0, 1, 2, 3, 4, 5]
        fig = plt.figure()
        plt.plot(x, y, color='red')
        plt.title("Título de teste")
        plt.xlabel('x')
        plt.ylabel('y')
        st.pyplot(fig)
    elif grafico == 'Gráfico 3':
        x = [0, 1, 2, 3, 4, 5]
        y = [0, 1, 1, 2, 3, 5]
        fig = plt.figure()
        plt.plot(x, y, color='red')
        plt.title("Título de teste")
        plt.xlabel('x')
        plt.ylabel('y')
        st.pyplot(fig)

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
#from PIL import Image
#img = Image.open("logo_ds.png")

# display image using streamlit
# width is used to set the width of an image
#st.image(img, width=200)
