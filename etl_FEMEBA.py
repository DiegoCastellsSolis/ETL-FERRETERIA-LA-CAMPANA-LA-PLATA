import os
import pandas as pd
import re

def extract(directorio_raw,archivo):
    path = directorio_raw+'/'+archivo
    df = pd.read_excel(path,header=9)
    return df

def transform(df):
    df.rename(columns={'Unnamed: 1': 'codigo', 'Unnamed: 3': 'descripcion', 'Unnamed: 26': 'precio_unitario', 'Unnamed: 29': 'variacion'}, inplace=True)
    columnas_a_eliminar_1 = ['Unnamed: ' + str(i) for i in range(4, 26)] 
    columnas_a_eliminar_2 = ['Unnamed: ' + str(i) for i in range(27, 29)] 
    columnas_a_eliminar_3 = ['Unnamed: 0','Unnamed: 2'] 

    # Combina las tres listas en una sola
    columnas_a_eliminar = columnas_a_eliminar_1 + columnas_a_eliminar_2 + columnas_a_eliminar_3
    df.drop(columns=columnas_a_eliminar, inplace=True)
    df = df.dropna(subset=['precio_unitario'])

    # Crear una expresión regular para identificar las filas donde 'codigo' contiene texto
    patron = r'.*[a-zA-Z].*'

    # Filtrar las filas que cumplen con el patrón y eliminarlas
    df = df[~df['codigo'].str.contains(patron, na=False)]
    df = df[~df['precio_unitario'].str.contains(patron, na=False)]
    df['precio'] = df['precio_unitario']*(1+df['variacion'])

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
    archivo = "FEMEBA.xlsx"
    ETL(directorio_raw,directorio_out,archivo)