import sys
import os
from PyQt6.QtWidgets import QApplication
from vista.pagina_principal import PaginaPrincipal
from modelo.file_manager import FileManager

def inicializar_archivo_si_no_existe(ruta_archivo, encabezados):
    if not os.path.exists(ruta_archivo):
        print(f"Archivo '{ruta_archivo}' no existe. Creando con encabezados.")
        FileManager.escribir_csv(ruta_archivo, [encabezados])
    else:
        print(f"Archivo '{ruta_archivo}' ya existe. No se sobrescribe.")

def main():


    # Encabezados por archivo
    encabezados_articulos = ["id", "nombre", "precio", "stock"]
    encabezados_clientes = ["id", "nombre", "telefono"]
    encabezados_ventas = ["id", "cliente_id", "fecha", "total"]

    # Verificar y crear archivos si no existen

    # Iniciar la aplicación
    app = QApplication(sys.argv)
    ventana = PaginaPrincipal()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
