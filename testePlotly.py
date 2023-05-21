# importação de bibliotecas
import pandas as pd
from functools import reduce
import plotly.graph_objs as go
import plotly.express as px
import zipfile
import streamlit as st
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

    #df.drop_duplicates(inplace=True)
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
    'AC': 'Norte',
    'AL': 'Nordeste',
    'AP': 'Norte',
    'AM': 'Norte',
    'BA': 'Nordeste',
    'CE': 'Nordeste',
    'DF': 'Centro-Oeste',
    'ES': 'Sudeste',
    'GO': 'Centro-Oeste',
    'MA': 'Nordeste',
    'MT': 'Centro-Oeste',
    'MS': 'Centro-Oeste',
    'MG': 'Sudeste',
    'PA': 'Norte',
    'PB': 'Nordeste',
    'PR': 'Sul',
    'PE': 'Nordeste',
    'PI': 'Nordeste',
    'RJ': 'Sudeste',
    'RN': 'Nordeste',
    'RS': 'Sul',
    'RO': 'Norte',
    'RR': 'Norte',
    'SC': 'Sul',
    'SP': 'Sudeste',
    'SE': 'Nordeste',
    'TO': 'Norte'
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

st.title("Testando o plotly")
escolha = st.selectbox("Qual competência você deseja ver?", ["red", "mat", "ch", "lc", "cn"])
if escolha == 'red':
    st.plotly_chart(fig_red)
elif escolha == 'mat':
    st.plotly_chart(fig_mat)
elif escolha == 'ch':
    st.plotly_chart(fig_ch)
elif escolha == 'lc':
    st.plotly_chart(fig_lc)
elif escolha == 'cn':
    st.plotly_chart(fig_cn)