import os.path
from datetime import datetime
from operator import index
import pandas as pd
import sqlite3
from bs4 import BeautifulSoup
import numpy as np
from datetime import datetime
import requests

url='https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attributes_Extraction_only=['Name','MC_USD_Billion']
table_attributes=['Name','MC_USD_Billion','MC_EUR_Billion','MC_INR_Billion']
output_csv = 'Largest_banks_data.csv'
db_name = 'Banks.db'
table_name = 'Largest_banks'
log_file='code_log.txt'

def log_progress(message):
    timestamp_format="%Y-%h-%d-%H:%M:%S"
    now=datetime.now()
    timestamp=now.strftime(timestamp_format)
    with open(log_file ,'a') as f:
        f.write(f'{timestamp}: {message} \n')

def extract(url,table_attributes):
    log_progress(' start to extract data')
    df=pd.DataFrame(columns=table_attributes)
    requested_data=requests.get(url).text
    data =BeautifulSoup(requested_data,'html.parser')
    all_tables=data.find_all('tbody')
    rows=all_tables[0].find_all('tr')
    for row in rows:
        col=row.find_all('td')
        if len(col)!=0:
            if col[1].find('a') is not None :
                data_dict={
                    'Name': col[1].text,
                    'MC_USD_Billion': col[2].text
                }
            df1=pd.DataFrame(data_dict,index=[0])
            df=pd.concat([df,df1],ignore_index=True)
    log_progress('data is extract Done')
    return df


def transform(df):
    clean_data_name=df['Name'].tolist()
    clean_data_MC_USD_Billion =df['MC_USD_Billion'].tolist()
    clean_data_MC_USD_Billion=[x.replace('\n','')  for x in clean_data_MC_USD_Billion ]
    clean_list=[x.replace('\n','') for x in clean_data_name ]
    df['Name']=clean_list
    df['MC_USD_Billion']=clean_data_MC_USD_Billion
    # make it float
    df['MC_USD_Billion']=df['MC_USD_Billion'].astype(float)
    # convert rate.csv to dict
    dataframe=pd.read_csv('exchange_rate.csv')
    exchange_rate = dataframe.set_index('Currency').to_dict()['Rate']
    log_progress('Exchange rates loaded')
    # add new columns
    df['MC_GBP_Billion']=[round(x* exchange_rate['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion']=[round(x* exchange_rate['EUR'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [round(x * exchange_rate['INR'],2) for x in df['MC_USD_Billion']]
    log_progress('Data transformation completed')
    return df

transformed_data=transform(extract(url,table_attributes_Extraction_only))

def load_to_csv(transformed_data,csv_path=output_csv):
    log_progress("make file as csv file")
    transformed_data.to_csv(csv_path)
load_to_csv(transformed_data)

connection=sqlite3.connect(db_name)
def load_to_db(transformed_data,connection,table_name):
    log_progress('transform data to db file')
    transformed_data.to_sql(table_name,connection,if_exists='replace',index=False)

def run_query(sql_statement,sql_connection):
    print(sql_statement)
    log_progress('you make new query in data base  ')
    sql_output=pd.read_sql_query(sql_statement,sql_connection)
    print(sql_output)
#load data in data base
load_to_db(transformed_data,connection,table_name)

#query to print the contents of the entire table
query='SELECT * FROM  Largest_banks'
run_query(query,connection)

# query to print average market capitalization of all the banks in Billion USD.
query2='SELECT AVG(MC_GBP_Billion) FROM Largest_banks'
run_query(query2,connection)

# query Print only the names of the top 5 banks
query3='SELECT Name from Largest_banks LIMIT 5'
run_query(query3,connection)
