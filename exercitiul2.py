import pandas as pd
import numpy as np
import sqlite3
import csv

# Create your connection.

with sqlite3.connect('users\db.sqlite3') as conn:
    df=pd.read_sql('SELECT * FROM persoane_user',conn)
    print(df)
    df['full_name']=pd.Series(df['first_name']+df['last_name'])
    print(df)
    df.to_csv('afisare.csv')
    #mean si std pt no_of_login
    print("Media pe nr_of_login", df['number_of_login'].mean())
    print("Standard deviation nr_of_login", df['number_of_login'].std())

