import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.uic import loadUi
from .articulos import Articulos  # Asegúrate que el paquete esté bien configurado
from .cliente import Cliente      # Importar la clase Cliente correctamente

class PaginaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        base_dir = os.path.abspath(os.path.dirname(__file__))
        ui_path = os.path.join(base_dir, "paginaPrincipal.ui")

        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"No se encontró el archivo UI: {ui_path}")

        loadUi(ui_path, self)

        self.articulos_window = None
        self.clientes_window = None

        self.btnArticulos.clicked.connect(self.abrir_articulos)
        self.btnClientes.clicked.connect(self.abrir_clientes)

    def abrir_articulos(self):
        if self.articulos_window is None:
            self.articulos_window = Articulos()
        self.articulos_window.show()
        self.articulos_window.raise_()

    def abrir_clientes(self):
        if not hasattr(self, 'clientes_window') or self.clientes_window is None:
            from .cliente import Cliente  # Importa aquí para evitar ciclos
            self.clientes_window = Cliente()
        self.clientes_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = PaginaPrincipal()
    main_window.show()
    sys.exit(app.exec())
