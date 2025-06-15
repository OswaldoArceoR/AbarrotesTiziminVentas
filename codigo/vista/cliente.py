import os
from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QApplication
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QHeaderView  # <-- Añade esto
import csv
from codigo.modelo.excepciones import ClienteDuplicadoError

CSV_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "registroClientes.csv")

class Cliente(QWidget):
    def __init__(self):
        super().__init__()

        base_dir = os.path.abspath(os.path.dirname(__file__))
        ui_path = os.path.join(base_dir, "cliente.ui")

        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"No se encontró el archivo UI: {ui_path}")

        loadUi(ui_path, self)

        # Establece el icono de la ventana manualmente
        icon_path = os.path.join("codigo", "vista", "logo sin nombre.png")
        if os.path.exists(os.path.join(base_dir, "logo sin nombre.png")):
            icon_path = os.path.join(base_dir, "logo sin nombre.png")
        icon = QIcon(icon_path)
        self.setWindowIcon(icon)
        # Establece el icono global para la barra de tareas
        QApplication.setWindowIcon(icon)

        self.lista_clientes = []

        self.btnAgregar.clicked.connect(self.agregar_cliente)
        self.btnActualizar.clicked.connect(self.actualizar_cliente)
        self.btnEliminar.clicked.connect(self.eliminar_cliente)
        self.tableClientes.itemSelectionChanged.connect(self.cargar_datos_cliente_seleccionado)

        self.cargar_datos_csv()
        self.actualizar_tabla_clientes()

        # Ajustar columnas de la tabla para que se estiren al tamaño de la ventana
        self.tableClientes.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def generar_id_unico(self):
        ids = [int(cliente["id"]) for cliente in self.lista_clientes if cliente["id"].isdigit()]
        return str(max(ids) + 1) if ids else "1"

    def agregar_cliente(self):
        nombre = self.lineEditNombre.text().strip()
        apellido = self.lineEditApellido.text().strip()
        calle = self.lineEditCalle.text().strip()
        numero = self.lineEditNumero.text().strip()
        colonia = self.lineEditColonia.text().strip()
        cp = self.lineEditCP.text().strip()
        ciudad = self.lineEditCiudad.text().strip()
        estado = self.lineEditEstado.text().strip()
        telefono = self.lineEditTelefono.text().strip()

        if not nombre or not apellido:
            QMessageBox.warning(self, "Error", "El nombre y apellido paterno no pueden estar vacíos.")
            return
        if not calle or not numero or not colonia or not cp or not ciudad or not estado:
            QMessageBox.warning(self, "Error", "Todos los campos de dirección son obligatorios.")
            return
        if not telefono:
            QMessageBox.warning(self, "Error", "El teléfono no puede estar vacío.")
            return

        try:
            # Validar duplicados por nombre y apellido
            for cliente in self.lista_clientes:
                if cliente["nombre"] == nombre and cliente["apellido"] == apellido:
                    raise ClienteDuplicadoError(f"El cliente '{nombre} {apellido}' ya existe.")

            cliente = {
                "id": self.generar_id_unico(),
                "nombre": nombre,
                "apellido": apellido,
                "calle": calle,
                "numero": numero,
                "colonia": colonia,
                "cp": cp,
                "ciudad": ciudad,
                "estado": estado,
                "telefono": telefono
            }

            self.lista_clientes.append(cliente)
            self.guardar_datos_csv()
            self.actualizar_tabla_clientes()
            self.limpiar_formulario_clientes()
        except ClienteDuplicadoError as e:
            QMessageBox.warning(self, "Error De Duplicado", str(e))

    def actualizar_cliente(self):
        selected = self.tableClientes.currentRow()
        if selected < 0 or selected >= len(self.lista_clientes):
            QMessageBox.warning(self, "Error", "Seleccione un cliente para actualizar.")
            return

        nombre = self.lineEditNombre.text().strip()
        apellido = self.lineEditApellido.text().strip()
        calle = self.lineEditCalle.text().strip()
        numero = self.lineEditNumero.text().strip()
        colonia = self.lineEditColonia.text().strip()
        cp = self.lineEditCP.text().strip()
        ciudad = self.lineEditCiudad.text().strip()
        estado = self.lineEditEstado.text().strip()
        telefono = self.lineEditTelefono.text().strip()

        if not nombre or not apellido:
            QMessageBox.warning(self, "Error", "El nombre y apellido paterno no pueden estar vacíos.")
            return
        if not calle or not numero or not colonia or not cp or not ciudad or not estado:
            QMessageBox.warning(self, "Error", "Todos los campos de dirección son obligatorios.")
            return
        if not telefono:
            QMessageBox.warning(self, "Error", "El teléfono no puede estar vacío.")
            return

        self.lista_clientes[selected] = {
            "id": self.lista_clientes[selected]["id"],
            "nombre": nombre,
            "apellido": apellido,
            "calle": calle,
            "numero": numero,
            "colonia": colonia,
            "cp": cp,
            "ciudad": ciudad,
            "estado": estado,
            "telefono": telefono
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
            self.tableClientes.setItem(row, 2, QTableWidgetItem(cliente["apellido"]))
            self.tableClientes.setItem(row, 3, QTableWidgetItem(cliente["calle"]))
            self.tableClientes.setItem(row, 4, QTableWidgetItem(cliente["numero"]))
            self.tableClientes.setItem(row, 5, QTableWidgetItem(cliente["colonia"]))
            self.tableClientes.setItem(row, 6, QTableWidgetItem(cliente["cp"]))
            self.tableClientes.setItem(row, 7, QTableWidgetItem(cliente["ciudad"]))
            self.tableClientes.setItem(row, 8, QTableWidgetItem(cliente["estado"]))
            self.tableClientes.setItem(row, 9, QTableWidgetItem(cliente["telefono"]))

    def limpiar_formulario_clientes(self):
        self.lineEditNombre.clear()
        self.lineEditApellido.clear()
        self.lineEditCalle.clear()
        self.lineEditNumero.clear()
        self.lineEditColonia.clear()
        self.lineEditCP.clear()
        self.lineEditCiudad.clear()
        self.lineEditEstado.clear()
        self.lineEditTelefono.clear()
        self.tableClientes.clearSelection()

    def guardar_datos_csv(self):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "ID", "Nombre", "Apellido", "Calle", "Numero", "Colonia", "CP", "Ciudad", "Estado", "Telefono"
            ])
            for cliente in self.lista_clientes:
                writer.writerow([
                    cliente["id"],
                    cliente["nombre"],
                    cliente["apellido"],
                    cliente["calle"],
                    cliente["numero"],
                    cliente["colonia"],
                    cliente["cp"],
                    cliente["ciudad"],
                    cliente["estado"],
                    cliente["telefono"]
                ])

    def cargar_datos_csv(self):
        if not os.path.exists(CSV_FILE):
            return

        with open(CSV_FILE, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  # saltar encabezado
            self.lista_clientes = []
            for row in reader:
                try:
                    cliente = {
                        "id": row[0],
                        "nombre": row[1],
                        "apellido": row[2],
                        "calle": row[3],
                        "numero": row[4],
                        "colonia": row[5],
                        "cp": row[6],
                        "ciudad": row[7],
                        "estado": row[8],
                        "telefono": row[9]
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
        self.lineEditApellido.setText(cliente["apellido"])
        self.lineEditCalle.setText(cliente["calle"])
        self.lineEditNumero.setText(cliente["numero"])
        self.lineEditColonia.setText(cliente["colonia"])
        self.lineEditCP.setText(cliente["cp"])
        self.lineEditCiudad.setText(cliente["ciudad"])
        self.lineEditEstado.setText(cliente["estado"])
        self.lineEditTelefono.setText(cliente["telefono"])
