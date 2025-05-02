import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
import os
from dotenv import load_dotenv

load_dotenv()

# Conexão com banco de dados
def get_db_connection():
    return create_engine(os.getenv("DATABASE_URL"))

# Criar tabela
def create_table(engine, df):
    df.to_sql('temperature_logs', engine, if_exists='replace', index=False)

# Interface Streamlit
st.title("Upload de Arquivo CSV")
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Estrutura do Dataset:")
    st.write(df.head())

    engine = get_db_connection()
    create_table(engine, df)
    st.success("Dados enviados para o banco de dados.")

# Usando as Views SQL para as consultas:
def load_data_from_view(view_name):
    engine = get_db_connection()
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# Visualização
st.title("Visualização dos Dados")

# Exemplo de gráfico para a view 'avg_temp_por_dispositivo'
df_avg_temp = load_data_from_view('avg_temp_por_dispositivo')
fig1 = px.bar(df_avg_temp, x='device_id', y='avg_temp', title='Média de Temperatura por Dispositivo')
st.plotly_chart(fig1)

# Exemplo de gráfico para a view 'leituras_por_hora'
df_leituras_hora = load_data_from_view('leituras_por_hora')
fig2 = px.line(df_leituras_hora, x='hora', y='contagem', title='Leituras por Hora')
st.plotly_chart(fig2)

# Exemplo de gráfico para a view 'temp_max_min_por_dia'
df_temp_max_min = load_data_from_view('temp_max_min_por_dia')
fig3 = px.line(df_temp_max_min, x='data', y=['temp_max', 'temp_min'], title='Temperaturas Máximas e Mínimas por Dia')
st.plotly_chart(fig3)
