from modelo.entidad_base import EntidadBase
from modelo.detalle_venta import DetalleVenta

class Venta(EntidadBase):
    def __init__(self, cliente):
        super().__init__()
        self.cliente = cliente
        self.detalles = []
        self.total = 0.0

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)
        self.total += detalle.subtotal

    def calcular_total(self):
        return self.total

    def __str__(self):
        return f"Venta(ID {self.id}, Cliente: {self.cliente.nombre}, Total: {self.total})"
