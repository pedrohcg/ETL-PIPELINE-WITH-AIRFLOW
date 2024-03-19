#!/usr/bin/env python
# coding: utf-8

import os
import sqlite3
import requests
import datetime
import pandas as pd

def api_data_extract():
    now = datetime.datetime.now()
    
    api_data = requests.get("http://api.weatherapi.com/v1/current.json?key=c8cc17ac554d4ffb90c184403241803&q=Joao Pessoa&aqi=yes")
    
    # Converts data to JSON
    data = api_data.json()
    
    # Use JSON data to create a dict
    dict = {
        "temperature": [data["current"]["temp_c"]],
        "wind_speed": [data["current"]["wind_kph"]],
        "condition": [data["current"]["condition"]["text"]],
        "precipitation": [data["current"]["precip_mm"]],
        "humidity": [data["current"]["humidity"]],
        "feels_like_temp": [data["current"]["feelslike_c"]],
        "pressure": [data["current"]["pressure_mb"]],
        "visibility": [data["current"]["vis_km"]],
        "is_day": [data["current"]["is_day"]],
        "timestamp": [now]
    }
    
    return pd.DataFrame(dict)

def data_quality(data_df):
    if data_df.empty:
        print('No data present.')
        return False
    
    if data_df.isnull().values.any():
        print('Null values detected.')
        
def transform_data(data_df):
    # Converts column to boolean type
    data_df["is_day"] = data_df["is_day"].astype(bool)
    
    # Creates a new column ID column with the data of the columns timestamp and temperature
    data_df["ID"] = data_df["timestamp"].astype(str) + "-" + data_df["temperature"].astype(str)
    
    return data_df

def extract_transform():
    # Extract the data
    data_df = api_data_extract()
    
    # Data transformation
    data_df = transform_data(data_df)
    
    data_quality(data_df)
    
    return data_df

def etl_process():
    df = extract_transform()
    
    file_path = "/opt/airflow/dags/projeto2_dados.csv"
    
    # Verify if the output file already exists to decide if it will or not create with a header
    header = not os.path.isfile(file_path)
    
    # Save dataframe as csv using the append mode
    df.to_csv(file_path, mode='a', index=False, header=header)
    
    conn = sqlite3.connect('/opt/airflow/dags/database.db')
    
    # Creates the table on the database or append the data if it already exists
    df.to_sql('table', conn, if_exists='append', index=False)
    
    conn.close()