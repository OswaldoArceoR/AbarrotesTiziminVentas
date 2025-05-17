from codigo.controlador.AlertaStock import AlertaStock
from codigo.modelo.entidad_base import EntidadBase

class Articulo(EntidadBase):
    def __init__(self, nombre, precio_publico, precio_proveedor, stock):
        super().__init__()
        self.nombre = nombre
        self.precio_publico = precio_publico
        self.precio_proveedor = precio_proveedor
        self.stock = stock
        self.AlertaStock=AlertaStock()

    def reducir_stock(self, cantidad: int):
        self.stock -= cantidad
        if self.stock < 5:  # Umbral fijo (RF-10)
            self.alerta_stock.notificar(self.nombre, self.stock)

    def validar_stock(self, cantidad):
        return self.stock >= cantidad

    def __str__(self):
        return f"Articulo({self.nombre}, Stock: {self.stock})"
