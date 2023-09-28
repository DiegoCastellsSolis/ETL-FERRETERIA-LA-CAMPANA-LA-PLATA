import os
import pandas as pd
import re

def extract(directorio_raw,archivo):
    path = directorio_raw+'/'+archivo
    df = pd.read_excel(path,header=9, usecols="B:F") 
    return df

def transform(df):
   
    dfx = df
    dfx = dfx.rename(columns={
        'Unnamed: 1': 'codigo',
        'Unnamed: 2': 'descripcion',
        'Unnamed: 3': 'empaque',
        'Unnamed: 4': 'raw',
        'Unnamed: 5': 'precio'
    }) 
    dfx = dfx.dropna(subset=['codigo'])  

    # Restablecer los índices del DataFrame
    dfx.reset_index(drop=True, inplace=True) 
    list_articles = [item for item in df[df.columns[0]].tolist() if item != "Código" and not pd.isna(item) and not re.match(r'\d+\.\d+', str(item)) and "Plástico" not in item and "Poliestireno" not in item ]
    
    # Renombrar las columnas
    df = df.rename(columns={
        'Unnamed: 1': 'codigo',
        'Unnamed: 2': 'descripcion',
        'Unnamed: 3': 'empaque',
        'Unnamed: 4': 'raw',
        'Unnamed: 5': 'precio'
    })
    #ELIMINO LA COLUMNA 3 QUE AL EXISTIR UN COLUMNA DIVISORIA ENTRE DESCRIPCION Y PRECIO POSEE VALORES BASURA
    df = df.drop('raw', axis=1)
    df = df.dropna(subset=['codigo'])

    # Crear la nueva columna 'tipo_product'
    df['producto'] = None
    current_tipo_product = None

    # Definir las palabras a excluir
    palabras_excluir = ["Plástico", "Poliestireno"]

    # Filtrar la columna 'codigo' para excluir las palabras
    for palabra in palabras_excluir:
        df = df[~df['codigo'].str.contains(palabra, case=False)]

    # Restablecer el índice del DataFrame
    df.reset_index(drop=True, inplace=True)

    for index, row in df.iterrows():
        codigo = row['codigo']
        if codigo in list_articles:
            current_tipo_product = codigo
        df.at[index, 'producto'] = current_tipo_product
        
    df = df.dropna(subset=['precio'])

    df = df.dropna(subset=[df.columns[0]])
    df = df.dropna(subset=[df.columns[3]])

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
    archivo = "RAO.xlsx"
    ETL(directorio_raw,directorio_out,archivo)