import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.uic import loadUi


class PaginaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        # Obtiene el directorio actual donde se encuentra main.py
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Construye la ruta relativa hacia la carpeta "vista" y el archivo .ui
        ui_path = os.path.join(base_dir, "vista", "paginaPrincipal.ui")
        # Carga la interfaz
        loadUi(ui_path, self)

        # Conecta los botones con sus respectivas funciones
        self.btnArticulos.clicked.connect(self.mostrar_articulos)
        self.btnClientes.clicked.connect(self.mostrar_clientes)
        self.btnVentas.clicked.connect(self.mostrar_ventas)

    def mostrar_articulos(self):
        print("Mostrando gestión de artículos")

    def mostrar_clientes(self):
        print("Mostrando gestión de clientes")

    def mostrar_ventas(self):
        print("Mostrando gestión de ventas")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PaginaPrincipal()
    ventana.show()
    sys.exit(app.exec())
