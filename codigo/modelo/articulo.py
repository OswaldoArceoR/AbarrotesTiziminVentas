from codigo.modelo.entidad_base import EntidadBase

class Articulo(EntidadBase):
    def __init__(self, nombre, precio_publico, precio_proveedor, stock):
        super().__init__()
        self.nombre = nombre
        self.precio_publico = precio_publico
        self.precio_proveedor = precio_proveedor
        self.stock = stock

    def validar_stock(self, cantidad):
        return self.stock >= cantidad

    def __str__(self):
        return f"Articulo({self.nombre}, Stock: {self.stock})"
