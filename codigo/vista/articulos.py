import os
from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt6.uic import loadUi
import csv

CSV_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "registroArticulos.csv")

class Articulos(QWidget):
    def __init__(self):
        super().__init__()

        base_dir = os.path.abspath(os.path.dirname(__file__))
        ui_path = os.path.join(base_dir, "articulos.ui")

        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"No se encontró el archivo UI: {ui_path}")

        loadUi(ui_path, self)

        self.lista_articulos = []

        # Conectar botones y tabla
        self.btnAgregar.clicked.connect(self.agregar_articulo)
        self.btnActualizar.clicked.connect(self.actualizar_articulo)
        self.btnEliminar.clicked.connect(self.eliminar_articulo)
        self.tableArticulos.itemSelectionChanged.connect(self.cargar_datos_articulo_seleccionado)

        # Cargar datos guardados
        self.cargar_datos_csv()
        self.actualizar_tabla_articulos()

    def agregar_articulo(self):
        nombre = self.lineEditNombre.text().strip()
        if not nombre:
            QMessageBox.warning(self, "Error", "El nombre no puede estar vacío.")
            return

        precio_publico = self.spinPrecioPublico.value()
        precio_proveedor = self.spinPrecioProveedor.value()
        stock = self.spinStock.value()

        if precio_publico <= 0 or precio_proveedor <= 0:
            QMessageBox.warning(self, "Error", "El precio debe ser mayor a 0.")
            return

        articulo = {
            "id": str(len(self.lista_articulos) + 1),
            "nombre": nombre,
            "precio_publico": precio_publico,
            "precio_proveedor": precio_proveedor,
            "stock": stock
        }

        self.lista_articulos.append(articulo)
        self.guardar_datos_csv()
        self.actualizar_tabla_articulos()
        self.limpiar_formulario_articulos()

    def actualizar_articulo(self):
        selected = self.tableArticulos.currentRow()
        if selected < 0 or selected >= len(self.lista_articulos):
            QMessageBox.warning(self, "Error", "Seleccione un artículo para actualizar.")
            return

        nombre = self.lineEditNombre.text().strip()
        if not nombre:
            QMessageBox.warning(self, "Error", "El nombre no puede estar vacío.")
            return

        precio_publico = self.spinPrecioPublico.value()
        precio_proveedor = self.spinPrecioProveedor.value()
        stock = self.spinStock.value()

        self.lista_articulos[selected] = {
            "id": self.lista_articulos[selected]["id"],
            "nombre": nombre,
            "precio_publico": precio_publico,
            "precio_proveedor": precio_proveedor,
            "stock": stock
        }

        self.guardar_datos_csv()
        self.actualizar_tabla_articulos()
        self.limpiar_formulario_articulos()

    def eliminar_articulo(self):
        selected = self.tableArticulos.currentRow()
        if selected < 0 or selected >= len(self.lista_articulos):
            QMessageBox.warning(self, "Error", "Seleccione un artículo para eliminar.")
            return

        del self.lista_articulos[selected]
        self.guardar_datos_csv()
        self.actualizar_tabla_articulos()
        self.limpiar_formulario_articulos()

    def actualizar_tabla_articulos(self):
        self.tableArticulos.setRowCount(0)

        for articulo in self.lista_articulos:
            row = self.tableArticulos.rowCount()
            self.tableArticulos.insertRow(row)
            self.tableArticulos.setItem(row, 0, QTableWidgetItem(articulo["id"]))
            self.tableArticulos.setItem(row, 1, QTableWidgetItem(articulo["nombre"]))
            self.tableArticulos.setItem(row, 2, QTableWidgetItem(f"{articulo['precio_publico']:.2f}"))
            self.tableArticulos.setItem(row, 3, QTableWidgetItem(f"{articulo['precio_proveedor']:.2f}"))
            self.tableArticulos.setItem(row, 4, QTableWidgetItem(str(articulo["stock"])))

    def limpiar_formulario_articulos(self):
        self.lineEditNombre.clear()
        self.spinPrecioPublico.setValue(0)
        self.spinPrecioProveedor.setValue(0)
        self.spinStock.setValue(0)
        self.tableArticulos.clearSelection()

    def guardar_datos_csv(self):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nombre", "Precio Público", "Precio Proveedor", "Stock"])
            for articulo in self.lista_articulos:
                writer.writerow([
                    articulo["id"],
                    articulo["nombre"],
                    articulo["precio_publico"],
                    articulo["precio_proveedor"],
                    articulo["stock"]
                ])

    def cargar_datos_csv(self):
        if not os.path.exists(CSV_FILE):
            return

        with open(CSV_FILE, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # saltar encabezado
            self.lista_articulos = []
            for row in reader:
                try:
                    articulo = {
                        "id": row[0],
                        "nombre": row[1],
                        "precio_publico": float(row[2]),
                        "precio_proveedor": float(row[3]),
                        "stock": int(row[4])
                    }
                    self.lista_articulos.append(articulo)
                except (ValueError, IndexError):
                    pass

        self.actualizar_tabla_articulos()

    def cargar_datos_articulo_seleccionado(self):
        selected = self.tableArticulos.currentRow()
        if selected < 0 or selected >= len(self.lista_articulos):
            self.limpiar_formulario_articulos()
            return

        articulo = self.lista_articulos[selected]
        self.lineEditNombre.setText(articulo["nombre"])
        self.spinPrecioPublico.setValue(articulo["precio_publico"])
        self.spinPrecioProveedor.setValue(articulo["precio_proveedor"])
        self.spinStock.setValue(articulo["stock"])
