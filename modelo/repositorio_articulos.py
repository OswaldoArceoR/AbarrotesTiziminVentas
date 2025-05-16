from modelo.repositorio import Repositorio

class RepositorioArticulos(Repositorio):
    def __init__(self):
        super().__init__()

    def buscar_por_stock_bajo(self, limite):
        return [a for a in self.entidades.values() if a.stock < limite]
