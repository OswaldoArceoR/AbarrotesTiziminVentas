import os
from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PyQt6.uic import loadUi

class Articulos(QWidget):
    def __init__(self):
        super().__init__()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(base_dir, "..", "vista", "articulos.ui")
        print("Cargando UI de Articulos desde:", ui_path)
        loadUi(ui_path, self)
        self.setWindowTitle("Gestión de Artículos")

        self.lista_articulos = []

        self.btnAgregar.clicked.connect(self.agregar_articulo)
        self.btnActualizar.clicked.connect(self.actualizar_articulo)
        self.btnEliminar.clicked.connect(self.eliminar_articulo)
        self.tableArticulos.itemSelectionChanged.connect(self.cargar_datos)

        self.actualizar_tabla()

    def agregar_articulo(self):
        nombre = self.lineEditNombre.text().strip()
        codigo = self.lineEditCodigo.text().strip()
        if not nombre or not codigo:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return
        precio_publico = self.spinPrecioPublico.value()
        stock = self.spinStock.value()

        articulo = {"codigo": codigo, "nombre": nombre, "precio_publico": precio_publico, "stock": stock}
        self.lista_articulos.append(articulo)
        self.actualizar_tabla()
        self.limpiar_formulario()

    def actualizar_articulo(self):
        selected = self.tableArticulos.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Error", "Seleccione un artículo para actualizar.")
            return
        nombre = self.lineEditNombre.text().strip()
        codigo = self.lineEditCodigo.text().strip()
        precio_publico = self.spinPrecioPublico.value()
        stock = self.spinStock.value()

        self.lista_articulos[selected] = {"codigo": codigo, "nombre": nombre, "precio_publico": precio_publico, "stock": stock}
        self.actualizar_tabla()
        self.limpiar_formulario()

    def eliminar_articulo(self):
        selected = self.tableArticulos.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Error", "Seleccione un artículo para eliminar.")
            return
        del self.lista_articulos[selected]
        self.actualizar_tabla()
        self.limpiar_formulario()

    def actualizar_tabla(self):
        self.tableArticulos.setRowCount(0)
        for articulo in self.lista_articulos:
            row = self.tableArticulos.rowCount()
            self.tableArticulos.insertRow(row)
            self.tableArticulos.setItem(row, 0, QTableWidgetItem(articulo["codigo"]))
            self.tableArticulos.setItem(row, 1, QTableWidgetItem(articulo["nombre"]))
            self.tableArticulos.setItem(row, 2, QTableWidgetItem(f"{articulo['precio_publico']:.2f}"))
            self.tableArticulos.setItem(row, 3, QTableWidgetItem(str(articulo["stock"])))

    def limpiar_formulario(self):
        self.lineEditNombre.clear()
        self.lineEditCodigo.clear()
        self.spinPrecioPublico