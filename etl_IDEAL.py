import os
import pandas as pd
import re

def extract(directorio_raw,archivo):
    path = directorio_raw+'/'+archivo
    df = pd.read_excel(path,header=0, usecols="A:C") 
    return df

def transform(df):
    
    df = df.rename(columns={
    'Unnamed: 0': 'codigo',
    'Unnamed: 1': 'descripcion',
    'Unnamed: 2': 'precio' 
    }) 
    #print(df.head(15))
    df = df.dropna(subset=['codigo'])  
    df = df.dropna(subset=['precio'])  
    # Restablecer los índices del DataFrame
    df.reset_index(drop=True, inplace=True) 
    #print("-----")
    #print(df.head(15))
    return df


def load(df,directorio_out,archivo):
    directorio_out = './data/out/'+archivo
    df.to_excel(directorio_out)


def ETL(directorio_raw,directorio_out,archivo):
    df = extract(directorio_raw,archivo)
    df = transform(df)
    load(df,directorio_out,archivo)

if __name__ == "__main__":
    directorio_raw = "./data/raw"
    directorio_out = "./data/out"
    archivo = "IDEAL.xlsx"
    ETL(directorio_raw,directorio_out,archivo)