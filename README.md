Pipeline_IOT


Descrição do Projeto


Este projeto implementa um pipeline de dados para processar e armazenar leituras de temperatura de dispositivos IoT em um banco de dados PostgreSQL, utilizando Docker. A solução também inclui um dashboard interativo criado com Streamlit, que visualiza insights como a média de temperatura por dispositivo, leituras por hora e temperaturas máximas e mínimas por dia.

O fluxo de trabalho do projeto envolve:

Processar um arquivo CSV (IOT-temp.csv) com leituras de temperatura de dispositivos IoT.\

Armazenar os dados em um banco de dados PostgreSQL usando SQLAlchemy.

Criar visualizações dinâmicas dos dados via Streamlit.

Como Configurar o Ambiente

Pré-requisitos:    
  
Python 3.8+

Docker

Conta no GitHub e Kaggle
    
Passos para configurar o ambiente:

Clone o repositório:

git clone https://github.com/DOliveiira/pipeline-IOT

cd repositorio

Crie e ative um ambiente virtual Python:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows

Instale as dependências necessárias:

pip install pandas psycopg2-binary sqlalchemy streamlit plotly

Configure o banco de dados PostgreSQL com Docker:

Inicie o contêiner PostgreSQL:

docker run --name postgres-iot -e POSTGRES_PASSWORD=sua_senha -p 5432:5432 -d postgres
Carregue os dados CSV para o banco de dados:

Execute o script de processamento:

python pipeline.py
Execute o dashboard Streamlit:

streamlit run dashboard.py
