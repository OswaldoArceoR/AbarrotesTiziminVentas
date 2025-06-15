import os
import csv
from datetime import datetime
from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QApplication, QHeaderView
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIcon

# Rutas relativas al directorio donde está este archivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "registroVentas.csv")
CSV_CLIENTES = os.path.join(BASE_DIR, "registroClientes.csv")
CSV_ARTICULOS = os.path.join(BASE_DIR, "registroArticulos.csv")

from codigo.controlador.TicketSimpleFactory import TicketSimpleFactory
from codigo.controlador.AlertaStock import AlertaStock

class Ventas(QWidget):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(BASE_DIR, "Ventas.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"No se encontró el archivo UI: {ui_path}")
        loadUi(ui_path, self)

        # Establece el icono de la ventana manualmente
        icon_path = os.path.join("codigo", "vista", "logo sin nombre.png")
        if os.path.exists(os.path.join(BASE_DIR, "logo sin nombre.png")):
            icon_path = os.path.join(BASE_DIR, "logo sin nombre.png")
        icon = QIcon(icon_path)
        self.setWindowIcon(icon)
        # Establece el icono global para la barra de tareas
        QApplication.setWindowIcon(icon)

        # Listas para la venta actual
        self.productos_disponibles = []
        self.productos_venta = []
        self.total_venta = 0.0

        # Cargar clientes y productos
        self.cargar_clientes()
        self.cargar_productos()

        # Conectar botones
        self.btnAgregarProducto.clicked.connect(self.agregar_producto_a_venta)
        self.btnEliminarProducto.clicked.connect(self.eliminar_producto_de_venta)
        self.btnTerminarVenta.clicked.connect(self.terminar_venta)

        # Inicializar tabla de productos en venta
        self.tablaVenta.setRowCount(0)
        self.actualizar_total()

        self.alerta_stock = AlertaStock(umbral_stock=3)

        # Ajustar columnas de las tablas para que se estiren al tamaño de la ventana
        self.tablaProductos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tablaVenta.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def showEvent(self, event):
        # Recarga productos y clientes cada vez que la ventana se muestra
        self.cargar_clientes()
        self.cargar_productos()
        super().showEvent(event)

    def cargar_clientes(self):
        self.comboCliente.clear()
        if not os.path.exists(CSV_CLIENTES):
            print(f"registroCliente.csv no encontrado en: {CSV_CLIENTES}")
            return
        with open(CSV_CLIENTES, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            encabezado = next(reader, None)
            for row in reader:
                # Solo agrega si la fila tiene datos y el nombre no es vacío ni igual al encabezado
                if row and row[0].strip() and (not encabezado or row[0].strip() != encabezado[0].strip()):
                    self.comboCliente.addItem(row[1].strip())
        if self.comboCliente.count() == 0:
            print("No se encontraron clientes válidos en registroCliente.csv")

    def cargar_productos(self):
        self.productos_disponibles.clear()
        self.tablaProductos.setRowCount(0)
        if not os.path.exists(CSV_ARTICULOS):
            print(f"registroArticulos.csv no encontrado en: {CSV_ARTICULOS}")
            return
        with open(CSV_ARTICULOS, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                if len(row) >= 5:
                    producto = {
                        "codigo": row[0],
                        "nombre": row[1],
                        "precio": float(row[2]),
                        "stock": int(row[4])
                    }
                    self.productos_disponibles.append(producto)
        # Ajustar columnas: Código, Nombre, Precio, Stock
        self.tablaProductos.setColumnCount(4)
        self.tablaProductos.setHorizontalHeaderLabels(["Código", "Nombre", "Precio", "Stock"])
        for idx, prod in enumerate(self.productos_disponibles):
            self.tablaProductos.insertRow(idx)
            self.tablaProductos.setItem(idx, 0, QTableWidgetItem(prod["codigo"]))
            self.tablaProductos.setItem(idx, 1, QTableWidgetItem(prod["nombre"]))
            self.tablaProductos.setItem(idx, 2, QTableWidgetItem(f"${prod['precio']:.2f}"))
            self.tablaProductos.setItem(idx, 3, QTableWidgetItem(str(prod["stock"])))

    def agregar_producto_a_venta(self):
        row = self.tablaProductos.currentRow()
        if (row < 0 or row >= len(self.productos_disponibles)):
            QMessageBox.warning(self, "Error", "Seleccione un producto para agregar.")
            return
        producto = self.productos_disponibles[row]

        # Contar cuántas veces ya se ha agregado este producto a la venta
        cantidad_en_venta = sum(1 for p in self.productos_venta if p["codigo"] == producto["codigo"])

        # Verificar stock disponible
        if producto["stock"] <= 0:
            QMessageBox.warning(self, "Stock insuficiente", f"No hay stock disponible para '{producto['nombre']}'.")
            fprint(f"Intento de agregar '{producto['nombre']}' sin stock disponible.")
            return
        if cantidad_en_venta >= producto["stock"]:
            QMessageBox.warning(self, "Stock insuficiente", f"No puedes agregar más unidades de '{producto['nombre']}' de las disponibles ({producto['stock']}).")
            fprint(f"Intento de agregar más unidades de '{producto['nombre']}' que el stock disponible.")
            return

        self.productos_venta.append(producto)
        self.actualizar_tabla_venta()
        self.actualizar_total()

    def eliminar_producto_de_venta(self):
        row = self.tablaVenta.currentRow()
        if row < 0 or row >= len(self.productos_venta):
            QMessageBox.warning(self, "Error", "Seleccione un producto para eliminar.")
            return
        del self.productos_venta[row]
        self.actualizar_tabla_venta()
        self.actualizar_total()

    def terminar_venta(self):
        cliente = self.comboCliente.currentText()
        if not cliente:
            QMessageBox.warning(self, "Error", "Debe seleccionar un cliente.")
            return
        if not self.productos_venta:
            QMessageBox.warning(self, "Error", "Debe agregar al menos un producto.")
            return
        total = self.total_venta
        productos_str = ";".join([f"{p['codigo']}:{p['nombre']}:{p['precio']}" for p in self.productos_venta])
        venta_dict = {
            "id": self.obtener_nueva_id(),
            "cliente": cliente,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "productos": productos_str,
            "total": total
        }
        self.guardar_venta_csv(venta_dict)

        # --- Actualizar stock de artículos vendidos ---
        self.actualizar_stock_articulos_vendidos()

        # --- Recargar productos para actualizar stock en la tabla ---
        self.cargar_productos()

        # --- Generar ticket usando TicketSimpleFactory ---
        # Clases mínimas para adaptarse a la fábrica (ajusta si tienes modelos reales)
        class ClienteObj:
            def __init__(self, nombre):
                self.nombre = nombre

        class ArticuloObj:
            def __init__(self, nombre):
                self.nombre = nombre

        class DetalleVenta:
            def __init__(self, articulo, cantidad, subtotal):
                self.articulo = articulo
                self.cantidad = cantidad
                self.subtotal = subtotal

        class VentaObj:
            def __init__(self, cliente, detalles, total):
                self.cliente = cliente
                self.detalles = detalles
                self.total = total

        detalles = []
        for p in self.productos_venta:
            articulo = ArticuloObj(p["nombre"])
            detalles.append(DetalleVenta(articulo, 1, p["precio"]))

        venta_obj = VentaObj(ClienteObj(cliente), detalles, total)
        ticket_factory = TicketSimpleFactory()
        ticket = ticket_factory.crear_ticket(venta_obj)

        mensaje = f"La venta se ha registrado correctamente.\n\nTicket:\n{ticket.contenido}"
        if hasattr(ticket, "pdf_path") and ticket.pdf_path:
            mensaje += f"\n\nTicket PDF generado en:\n{ticket.pdf_path}"
        QMessageBox.information(self, "Venta registrada", mensaje)

        self.productos_venta.clear()
        self.actualizar_tabla_venta()
        self.actualizar_total()

    def actualizar_stock_articulos_vendidos(self):
        # Cargar todos los artículos del CSV
        if not os.path.exists(CSV_ARTICULOS):
            return
        articulos = []
        with open(CSV_ARTICULOS, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            encabezado = next(reader, None)
            for row in reader:
                if len(row) >= 5:
                    articulo = {
                        "id": row[0],
                        "nombre": row[1],
                        "precio_publico": float(row[2]),
                        "precio_proveedor": float(row[3]),
                        "stock": int(row[4])
                    }
                    articulos.append(articulo)
        articulos_bajo_stock = []
        # Restar 1 al stock de cada producto vendido
        for vendido in self.productos_venta:
            for articulo in articulos:
                if articulo["id"] == vendido["codigo"]:
                    if articulo["stock"] > 0:
                        articulo["stock"] -= 1
                        # Verificar alerta de stock bajo
                        if articulo["stock"] <= self.alerta_stock.umbral_stock:
                            articulos_bajo_stock.append((articulo["nombre"], articulo["stock"]))
                            self.alerta_stock.verificar_stock(articulo["nombre"], articulo["stock"])
        # Guardar los artículos actualizados en el CSV
        with open(CSV_ARTICULOS, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Nombre", "Precio Público", "Precio Proveedor", "Stock"])
            for articulo in articulos:
                writer.writerow([
                    articulo["id"],
                    articulo["nombre"],
                    articulo["precio_publico"],
                    articulo["precio_proveedor"],
                    articulo["stock"]
                ])
        # Mostrar advertencia si hay artículos con poco stock
        if articulos_bajo_stock:
            mensaje = "¡Atención! Los siguientes artículos tienen poco stock:\n"
            for nombre, stock in articulos_bajo_stock:
                mensaje += f"- {nombre}: {stock} unidades\n"
            QMessageBox.warning(self, "Stock bajo", mensaje)

    def actualizar_tabla_venta(self):
        self.tablaVenta.setRowCount(0)
        for idx, prod in enumerate(self.productos_venta):
            self.tablaVenta.insertRow(idx)
            self.tablaVenta.setItem(idx, 0, QTableWidgetItem(prod["codigo"]))
            self.tablaVenta.setItem(idx, 1, QTableWidgetItem(prod["nombre"]))
            self.tablaVenta.setItem(idx, 2, QTableWidgetItem(f"${prod['precio']:.2f}"))

    def actualizar_total(self):
        self.total_venta = sum([p["precio"] for p in self.productos_venta])
        self.lblTotalVenta.setText(f"Total: ${self.total_venta:.2f}")

    def obtener_nueva_id(self):
        if not os.path.exists(CSV_FILE):
            return "1"
        with open(CSV_FILE, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)
            ids = [int(row[0]) for row in reader if row and row[0].isdigit()]
            return str(max(ids) + 1) if ids else "1"

    def guardar_venta_csv(self, venta):
        existe = os.path.exists(CSV_FILE)
        with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not existe:
                writer.writerow(["ID", "Cliente", "Fecha", "Productos", "Total"])
            writer.writerow([venta["id"], venta["cliente"], venta["fecha"], venta["productos"], venta["total"]])

# Añade esta función al final del archivo si no existe fprint
def fprint(msg):
    print(f"[VENTAS] {msg}")
