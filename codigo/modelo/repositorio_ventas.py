from codigo.modelo.repositorio import Repositorio

class RepositorioVentas(Repositorio):
    def __init__(self):
        super().__init__()

    def listar_compras_por_cliente(self, cliente):
        return [v for v in self.entidades.values() if v.cliente.id == cliente.id]
