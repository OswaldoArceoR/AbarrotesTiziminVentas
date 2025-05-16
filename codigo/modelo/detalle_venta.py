from codigo.modelo.articulo import Articulo

class DetalleVenta:
    def __init__(self, articulo: Articulo, cantidad: int):
        self.articulo = articulo
        self.cantidad = cantidad
        self.subtotal = self.calcular_subtotal()

    def calcular_subtotal(self):
        return self.articulo.precio_publico * self.cantidad

    def __str__(self):
        return f"DetalleVenta(Articulo: {self.articulo.nombre}, Cantidad: {self.cantidad}, Subtotal: {self.subtotal})"
