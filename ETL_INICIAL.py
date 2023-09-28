import os
import pandas as pd
import re
import etl_FEMEBA
import etl_RAO
import etl_SANOR
import etl_IDEAL
import warnings



# Crear una función para procesar cada archivo
def procesar_archivo_ideal(directorio_raw,directorio_out,archivo):
    # Lógica para procesar el archivo IDEAL.xlsx
    etl_IDEAL.ETL(directorio_raw,directorio_out,archivo)
    print(f'El archivo {archivo} se ha procesado')
    pass

def procesar_archivo_mafeba(directorio_raw,directorio_out,archivo):
    # Lógica para procesar el archivo MAFEBA.xlsx
    etl_FEMEBA.ETL(directorio_raw,directorio_out,archivo)
    print(f'El archivo {archivo} se ha procesado')
    pass

def procesar_archivo_rao(directorio_raw,directorio_out,archivo):
    # Lógica para procesar el archivo RAO.xlsx
    etl_RAO.ETL(directorio_raw,directorio_out,archivo)
    print(f'El archivo {archivo} se ha procesado')
    pass

def procesar_archivo_sanor(directorio_raw,directorio_out,archivo):
    # Lógica para procesar el archivo SANOR.xlsx
    try:
        etl_SANOR.ETL(directorio_raw,directorio_out,archivo)
        print(f'El archivo {archivo} se ha procesado')
    except:
        print('error')
    pass


def main():
    directorio_raw = './data/raw'  # Reemplaza esto con la ruta de tu directorio
    directorio_out = './data/out'
    # Verifica si el directorio existe 
    if os.path.exists(directorio_raw) and os.path.isdir(directorio_raw): 
        archivos = os.listdir(directorio_raw)
        if archivos:
            #print("Archivos en el directorio:") 
            print("Comenzara a procesarse los archivos") 
            for archivo in archivos: 
                #print(archivo) 
                path = directorio_raw+'/'+archivo
                
                if archivo == "IDEAL.xlsx":
                    procesar_archivo_ideal(directorio_raw,directorio_out,archivo)
                elif archivo == "MAFEBA.xlsx":
                    procesar_archivo_mafeba(directorio_raw,directorio_out,archivo)
                elif archivo == "RAO.xlsx":
                    procesar_archivo_rao(directorio_raw,directorio_out,archivo)
                elif archivo == "SANOR.xlsx":
                    procesar_archivo_sanor(directorio_raw,directorio_out,archivo)
                else:
                    print(f"Archivo no reconocido: {archivo}")
        else:
            print("El directorio está vacío.") 
    else: 
        print("El directorio no existe o no es válido.") 

if __name__ == "__main__":

    # Desactivar una advertencia específica por su contenido
    warnings.filterwarnings("ignore", category=UserWarning, message="Unknown extension is not supported and will be removed")
    warnings.filterwarnings("ignore", category=UserWarning, message="Conditional Formatting extension is not supported and will be removed")

    main()

    warnings.resetwarnings()