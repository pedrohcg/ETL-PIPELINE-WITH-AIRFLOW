
# Pipeline ETL Usando Airflow

## Descrição

Este projeto tem como objetivo desenvolver um pipeline ETL utilizando Airflow para obter dados sobre o clima de uma cidade espec[ifica a cada hora. Os dados são extraídos usando a WheatherAPI, depois são transformados com python e é feito verificação de qualidade dos dados. Por fim os dados são carregados em um banco de dados sqlite para que possamos usar sql para analisá-los e também são salvos em um arquivo csv.

## Tecnologias

Esse software usa as seguintes tecnologias:

 - [Docker](https://www.docker.com/)
 - [Airflow](https://airflow.apache.org/)
 - [WeatherAPI](https://www.weatherapi.com/)
 - [Python](https://www.python.org/)
 - [SQLite](https://www.sqlite.org/)
 - [Pandas](https://pandas.pydata.org/)

## Como Usar

Para executar este projeto você precisará do Docker instalado em seu computador, também precisará de uma conta WeatherAPI para poder gerar uma chave API e, em seguida, precisará colocar sua chave na solicitação get no script de etl. Então você precisará executar os seguintes comandos em seu terminal:

```bash
# Clonar o respositório
$ git clone https://github.com/pedrohcg/ETL-PIPELINE-WITH-AIRFLOW/tree/main

# Fazer a migração do banco de dados do airflow, criar conta do usuário e criar/fazer download das imagens
$ docker compose up airflow-init

# Inicia o container
$ docker compose up

# Conenctando ao Airflow
http://localhost:8080/home

# Usuário e senha serão ambos airflow
```

Com tudo isso feito você estará na página principal do airflow com o DAG desabilitado, agora você só precisa habilitar o DAG e ele funcionará a cada hora de 18/03/2024 (a data de início que coloquei neste DAG) até hoje . Você também pode executá-lo manualmente ou aguardar o agendador.
