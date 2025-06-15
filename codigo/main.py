import sys
import os
import csv
from PyQt6.QtWidgets import QApplication
from vista.pagina_principal import PaginaPrincipal


def inicializar_archivo_si_no_existe(ruta_archivo, encabezados):
    if not os.path.exists(ruta_archivo):
        print(f"Archivo '{ruta_archivo}' no existe. Creando con encabezados.")
        with open(ruta_archivo, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(encabezados)
    else:
        print(f"Archivo '{ruta_archivo}' ya existe. No se sobrescribe.")

def main():
    # Encabezados para cada CSV
    encabezados_articulos = ["id", "nombre", "precio", "stock"]
    encabezados_clientes  = ["id", "nombre", "telefono"]
    encabezados_ventas    = ["id", "cliente_id", "fecha", "total"]

    # Inicializar archivos CSV si no existen
    #inicializar_archivo_si_no_existe("registroArticulos.csv", encabezados_articulos)
    #inicializar_archivo_si_no_existe("registroClientes.csv", encabezados_clientes)
    #inicializar_archivo_si_no_existe("registroVentas.csv", encabezados_ventas)

    app = QApplication(sys.argv)
    ventana = PaginaPrincipal()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
