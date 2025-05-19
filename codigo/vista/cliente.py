import os
from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt6.uic import loadUi
import csv

CSV_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "registroClientes.csv")

class Cliente(QWidget):
    def __init__(self):
        super().__init__()

        base_dir = os.path.abspath(os.path.dirname(__file__))
        ui_path = os.path.join(base_dir, "cliente.ui")

        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"No se encontró el archivo UI: {ui_path}")

        loadUi(ui_path, self)

        self.lista_clientes = []

        # Conectar botones y tabla
        self.btnAgregar.clicked.connect(self.agregar_cliente)
        self.btnActualizar.clicked.connect(self.actualizar_cliente)
        self.btnEliminar.clicked.connect(self.eliminar_cliente)
        self.tableClientes.itemSelectionChanged.connect(self.cargar_datos_cliente_seleccionado)

        # Cargar datos guardados
        self.cargar_datos_csv()
        self.actualizar_tabla_clientes()

    def agregar_cliente(self):
        nombre = self.lineEditNombre.text().strip()
        correo = self.lineEditCorreo.text().strip()

        if not nombre:
            QMessageBox.warning(self, "Error", "El nombre no puede estar vacío.")
            return

        if not correo:
            QMessageBox.warning(self, "Error", "El correo no puede estar vacío.")
            return

        cliente = {
            "id": str(len(self.lista_clientes) + 1),
            "nombre": nombre,
            "correo": correo
        }

        self.lista_clientes.append(cliente)
        self.guardar_datos_csv()
        self.actualizar_tabla_clientes()
        self.limpiar_formulario_clientes()

    def actualizar_cliente(self):
        selected = self.tableClientes.currentRow()
        if selected < 0 or selected >= len(self.lista_clientes):
            QMessageBox.warning(self, "Error", "Seleccione un cliente para actualizar.")
            return

        nombre = self.lineEditNombre.text().strip()
        correo = self.lineEditCorreo.text().strip()

        if not nombre:
            QMessageBox.warning(self, "Error", "El nombre no puede estar vacío.")
            return

        if not correo:
            QMessageBox.warning(self, "Error", "El correo no puede estar vacío.")
            return

        self.lista_clientes[selected] = {
            "id": self.lista_clientes[selected]["id"],
            "nombre": nombre,
            "correo": correo
        }

        self.guardar_datos_csv()
        self.actualizar_tabla_clientes()
        self.limpiar_formulario_clientes()

    def eliminar_cliente(self):
        selected = self.tableClientes.currentRow()
        if selected < 0 or selected >= len(self.lista_clientes):
            QMessageBox.warning(self, "Error", "Seleccione un cliente para eliminar.")
            return

        del self.lista_clientes[selected]
        self.guardar_datos_csv()
        self.actualizar_tabla_clientes()
        self.limpiar_formulario_clientes()

    def actualizar_tabla_clientes(self):
        self.tableClientes.setRowCount(0)

        for cliente in self.lista_clientes:
            row = self.tableClientes.rowCount()
            self.tableClientes.insertRow(row)
            self.tableClientes.setItem(row, 0, QTableWidgetItem(cliente["id"]))
            self.tableClientes.setItem(row, 1, QTableWidgetItem(cliente["nombre"]))
            self.tableClientes.setItem(row, 2, QTableWidgetItem(cliente["correo"]))

    def limpiar_formulario_clientes(self):
        self.lineEditNombre.clear()
        self.lineEditCorreo.clear()
        self.tableClientes.clearSelection()

    def guardar_datos_csv(self):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nombre", "Correo"])
            for cliente in self.lista_clientes:
                writer.writerow([
                    cliente["id"],
                    cliente["nombre"],
                    cliente["correo"]
                ])

    def cargar_datos_csv(self):
        if not os.path.exists(CSV_FILE):
            return

        with open(CSV_FILE, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # saltar encabezado
            self.lista_clientes = []
            for row in reader:
                try:
                    cliente = {
                        "id": row[0],
                        "nombre": row[1],
                        "correo": row[2]
                    }
                    self.lista_clientes.append(cliente)
                except (IndexError, ValueError):
                    pass

        self.actualizar_tabla_clientes()

    def cargar_datos_cliente_seleccionado(self):
        selected = self.tableClientes.currentRow()
        if selected < 0 or selected >= len(self.lista_clientes):
            self.limpiar_formulario_clientes()
            return

        cliente = self.lista_clientes[selected]
        self.lineEditNombre.setText(cliente["nombre"])
        self.lineEditCorreo.setText(cliente["correo"])
