####Projeto BigData E-Fecaf
Este projeto envolve a criação de uma aplicação em Streamlit que realiza o upload de um arquivo CSV com dados de temperatura, os armazena em um banco de dados PostgreSQL e visualiza esses dados em gráficos interativos.

#Passos para Execução
###Passo 1: Configuração do Repositório no GitHub
Criar Repositório no GitHub:
Acesse o GitHub e crie um novo repositório com o nome nome-sobrenome-bigdatafecaf.
Inicialize o repositório com um arquivo README.md.

Conectar o GitHub ao Replit:
Acesse o Replit e crie uma conta ou faça login.
Conecte o Replit ao seu GitHub para facilitar a sincronização do projeto.

###Passo 2: Configuração do Ambiente no Replit
Baixar e Fazer Upload do Dataset:
Baixe o dataset do link fornecido.
Faça upload do dataset para o Replit, garantindo que ele esteja no mesmo diretório do seu código.

#Instalar Dependências:
No shell do Replit, execute o seguinte comando para instalar as dependências necessárias:

poetry add streamlit pandas sqlalchemy psycopg2-binary plotly python-dotenv
#Criar o Arquivo .env:
No Replit, crie um arquivo chamado .env e adicione sua string de conexão do PostgreSQL:

DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco

###Passo 3: Desenvolver o Script em main.py
Criar o Arquivo main.py:
No Replit, crie um arquivo chamado main.py e adicione o seguinte código:

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Função para criar conexão com o banco de dados
def get_db_connection():
    return create_engine(os.getenv("DATABASE_URL"))

# Função para criar tabela no PostgreSQL
def create_table(engine, df):
    df.to_sql('temperature_logs', engine, if_exists='replace', index=False)

# Upload do arquivo CSV
st.title("Upload de Arquivo CSV")
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Leitura do arquivo CSV
    df = pd.read_csv(uploaded_file)
    st.write("Estrutura do Dataset:")
    st.write(df.head())

    # Conectar ao banco de dados
    engine = get_db_connection()

    # Criar tabela no PostgreSQL
    create_table(engine, df)
    st.success("Dados enviados para o banco de dados.")

    # Ler dados do banco de dados
    query = "SELECT * FROM temperature_logs"
    data = pd.read_sql(query, engine)

    # Visualização dos dados com Plotly
    st.title("Visualização dos Dados")
    fig = px.line(data, x='noted_date', y='temp', title='Série Temporal de Temperaturas')
    st.plotly_chart(fig)
###Passo 4: Executar o Streamlit
No Replit, execute o comando para iniciar o Streamlit:

streamlit run main.py
A interface do Streamlit abrirá em uma nova aba. Faça o upload do arquivo CSV e visualize o gráfico gerado.

###Passo 5: Fazer Git Push
Adicionar e Comitar Alterações:
No shell do Replit, execute os seguintes comandos para adicionar e comitar as mudanças:

git add .
git commit -m "Adicionar código do Streamlit e configuração do banco de dados"
Fazer Push para o GitHub:
Execute o comando para empurrar as alterações para o GitHub:

git push origin main

###Passo 6: Deploy no Render.com
Criar Conta e Novo Serviço no Render:
Acesse Render.com e crie uma conta ou faça login.
Crie um novo serviço web e conecte-o ao repositório GitHub do projeto.

##Configurar o Serviço:
Configure o serviço para usar o comando de inicialização do Streamlit:


#Editar
#streamlit run main.py
#Deploy:
#Finalize a configuração e inicie o deploy. O Render.com irá construir e implantar sua aplicação.

##Considerações Finais
Banco de Dados:
Certifique-se de que o banco de dados PostgreSQL está acessível a partir do ambiente onde o Streamlit está sendo executado.

##Segurança:
Nunca exponha credenciais sensíveis diretamente no código. Utilize variáveis de ambiente para gerenciá-las de forma segura.

##Debugging:
Se encontrar erros, verifique os logs no Replit e no Render.com para diagnósticos.







