import csv

class FileManager:
    def guardarCsv(self, nombreArchivo, datos, campos):
        """"Guarda una lista de diccionarios en un archivo csv"""
        with open(nombreArchivo, 'w',encoding='utf-8' ,newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerow(datos)

    def leerCsv(self, nombreArchivo):
        """Lee una archivo csv y devuelve una lista de diccionarios"""
        try:
            with open(nombreArchivo,'r', encoding='utf-8') as archivo:
                lector= csv.DictReader(archivo)
                return [fila for fila in lector]
        except FileNotFoundError:
            return []