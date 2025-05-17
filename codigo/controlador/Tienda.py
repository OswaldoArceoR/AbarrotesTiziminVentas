from codigo.modelo.repositorio_clientes import RepositorioClientes
from codigo.modelo.repositorio_ventas import RepositorioVentas
from codigo.modelo.repositorio_articulos import RepositorioArticulos

class Tienda:
    _instancia = None  # Variable de clase para el Singleton

    def __init__(self):
        if Tienda._instancia is not None:
            raise Exception("¡Usa get_instance() para obtener la instancia!")
        self.repo_clientes = RepositorioClientes()
        self.repo_articulos = RepositorioArticulos()
        self.repo_ventas = RepositorioVentas()

    @classmethod
    def get_instance(cls):
        if cls._instancia is None:
            cls._instancia = Tienda()
        return cls._instancia

    # Métodos para acceder a los repositorios
    def get_repo_clientes(self):
        return self.repo_clientes

    def get_repo_articulos(self):
        return self.repo_articulos

    def get_repo_ventas(self):
        return self.repo_ventas