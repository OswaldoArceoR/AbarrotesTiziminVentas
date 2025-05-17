from codigo.modelo.repositorio import Repositorio
from codigo.modelo.articulo import Articulo

class RepositorioArticulos(Repositorio):
    def __init__(self):
        super().__init__("articulos.csv", ["id", "nombre", "precio_publico", "precio_proveedor", "stock"])

    def crear_instancia(self, datos):
        return Articulo(datos["nombre"], float(datos["precio_publico"]), float(datos["precio_proveedor"]), int(datos["stock"]))
