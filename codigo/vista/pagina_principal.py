import sys
import os
import csv
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PyQt6.uic import loadUi

CSV_FILE = os.path.join(os.path.dirname(__file__), "registroArticulos.csv")

class PaginaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        base_dir = os.path.abspath(os.path.dirname(__file__))
        ui_path = os.path.join(base_dir, "paginaPrincipal.ui")  # ✅ Ruta corregida

        print("Intentando cargar:", ui_path)

        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"No se encontró el archivo: {ui_path}")

        loadUi(ui_path, self)
        self.btnArticulos.clicked.connect(self.abrir_articulos)

    def abrir_articulos(self):
        base_dir = os.path.abspath(os.path.dirname(__file__))
        ui_path = os.path.join(base_dir, "articulos.ui")  # ✅ Ruta corregida

        print("Intentando cargar ventana de Artículos desde:", ui_path)

        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"No se encontró el archivo: {ui_path}")

        self.articulos_window = QWidget()
        loadUi(ui_path, self.articulos_window)

        self.lista_articulos = []

        self.cargar_datos_csv()

        self.articulos_window.btnAgregar.clicked.connect(self.agregar_articulo)
        self.articulos_window.btnActualizar.clicked.connect(self.actualizar_articulo)
        self.articulos_window.btnEliminar.clicked.connect(self.eliminar_articulo)

        self.articulos_window.show()

    def agregar_articulo(self):
        nombre = self.articulos_window.lineEditNombre.text().strip()
        if not nombre:
            QMessageBox.warning(self, "Error", "El nombre no puede estar vacío.")
            return

        precio_publico = self.articulos_window.spinPrecioPublico.value()
        precio_proveedor = self.articulos_window.spinPrecioProveedor.value()
        stock = self.articulos_window.spinStock.value()

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
        selected = self.articulos_window.tableArticulos.currentRow()
        if selected < 0 or selected >= len(self.lista_articulos):
            QMessageBox.warning(self, "Error", "Seleccione un artículo para actualizar.")
            return

        nombre = self.articulos_window.lineEditNombre.text().strip()
        precio_publico = self.articulos_window.spinPrecioPublico.value()
        precio_proveedor = self.articulos_window.spinPrecioProveedor.value()
        stock = self.articulos_window.spinStock.value()

        self.lista_articulos[selected]["nombre"] = nombre
        self.lista_articulos[selected]["precio_publico"] = precio_publico
        self.lista_articulos[selected]["precio_proveedor"] = precio_proveedor
        self.lista_articulos[selected]["stock"] = stock

        self.guardar_datos_csv()
        self.actualizar_tabla_articulos()
        self.limpiar_formulario_articulos()

    def eliminar_articulo(self):
        selected = self.articulos_window.tableArticulos.currentRow()
        if selected < 0 or selected >= len(self.lista_articulos):
            QMessageBox.warning(self, "Error", "Seleccione un artículo para eliminar.")
            return

        del self.lista_articulos[selected]
        self.guardar_datos_csv()
        self.actualizar_tabla_articulos()
        self.limpiar_formulario_articulos()

    def actualizar_tabla_articulos(self):
        table = self.articulos_window.tableArticulos
        table.setRowCount(0)

        for articulo in self.lista_articulos:
            row = table.rowCount()
            table.insertRow(row)
            table.setItem(row, 0, QTableWidgetItem(articulo["id"]))
            table.setItem(row, 1, QTableWidgetItem(articulo["nombre"]))
            table.setItem(row, 2, QTableWidgetItem(f"{articulo['precio_publico']:.2f}"))
            table.setItem(row, 3, QTableWidgetItem(f"{articulo['precio_proveedor']:.2f}"))
            table.setItem(row, 4, QTableWidgetItem(str(articulo["stock"])))

    def limpiar_formulario_articulos(self):
        self.articulos_window.lineEditNombre.clear()
        self.articulos_window.spinPrecioPublico.setValue(0)
        self.articulos_window.spinPrecioProveedor.setValue(0)
        self.articulos_window.spinStock.setValue(0)
        self.articulos_window.tableArticulos.clearSelection()

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
            next(reader)  # Saltar encabezado
            self.lista_articulos = []
            for row in reader:
                articulo = {
                    "id": row[0],
                    "nombre": row[1],
                    "precio_publico": float(row[2]),
                    "precio_proveedor": float(row[3]),
                    "stock": int(row[4])
                }
                self.lista_articulos.append(articulo)

        self.actualizar_tabla_articulos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = PaginaPrincipal()
    main_window.show()
    sys.exit(app.exec())
