import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title='INEP - Análises',
    page_icon='📊'
)
st.title("Análises e Gráficos")

st.write("Esse espaço é reservado para as análises e gráficos feitos pela equipe do Projeto INEP")

st.write("Gráfico 1")
x = [0,1,2,3,4,5]
y = [0,1,4,9,16,25]
fig = plt.figure()
plt.plot(x,y,color='red')
plt.title("Título de teste")
plt.xlabel('x')
plt.ylabel('y')

st.pyplot(fig)