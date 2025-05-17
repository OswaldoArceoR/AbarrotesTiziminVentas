from codigo.modelo.repositorio import Repositorio
from codigo.modelo.cliente import Cliente

class RepositorioClientes(Repositorio):
    def __init__(self):
        super().__init__("clientes.csv", ["id", "nombre", "apellido", "direccion", "telefono"])

    def crear_instancia(self, datos):
        return Cliente(datos["nombre"], datos["apellido"], datos["direccion"], datos["telefono"])
