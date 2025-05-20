import os
from PyQt6.QtWidgets import QWidget
from PyQt6.uic import loadUi

# Se importan las clases para cada ventana.
from .articulos import Articulos
from .cliente import Cliente
from .Ventas import Ventas

class PaginaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        base_dir = os.path.abspath(os.path.dirname(__file__))
        ui_path = os.path.join(base_dir, "paginaPrincipal.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"No se encontró el UI: {ui_path}")
        loadUi(ui_path, self)

        # Inicializamos las ventanas en None para instanciarlas cuando se necesiten.
        self.articulos_window = None
        self.clientes_window = None
        self.ventas_window = None

        # Conectamos cada botón a su métod0:
        self.btnArticulos.clicked.connect(self.abrir_articulos)
        self.btnClientes.clicked.connect(self.abrir_clientes)
        self.btnVentas.clicked.connect(self.abrir_ventas)

    def abrir_articulos(self):
        if self.articulos_window is None:
            self.articulos_window = Articulos()
        self.articulos_window.show()
        self.articulos_window.raise_()

    def abrir_clientes(self):
        if self.clientes_window is None:
            self.clientes_window = Cliente()
        self.clientes_window.show()
        self.clientes_window.raise_()

    def abrir_ventas(self):
        # Función para el botón "Ventas"
        print("Abriendo ventana de Ventas")  # Mensaje para confirmar en consola la ejecución
        if self.ventas_window is None:
            self.ventas_window = Ventas()
        self.ventas_window.show()
        self.ventas_window.raise_()
