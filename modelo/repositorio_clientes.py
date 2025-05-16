from modelo.repositorio import Repositorio

class RepositorioClientes(Repositorio):
    def __init__(self):
        super().__init__()

    def buscar_por_nombre(self, nombre):
        return [c for c in self.entidades.values() if c.nombre.lower() == nombre.lower()]
