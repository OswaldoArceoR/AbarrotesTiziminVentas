import os
import csv
from datetime import datetime
from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt6.uic import loadUi

# Definición de la ruta para el archivo CSV donde se almacenarán las ventas:
CSV_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "registroVentas.csv")

class Ventas(QWidget):
    def __init__(self):
        super().__init__()
        base_dir = os.path.abspath(os.path.dirname(__file__))
        # IMPORTANTE: El archivo de la interfaz debe llamarse "Ventas.ui" (con V mayúscula)
        ui_path = os.path.join(base_dir, "Ventas.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"No se encontró el archivo UI: {ui_path}")
        loadUi(ui_path, self)

        self.lista_ventas = []

        # Conectar botones a sus funciones:
        self.btnRegistrarVenta.clicked.connect(self.registrar_venta)
        self.btnActualizarVenta.clicked.connect(self.actualizar_venta)
        self.btnEliminarVenta.clicked.connect(self.eliminar_venta)
        self.tableVentas.itemSelectionChanged.connect(self.mostrar_venta_seleccionada)

        # Cargar los datos si existen y actualizar la tabla
        self.cargar_datos_csv()
        self.actualizar_tabla()

    def registrar_venta(self):
        cliente = self.lineEditCliente.text().strip()
        total = self.spinTotal.value()
        if not cliente:
            QMessageBox.warning(self, "Error", "El cliente no puede estar vacío.")
            return
        if total <= 0:
            QMessageBox.warning(self, "Error", "El total debe ser mayor a 0.")
            return
        venta = {
            "id": str(len(self.lista_ventas) + 1),
            "cliente": cliente,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total": total
        }
        self.lista_ventas.append(venta)
        self.guardar_datos_csv()
        self.actualizar_tabla()
        self.limpiar_formulario()

    def actualizar_venta(self):
        index = self.tableVentas.currentRow()
        if index < 0 or index >= len(self.lista_ventas):
            QMessageBox.warning(self, "Error", "Seleccione una venta para actualizar.")
            return
        cliente = self.lineEditCliente.text().strip()
        total = self.spinTotal.value()
        if not cliente:
            QMessageBox.warning(self, "Error", "El cliente no puede estar vacío.")
            return
        if total <= 0:
            QMessageBox.warning(self, "Error", "El total debe ser mayor a 0.")
            return
        self.lista_ventas[index]["cliente"] = cliente
        self.lista_ventas[index]["total"] = total
        self.guardar_datos_csv()
        self.actualizar_tabla()
        self.limpiar_formulario()

    def eliminar_venta(self):
        index = self.tableVentas.currentRow()
        if index < 0 or index >= len(self.lista_ventas):
            QMessageBox.warning(self, "Error", "Seleccione una venta para eliminar.")
            return
        del self.lista_ventas[index]
        self.guardar_datos_csv()
        self.actualizar_tabla()
        self.limpiar_formulario()

    def actualizar_tabla(self):
        self.tableVentas.setRowCount(0)
        for venta in self.lista_ventas:
            row = self.tableVentas.rowCount()
            self.tableVentas.insertRow(row)
            self.tableVentas.setItem(row, 0, QTableWidgetItem(venta["id"]))
            self.tableVentas.setItem(row, 1, QTableWidgetItem(venta["cliente"]))
            self.tableVentas.setItem(row, 2, QTableWidgetItem(venta["fecha"]))
            self.tableVentas.setItem(row, 3, QTableWidgetItem(f"${venta['total']:.2f}"))

    def limpiar_formulario(self):
        self.lineEditCliente.clear()
        self.spinTotal.setValue(0)
        self.tableVentas.clearSelection()

    def guardar_datos_csv(self):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Cliente", "Fecha", "Total"])
            for venta in self.lista_ventas:
                writer.writerow([venta["id"], venta["cliente"], venta["fecha"], venta["total"]])

    def cargar_datos_csv(self):
        if not os.path.exists(CSV_FILE):
            return
        with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            try:
                next(reader)  # Saltar encabezado
            except StopIteration:
                return
            self.lista_ventas = []
            for row in reader:
                try:
                    venta = {
                        "id": row[0],
                        "cliente": row[1],
                        "fecha": row[2],
                        "total": float(row[3])
                    }
                    self.lista_ventas.append(venta)
                except (ValueError, IndexError):
                    continue
        self.actualizar_tabla()

    def mostrar_venta_seleccionada(self):
        index = self.tableVentas.currentRow()
        if index < 0 or index >= len(self.lista_ventas):
            self.limpiar_formulario()
            return
        venta = self.lista_ventas[index]
        self.lineEditCliente.setText(venta["cliente"])
        self.spinTotal.setValue(venta["total"])
