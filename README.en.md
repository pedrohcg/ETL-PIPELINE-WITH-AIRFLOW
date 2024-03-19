
# ETL Pipeline Using Airflow

## Description

This project aims to develop a ETL pipeline using Airflow so it can get data about the weather of a chosen city every hour. The data is extracted from the WheatherAPI, then they are transformed with python and have they quality checked. At last the data is loaded in a sqlite database so we can use sql to analysis it and saved in a csv file. 

## Technologies

This software the following technologies:

 - [Docker](https://www.docker.com/)
 - [Airflow](https://airflow.apache.org/)
 - [WeatherAPI](https://www.weatherapi.com/)
 - [Python](https://www.python.org/)
 - [SQLite](https://www.sqlite.org/)
 - [Pandas](https://pandas.pydata.org/)

## How To use

To run this project you will need Docker installed on your computer, you'll also need an WeatherAPI account so you can generate a API Key, then you'll need to put your key on the get request on the etl script. Then you will need to execute the following commands on your terminal:

```bash
# Clone this repository
$ git clone https://github.com/pedrohcg/ETL-PIPELINE-WITH-AIRFLOW/tree/main

# Run database migrations and create the first user accounts
$ docker compose up airflow-init

# Start the container
$ docker compose up

# Connect to Airflow
http://localhost:8080/home

# The user and password will both be airflow
```

With all that done you'll be on airflow main page with the DAG disable, now you only need to enable the DAG and it will run for every hour from 2024-03-18(the start date i put on this DAG) to today. You can also execute it manually or wait for the scheduler.

