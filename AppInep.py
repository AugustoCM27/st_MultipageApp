import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from functools import reduce
import plotly.graph_objs as go
import plotly.express as px
import zipfile
import seaborn as sns

st.set_page_config(
    page_title='Liga DS - Projeto INEP',
    page_icon='🐼'
)

tab_home, tab_analise1, tab_analise2, tab_contato = st.tabs(['Página Inicial 🏠',
                                                             'AnálisesSprints 📊',
                                                             'AnálisesBETA',
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
    
    st.subheader("Colaboradores 🤜🤛")
    st.write("Arara, Bia, Isa, Nemo, Ximbinha, Meio, Juvi, Henrique, Felipe, Pandinha e Augusto")
    
with tab_analise1:
    st.title("Análises e Gráficos")

    st.write("Esse espaço é reservado para as análises e gráficos feitos pela equipe do Projeto INEP")
    st.text_area('*Descrição das atividades de cada Sprint*',
                 'Sprint 1: Análise exploratória do ENEM 2022 (histogramas e mapas)\n'
                 'Sprint 2: Evolução temporal das notas por competência, para cada UF [2018-2022]\n'
                 'Sprint 3: Influência de aspectos sociais no desempenho no ENEM 2022')
    sprint = st.selectbox('*Qual sprint você gostaria de visualizar?*',
                          ['Sprint 1', 'Sprint 2', 'Sprint 3'])

    if sprint == 'Sprint 1':
        st.write('Adicionar os gráficos e análises do Sprint 1')
        radio_analise = st.radio(f"*Qual análise do {sprint} você gostaria de ver?*",
                                 ('Estatísticas das competências',
                                  'Distribuições dos participantes (Histogramas)',
                                  'Análises por UF (Mapas)'))
        
        df_spt1 = pd.read_csv('MICRODADOS_ENEM_2022_spt1.zip', compression='zip', delimiter=';')
        
        if radio_analise == 'Estatísticas das competências':
            st.write(df_spt1[["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO"]].describe())
        elif radio_analise == 'Distribuições dos participantes (Histogramas)':
            st.text('Adicionar os histogramas e comentários/conclusões')
            st.text('Adicionar link do colab')
        elif radio_analise == 'Análises por UF (Mapas)':
            st.text('Adicionar os mapas e comentários/conclusões')
            st.text('Adicionar link do colab')
            
    elif sprint == 'Sprint 2':
        st.write('Adicionar os gráficos e análises do Sprint 2')
        def df_unzip(ano):
            df = pd.read_csv(f'MICRODADOS_ENEM_{ano}_spt2.zip', compression='zip', delimiter=';')
            return df

        df2018 = df_unzip(2018)
        df2019 = df_unzip(2019)
        df2020 = df_unzip(2020)
        df2021 = df_unzip(2021)
        df2022 = df_unzip(2022)

        # criando uma função para tratamento dos dados
        # agrupando por estado e tirando a média das notas
        def f(x):
            for df in x:
                CN = df['NU_NOTA_CN'].groupby(df['SG_UF_PROVA'])
                df_cn = pd.DataFrame(CN.mean())
                CH = df['NU_NOTA_CH'].groupby(df['SG_UF_PROVA'])
                df_ch = pd.DataFrame(CH.mean())
                MT = df['NU_NOTA_MT'].groupby(df['SG_UF_PROVA'])
                df_mt = pd.DataFrame(MT.mean())
                LC = df['NU_NOTA_LC'].groupby(df['SG_UF_PROVA'])
                df_lc = pd.DataFrame(LC.mean())
                RED = df['NU_NOTA_REDACAO'].groupby(df['SG_UF_PROVA'])
                df_red = pd.DataFrame(RED.mean())
                # juntando tudo num único df:
                lista_df = [df_ch, df_cn, df_mt, df_lc, df_red]
                df_notas = reduce(lambda left,right: pd.merge(left,right,on=['SG_UF_PROVA'], how='outer'), lista_df)
                return df_notas

        # aplicando a função em todas as bases importadas
        listas_df = [[df2022], [df2021], [df2020], [df2019], [df2018]]
        listas_trat = []
        for i in range(0, len(listas_df)):
            listas_trat.append(f(listas_df[i]))

        # atribuindo as novas bases de dados à um df
        # notas médias de cada ano
        df22 = listas_trat[0]
        df21 = listas_trat[1]
        df20 = listas_trat[2]
        df19 = listas_trat[3]
        df18 = listas_trat[4]

        def df_competencia(competencia):
            df = pd.concat([df18[competencia],
                            df19[competencia],
                            df20[competencia],
                            df21[competencia],
                            df22[competencia]], axis=1)
            df.columns = ['2018', '2019', '2020', '2021', '2022']
            return df

        df_red = df_competencia('NU_NOTA_REDACAO')
        df_mat = df_competencia('NU_NOTA_MT')
        df_ch = df_competencia('NU_NOTA_CH')
        df_cn = df_competencia('NU_NOTA_CN')
        df_lc = df_competencia('NU_NOTA_LC')

        # dicionário para atribuir cada sigla a sua região
        regioes = {
            'AC': 'Norte','AL': 'Nordeste','AP': 'Norte','AM': 'Norte','BA': 'Nordeste','CE': 'Nordeste','DF': 'Centro-Oeste','ES': 'Sudeste',
            'GO': 'Centro-Oeste','MA': 'Nordeste','MT': 'Centro-Oeste','MS': 'Centro-Oeste','MG': 'Sudeste','PA': 'Norte','PB': 'Nordeste','PR': 'Sul','PE': 'Nordeste',
            'PI': 'Nordeste','RJ': 'Sudeste','RN': 'Nordeste','RS': 'Sul','RO': 'Norte','RR': 'Norte','SC': 'Sul','SP': 'Sudeste','SE': 'Nordeste','TO': 'Norte'
        }

        # função para atribuição
        def cat_reg(df):
            df['Região'] = df.index.map(regioes)
            df['UF'] = df.index
            df = df.reset_index()
            return df

        # aplicando a função
        df_red = cat_reg(df_red)
        df_mat = cat_reg(df_mat)
        df_cn = cat_reg(df_cn)
        df_ch = cat_reg(df_ch)
        df_lc = cat_reg(df_lc)

        # função para criar o novo df
        def melted(df):
            df_melted = pd.melt(df.reset_index(), id_vars = 'UF', value_vars=['2018', '2019', '2020', '2021', '2022'], var_name='ano')
            df_melted = df_melted.rename(columns = {'value': 'Média da nota'})
            return df_melted

        # aplicando a função
        df_melted_red = melted(df_red)
        df_melted_mat = melted(df_mat)
        df_melted_cn = melted(df_cn)
        df_melted_ch = melted(df_ch)
        df_melted_lc = melted(df_lc)

        # função para plotar a figura
        def figura(df, df_comp, competencia):
            fig = px.line(df, x='ano', y='Média da nota', color='UF')

            fig.update_layout(title=f'Média das notas de {competencia} por estado, por ano', xaxis_title='Anos',
                              yaxis_title='Média das notas')

            fig.update_layout(
               updatemenus=[dict(
                  buttons=list([
                    dict(label='Todos',
                         method='update',
                         args=[{'visible': True}]),
                    dict(label='Centro-Oeste',
                         method='update',
                         args=[{'visible': df_comp['Região'] == 'Centro-Oeste'}]),
                    dict(label='Nordeste',
                         method='update',
                         args=[{'visible': df_comp['Região'] == 'Nordeste'}]),
                    dict(label='Norte',
                         method='update',
                         args=[{'visible': df_comp['Região'] == 'Norte'}]),
                    dict(label='Sudeste',
                         method='update',
                         args=[{'visible': df_comp['Região'] == 'Sudeste'}]),
                    dict(label='Sul',
                         method='update',
                         args=[{'visible': df_comp['Região'] == 'Sul'}])
                  ]))])
            return fig

        fig_red = figura(df_melted_red, df_red, 'redação')
        fig_mat = figura(df_melted_mat, df_mat, 'matemática')
        fig_ch = figura(df_melted_ch, df_ch, 'ciências humanas')
        fig_lc = figura(df_melted_lc, df_lc, 'linguagens e códigos')
        fig_cn = figura(df_melted_cn, df_cn, 'ciências da natureza')

        escolha_radio = st.radio("Qual competência você deseja ver?", ["Redação", "Matemática", "Ciências Humanas", "Linguagens e Códigos", "Ciências da Natureza"])
        if escolha_radio == 'Redação':
            st.plotly_chart(fig_red)
        elif escolha_radio == 'Matemática':
            st.plotly_chart(fig_mat)
        elif escolha_radio == 'Ciências Humanas':
            st.plotly_chart(fig_ch)
        elif escolha_radio == 'Linguagens e Códigos':
            st.plotly_chart(fig_lc)
        elif escolha_radio == 'Ciências da Natureza':
            st.plotly_chart(fig_cn)
        
    elif sprint == 'Sprint 3':
        st.write('Adicionar os gráficos e análises do Sprint 3')
        
with tab_analise2:
    st.title("Análises e Gráficos")

    st.write("Esse espaço é reservado para as análises e gráficos feitos pela equipe do Projeto INEP")

    grafico = st.selectbox('Qual gráfico você gostaria de visualizar?',
                           ['Distribuições dos Dados - ENEM 2021', 'Mapas do Brasil - ENEM 2021', 'Notas médias por competência - ENEM 2021'])
    if grafico == 'Distribuições dos Dados - ENEM 2021':
        image = 'spt1_hist.png'
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
