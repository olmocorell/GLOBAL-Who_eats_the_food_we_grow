import pandas as pd
import json

#reading data
df = pd.read_csv("input/FAO.csv",encoding='cp1252')

#rename year`s columns 
columnas = df.columns[10:]
nombres = []
for a in columnas:
    nombres.append((a,a[1:]))
nombres = dict(nombres)
df = df.rename(columns=nombres)

#drop duplicates
df = df.drop_duplicates()

#export json to MongoDB
df.to_json("data")