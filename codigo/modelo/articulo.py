from codigo.controlador.AlertaStock import AlertaStock
from codigo.modelo.entidad_base import EntidadBase
from codigo.modelo.excepciones import StockInsuficienteError

class Articulo(EntidadBase):
    def __init__(self, nombre, precio_publico, precio_proveedor, stock):
        super().__init__()
        self.nombre = nombre
        self.precio_publico = precio_publico
        self.precio_proveedor = precio_proveedor
        self.stock = stock
        self.alerta_stock = AlertaStock()  # Se usa "alerta_stock" de manera consistente

    def reducir_stock(self, cantidad: int):
        if cantidad > self.stock:
            raise StockInsuficienteError(f"Stock insuficiente para {self.nombre}")
        self.stock -= cantidad
        if self.stock < 5:
            self.alerta_stock.notificar(self.nombre, self.stock)

    def validar_stock(self, cantidad):
        return self.stock >= cantidad

    def __str__(self):
        return f"Articulo({self.nombre}, Stock: {self.stock})"
