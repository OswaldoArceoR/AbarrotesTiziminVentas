import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtUiTools import QUiLoader

class PaginaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("paginaPrincipal.ui", None)

        # Conectar botones a funciones
        self.ui.btnArticulos.clicked.connect(self.mostrar_articulos)
        self.ui.btnClientes.clicked.connect(self.mostrar_clientes)
        self.ui.btnVentas.clicked.connect(self.mostrar_ventas)

    def mostrar_articulos(self):
        print("Mostrando gestión de artículos")

    def mostrar_clientes(self):
        print("Mostrando gestión de clientes")

    def mostrar_ventas(self):
        print("Mostrando gestión de ventas")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PaginaPrincipal().ui
    ventana.show()
    sys.exit(app.exec())
