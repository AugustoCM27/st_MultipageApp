import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from functools import reduce
import plotly.graph_objs as go
import plotly.express as px
import zipfile
import seaborn as sns
#!pip install geobr
import geobr
import shapely
import warnings
from shapely.errors import ShapelyDeprecationWarning
warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning);
import descartes
#import os

# edição bia - teste mudança de cores
# Read the contents of the styles.css file
#with open('styles.css', 'r') as f:
#    css = f.read()

# Apply the custom CSS
#st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
# fim edição bia

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
    
    st.subheader("Colaboradores 🤜🤛")
    st.write("Arara, Bia, Isa, Nemo, Ximbinha, Meio, Juvi, Henrique, Felipe, Pandinha e Augusto")
    
with tab_analise:
    st.title("Análises e Gráficos")

    st.write("Esse espaço é reservado para as análises e gráficos feitos pela equipe do Projeto INEP")
    expander = st.expander('*Descrição das atividades de cada Sprint*')
    expander.write('Sprint 1: Análise exploratória do ENEM 2022 (histogramas e mapas)')
    expander.write('Sprint 2: Evolução temporal das notas por competência, para cada UF [2018-2022]')
    expander.write('Sprint 3: Influência de aspectos sociais no desempenho no ENEM 2022')
    
    sprint = st.selectbox('*Qual sprint você gostaria de visualizar?*',
                          ['Sprint 1', 'Sprint 2', 'Sprint 3'])

    if sprint == 'Sprint 1':
        st.write('Adicionar os gráficos e análises do Sprint 1')
        radio_analise = st.radio(f"*Qual análise do {sprint} você gostaria de ver?*",
                                 ('Estatísticas das competências',
                                  'Distribuições dos participantes (Histogramas)',
                                  'Análises por UF (Mapas)',
                                  'Nota média dos candidatos por região'))
        
        
        
        if radio_analise == 'Estatísticas das competências':
            ano = st.slider("Qual ano você deseja visualizar as estatísticas das competências?", 2014, 2022)
            df = pd.read_csv(f'MICRODADOS_ENEM_{int(ano)}.zip', compression='zip', delimiter=';')
            st.write(df[["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO"]].describe())
            
        elif radio_analise == 'Distribuições dos participantes (Histogramas)':
            st.text('Adicionar os histogramas e comentários/conclusões')
            #df = pd.read_csv('MICRODADOS_ENEM_2022_spt1.zip', compression='zip', delimiter=';')
            ano = st.slider("Qual ano você deseja visualizar as distribuições?", 2014, 2022)
            df = pd.read_csv(f'MICRODADOS_ENEM_{int(ano)}.zip', compression='zip', delimiter=';')
            # Dicionário de mapeamento das categorias para intervalos
            faixas_etarias = {
                1: '-17',2: '17',3: '18',4: '19',5: '20',6: '21',7: '22',8: '23',9: '24',10: '25',11: '26-30',
                12: '31-35',13: '36-40',14: '41-45',15: '46-50',16: '51-55',17: '56-60',18: '61-65',19: '66-70',20: '70+'}
            # Substituir os valores da coluna "Faixa Etária" pelos intervalos correspondentes
            df['TP_FAIXA_ETARIA'] = df['TP_FAIXA_ETARIA'].map(faixas_etarias)

            nacionalidades = {0: 'Não informado',1: 'Brasileiro(a)',2: 'Brasileiro(a) Naturalizado(a)',3: 'Estrangeiro(a)',4: 'Brasileiro(a) Nato(a), nascido(a) no exterior'}
            df['TP_NACIONALIDADE'] = df['TP_NACIONALIDADE'].map(nacionalidades)

            cor_raca = {0: 'Não declarado',1: 'Branca',2: 'Preta',3: 'Parda',4: 'Amarela',5: 'Indígena',6: 'Não dispõe informação'}
            df['TP_COR_RACA'] = df['TP_COR_RACA'].map(cor_raca)

            escolas = {1: 'Não respondeu',2: 'Pública',3: 'Privada'}
            df['TP_ESCOLA'] = df['TP_ESCOLA'].map(escolas)
            
            hist = plt.figure()
            histograma = st.radio("Qual distribuição você deseja visualizar?",
                                  ['Faixa Etária', 'Nacionalidade', 'Cor/Raça', 'Tipo de Escola'])
            if histograma == 'Faixa Etária':
                hist_ref = sns.histplot(sorted(df["TP_FAIXA_ETARIA"]), stat='count', binwidth=1, color='blue')
                sns.histplot(sorted(df["TP_FAIXA_ETARIA"]), stat='count', binwidth=1, color='blue')
                # Posição dos xticks vai ser o limite direito da barra 
                # mais metade de seu comprimento
                xticks = [rec.get_x() + 0.5*hist_ref.patches[0].get_width() for rec in list(hist_ref.patches)]
                plt.xticks(xticks, rotation=90, fontsize=8)
                plt.yticks(fontsize=8)
                plt.xlabel('Idades (anos)', fontsize=8)
                plt.ylabel('Quantidade', fontsize=8)
                plt.title("Distribuição da Faixa Etária", fontsize=8)
                st.pyplot(hist)
            elif histograma == 'Nacionalidade':
                sns.histplot(df.loc[df["TP_NACIONALIDADE"]!='Brasileiro(a)', "TP_NACIONALIDADE"], binwidth=1)
                plt.xticks(rotation=10, fontsize=5)
                plt.yticks(fontsize=8)
                plt.xlabel('Situação', fontsize=8)
                plt.ylabel('Quantidade', fontsize=8)
                plt.title("Distribuição da Nacionalidade sem Brasileiros Nascidos", fontsize=8)
                st.pyplot(hist)
            elif histograma == 'Cor/Raça':
                sns.histplot(df["TP_COR_RACA"], binwidth=1)
                plt.xticks(rotation=10, fontsize=8)
                plt.yticks(fontsize=8)
                plt.xlabel('Cor / Raça', fontsize=8)
                plt.ylabel('Quantidade', fontsize=8)
                plt.title("Distribuição da Cor/Raça", fontsize=8)
                st.pyplot(hist)
            elif histograma == 'Tipo de Escola':
                sns.histplot(df['TP_ESCOLA'])
                plt.xticks(rotation=0, fontsize=8)
                plt.yticks(fontsize=8)
                plt.xlabel('Tipo de escola', fontsize=8)
                plt.ylabel('Quantidade', fontsize=8)
                plt.title("Distribuição da Tipo de Escola", fontsize=8)
                st.pyplot(hist)
                
            st.text('Adicionar link do colab')
        elif radio_analise == 'Análises por UF (Mapas)':
            st.text('Adicionar os mapas e comentários/conclusões')
            
            df = pd.read_csv('MICRODADOS_ENEM_2022_spt1.zip', compression='zip', delimiter=';')
            UFs = df["SG_UF_PROVA"].unique()
            variables = {"TP_ENSINO": 2,  # Educação especial
            "TP_ESCOLA": 3,  #Escola privada
            "TP_COR_RACA": 1,   # Brancos 
            "TP_SEXO": "F", 
            "TP_DEPENDENCIA_ADM_ESC": 1, # Federal 
            "TP_PRESENCA_CN": 1, # Presente Prova de Ciencias da Natureza
            "TP_PRESENCA_CH": 1, # Presente Prova de Ciencias Humanas
            "TP_PRESENCA_LC": 1, # Presente Prova de Linguagem
            "TP_PRESENCA_MT": 1} # Presente Prova de Matemática
            translation = {"TP_ENSINO": "Educação especial",
            "TP_ESCOLA": "Escola privada",
            "TP_COR_RACA": "Brancos",
            "TP_SEXO": "Mulheres", 
            "TP_DEPENDENCIA_ADM_ESC": "Federal" ,
            "TP_PRESENCA_CN": "Presença Ciencias da Natureza",
            "TP_PRESENCA_CH": "Presença Ciencias Humanas",
            "TP_PRESENCA_LC": "Presença Linguagem",
            "TP_PRESENCA_MT": "Presença Matemática",
            "AcessoInternet": "Acesso a Internet"
            }
            titles = {"Educação especial": "Prop. de Candidatos em Educação Especial",
            "Escola privada": "Prop. Candidatos de Escolas Privadas",
            "Brancos": "Índice de Diversidade de Cor",
            "Mulheres": "Prop. de Candidatas Mulheres", 
            "Federal":  "Prop. de Candidatos de Escolas Federais",
            "Presença Ciencias da Natureza": "Presença Ciencias da Natureza",
            "Presença Ciencias Humanas": "Presença Ciencias Humanas",
            "Presença Linguagem": "Presença Linguagem",
            "Presença Matemática": "Presença Matemática",
            "Acesso a Internet": "Taxa de Acesso a Internet"
            }
            
            dfProportion = pd.DataFrame()
            for factor in variables.keys():
                for UF in UFs:
                    if factor == "TP_COR_RACA":
                        proportion = df.loc[df["SG_UF_PROVA"]==UF, factor].value_counts().drop(0)
                        diversity_index = 1/((proportion/proportion.sum())**2).sum() # Simpson’s Index invertido '1/D'
                        dfProportion.loc[UF, translation[factor]] = diversity_index
                    else:
                        proportion = df.loc[df["SG_UF_PROVA"]==UF, factor].value_counts(normalize=True)[variables[factor]]
                        dfProportion.loc[UF, translation[factor]] = proportion
            # agrupando por estado e contando o número de ocorrências de cada valor categórico
            # A: Sem acesso // B: Com acesso
            df_net = df.groupby(['SG_UF_PROVA', 'Q025']).size().unstack(fill_value=0)
            # criando uma coluna com o percentual de acesso a internet por estado
            df_net['Acesso a Internet'] = df_net['B']/(df_net['A'] + df_net['B'])
            dfProportion = dfProportion.merge(df_net, how='left', left_index=True, right_index=True)

            br = geobr.read_state()
            df_t = br.merge(dfProportion, how="left", left_on="abbrev_state", right_index=True)
            
            plt.rcParams.update({"font.size": 3});
            quant_figuras = len(translation.values())
            fig, axs = plt.subplots((quant_figuras+1)//2, 2, figsize=(4, 12), dpi=400);
            for idx in range(quant_figuras):
                row = idx//2
                col = idx%2
                factor = list(translation.values())[idx]
                df_t.plot(
                    column=factor,
                    cmap="Blues",
                    legend=True,
                    legend_kwds={
                        #"label": factor,
                        "orientation": "horizontal",
                        "shrink": 0.4,
                    },
                    ax=axs[row, col],
                );
                axs[row, col].set_title(titles[factor])
                axs[row, col].axis("off");
            st.pyplot(fig)
            st.text('Adicionar link do colab')
        
        #edição bia - adicionei os histogramas lgbt
        #escolha_radio = st.radio("Qual competência você deseja ver?", ["Redação", "Matemática", "Ciências Humanas", "Linguagens e Códigos", "Ciências da Natureza"])
        elif radio_analise == 'Nota média dos candidatos por região':
            ano = st.slider("Qual ano você deseja visualizar as distribuições?", 2014, 2022)
            escolha_radio = st.radio("Qual competência você deseja ver?", ["Redação", "Matemática", "Ciências Humanas", "Linguagens e Códigos", "Ciências da Natureza"])
            df = pd.read_csv(f'MICRODADOS_ENEM_{ano}_spt2.zip', compression='zip', delimiter=';')
            #CN = df['NU_NOTA_CN'].groupby(df['SG_UF_PROVA'])
            #df_cn = pd.DataFrame(CN.mean())
            def f(comp, y):
              c = df['NU_NOTA_'+str(comp)].groupby(df['SG_UF_PROVA'])
              df_comp = pd.DataFrame(c.mean()) # criando um data frame com a média da competência em cada um dos estados
              hist_comp = plt.figure(figsize=(10,10))
              df_comp_sorted = df_comp.sort_values(by='NU_NOTA_'+str(comp), ascending=True)
              sns.histplot(x = df_comp_sorted.index, weights = df_comp_sorted['NU_NOTA_'+str(comp)], legend = False, binwidth = 1, hue = df_comp.index, palette = 'gist_ncar') # fazendo um histograma, no qual, no eixo x são os estados, e no eixo y a média de notas
              plt.ylim(min(df_comp[f'NU_NOTA_{comp}'])-50, max(df_comp[f'NU_NOTA_{comp}'])+170) # fiz isso apenas pra deixar todos numa escala igual
              plt.xlabel('UF')
              plt.ylabel('Média da nota')
              plt.title(y)
              return hist_comp
            
            if escolha_radio == 'Redação':
                st.pyplot(f('REDACAO', escolha_radio))
            elif escolha_radio == 'Matemática':
                st.pyplot(f('MT', escolha_radio))
            elif escolha_radio == 'Ciências Humanas':
                st.pyplot(f('CH', escolha_radio))
            elif escolha_radio == 'Linguagens e Códigos':
                st.pyplot(f('LC', escolha_radio))
            elif escolha_radio == 'Ciências da Natureza':
                st.pyplot(f('CN', escolha_radio))
          #fim da minha alteração
        
    elif sprint == 'Sprint 2':
        st.write('Adicionar os gráficos e análises do Sprint 2')
        def df_unzip(ano):
            df = pd.read_csv(f'MICRODADOS_ENEM_{ano}_spt2.zip', compression='zip', delimiter=';')
            return df
        
        df2014 = df_unzip(2014)
        df2015 = df_unzip(2015)
        df2016 = df_unzip(2016)
        df2017 = df_unzip(2017)
        df2018 = df_unzip(2018)
        df2019 = df_unzip(2019)
        df2020 = df_unzip(2020)
        df2021 = df_unzip(2021)
        df2022 = df_unzip(2022)
        
        # Criando uma nova coluna no DataFrame que associa cada estado à sua respectiva macroregião
        def df_addreg(df):
          df['Região'] = df['SG_UF_PROVA'].map(regioes)
          return df
        
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
        
        escolha_spt2 = st.radio("Qual análise do Sprint 2 você deseja ver?",
                                ["Análise temporal das notas", "Média das notas por região do Brasil"])
        if escolha_spt2 == "Análise temporal das notas":           
            # aplicando a função em todas as bases importadas
            listas_df = [[df2022], [df2021], [df2020], [df2019], [df2018], [df2017], [df2016], [df2015], [df2014]]
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
            df17 = listas_trat[5]
            df16 = listas_trat[6]
            df15 = listas_trat[7]
            df14 = listas_trat[8]

            def df_competencia(competencia):
                df = pd.concat([df14[competencia],
                                df15[competencia],
                                df16[competencia],
                                df17[competencia],
                                df18[competencia],
                                df19[competencia],
                                df20[competencia],
                                df21[competencia],
                                df22[competencia]], axis=1)
                df.columns = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
                return df

            df_red = df_competencia('NU_NOTA_REDACAO')
            df_mat = df_competencia('NU_NOTA_MT')
            df_ch = df_competencia('NU_NOTA_CH')
            df_cn = df_competencia('NU_NOTA_CN')
            df_lc = df_competencia('NU_NOTA_LC')
            # aplicando a função
            df_red = cat_reg(df_red)
            df_mat = cat_reg(df_mat)
            df_cn = cat_reg(df_cn)
            df_ch = cat_reg(df_ch)
            df_lc = cat_reg(df_lc)

            # função para criar o novo df
            def melted(df):
                df_melted = pd.melt(df.reset_index(), id_vars = 'UF', value_vars=['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'], var_name='ano')
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
                
        if escolha_spt2 == "Média das notas por região do Brasil":
            ano = st.slider("Qual ano você deseja visualizar?", 2014, 2022)
            df_ano = df_unzip(int(ano))
            df_ = df_addreg(df_ano)
   
            #Adicionando a coluna de regiao
            def media_reg(df):
              media_regiao = df.groupby('Região').mean(numeric_only=True)
              # Criando uma nova coluna com a soma das notas
              media_regiao['Soma'] = media_regiao['NU_NOTA_CN'] + media_regiao['NU_NOTA_CH'] + media_regiao['NU_NOTA_LC'] + media_regiao['NU_NOTA_MT'] + media_regiao['NU_NOTA_REDACAO']
              return media_regiao

            def fig_plot(media_regiao, ano):
              fig = go.Figure()
              # Adicionando traços de barra para cada disciplina
              fig.add_trace(go.Bar(x=media_regiao.index, y=media_regiao['NU_NOTA_CN'], name='Ciências da Natureza'))
              fig.add_trace(go.Bar(x=media_regiao.index, y=media_regiao['NU_NOTA_CH'], name='Ciências Humanas'))
              fig.add_trace(go.Bar(x=media_regiao.index, y=media_regiao['NU_NOTA_LC'], name='Linguagens e Códigos'))
              fig.add_trace(go.Bar(x=media_regiao.index, y=media_regiao['NU_NOTA_MT'], name='Matemática'))
              fig.add_trace(go.Bar(x=media_regiao.index, y=media_regiao['NU_NOTA_REDACAO'], name='Redação'))
              # Adicionando um trace de linha com a soma das notas
              fig.add_trace(go.Scatter(x=media_regiao.index, y=media_regiao['Soma'], name='Soma das notas'))
              # Configurando layout do gráfico
              fig.update_layout(barmode='stack', title=f'Média das notas do ENEM {ano} por região',
                                xaxis_title='Região', yaxis_title='Média das notas')
              # Exibindo o gráfico
              return fig
        
            media_regiao = media_reg(df_)
            st.plotly_chart(fig_plot(media_regiao, int(ano))) 
           
    elif sprint == 'Sprint 3':
        st.write('Adicionar os gráficos e análises do Sprint 3')
        
        def df_unzip_convert(ano):
            df = pd.read_csv(f'MICRODADOS_ENEM_{ano}.zip', compression='zip', delimiter=';')
            colunas_converter = ['TP_FAIXA_ETARIA', 'TP_ESTADO_CIVIL', 'TP_COR_RACA', 'TP_NACIONALIDADE', 'TP_ESCOLA']
            df[colunas_converter] = df[colunas_converter].astype(str)
            return df
        
        #ano = st.selectbox('Selecione um ano', ['2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014'])
        ano = st.slider("Selecione um ano", 2014, 2022)
        
        df = df_unzip_convert(ano)
        
        df = df.rename(columns={'NU_NOTA_CN': 'Ciências da Natureza', 'NU_NOTA_CH': 'Ciências Humanas', 'NU_NOTA_LC': 'Linguagens e Códigos', 'NU_NOTA_MT': 'Matemática', 'NU_NOTA_REDACAO': 'Redação'})
        df = df.rename(columns={'TP_SEXO':'Sexo', 'TP_COR_RACA':'Cor/Raça', 'TP_FAIXA_ETARIA':'Faixa Etária', 'TP_ESTADO_CIVIL':'Estado Civil', 'TP_NACIONALIDADE':'Nacionalidade','TP_ESCOLA':'Tipo de Escola'})
        
        def distrib(df, competencia, param):
          x = df[competencia].groupby(df[param])
          df_x = pd.DataFrame(x.mean())
          # Definindo as legendas
          leg_Sexo = ['Masculino', 'Feminino']
          leg_Cor = ['Não declarado', 'Branca', 'Preta', 'Parda', 'Amarela', 'Indígena']
          leg_Nacionalidade = ['Não informada', 'Brasileiro', 'Brasileiro naturalizado', 'Estrangeiro','Brasileiro nascido no exterior']
          leg_EstadoCivil = ['Não informado', 'Solteiro', 'Casado', 'Divorciado', 'Viúvo']
          leg_tp_escola = ['Não respondeu', 'Pública', 'Privada', 'Exterior']
          leg_Faixa_etária = ['menor de 17', '17', '18', '19', '20', '21', '22', '23', '24', '25', 'entre 26-30', 'entre 31-35',
                                'entre 36-40', 'entre 41-45', 'entre 46-50', 'entre 51-55', 'entre 56-60', 'entre 61-66',
                                'entre 66-70', 'maior que 70']
          parametros = {'Sexo':leg_Sexo, 
                        'Cor/Raça':leg_Cor,
                        'Faixa Etária':leg_Faixa_etária,
                        'Estado Civil':leg_EstadoCivil,
                        'Nacionalidade':leg_Nacionalidade,
                        'Tipo de Escola':leg_tp_escola}
            
          hist_x = plt.figure() 
          sns.histplot(x=df_x.index, weights=df_x[competencia], legend=True, binwidth=1, hue=df_x.index,
                       palette='gist_ncar')  # fazendo um histograma, no qual, no eixo x são os estados, e no eixo y a média de notas
          plt.legend(title='Legenda', labels=parametros[param], loc='center left', bbox_to_anchor=(1, 0.5))
          return hist_x
        
        competencia = st.selectbox('Qual competência você deseja visualizar?',
                                   ['Ciências da Natureza', 'Ciências Humanas', 'Linguagens e Códigos', 'Matemática', 'Redação'])
        param = st.selectbox("Qual atributo você quer ver?",
                             ['Sexo', 'Cor/Raça', 'Faixa Etária', 'Estado Civil', 'Nacionalidade', 'Tipo de Escola'])
        st.pyplot(distrib(df, competencia, param))
        
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
