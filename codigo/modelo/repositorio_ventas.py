from codigo.modelo.repositorio import Repositorio
from codigo.modelo.venta import Venta

class RepositorioVentas(Repositorio):
    def __init__(self):
        super().__init__("ventas.csv", ["id", "cliente", "fecha", "total"])

    def crear_instancia(self, datos):
        return Venta(datos["cliente"])
