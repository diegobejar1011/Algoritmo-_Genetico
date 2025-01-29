import csv

def get_dataset_csv(archivo_csv):
    datos = []
    with open(archivo_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo, delimiter=';')
        for fila in lector:
            if fila:  
                diccionario = {f'X{i+1}': int(valor.strip()) for i, valor in enumerate(fila[:-1])}
                diccionario['Y'] = int(fila[-1].strip())
                datos.append(diccionario)
    return datos
