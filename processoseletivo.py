import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout= 'wide')

st.title('Acompanhamento de Processos Seletivos')
st.write('Controle dos processos seletivos realizados pela Presidência da República')


df = pd.read_csv('controle_editais6.csv', sep=';')
#df['Ano de recebimento da demanda'] = pd.to_datetime(df['Ano de recebimento da demanda'])
#df = df.sort_values('Ano de recebimento da demanda')


df['Year'] = df['Ano de recebimento da demanda']
year = st.sidebar.selectbox('Ano', df['Year'].unique())

df_filtered = df[df['Year'] == year]
df_filtered

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x='Ano de recebimento da demanda', color= 'Casa Demandante', y='Quantidade de vagas', title= 'Número de vagas por período')
col1.plotly_chart(fig_date)
