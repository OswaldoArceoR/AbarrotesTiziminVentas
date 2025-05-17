from codigo.modelo.cliente import Cliente

class ClienteControlador:
    def __init__(self, repo_clientes):
        self.repo = repo_clientes  # Inyectado desde Tienda

    def registrar_cliente(self, cliente: Cliente) -> None:
        """Registra un cliente (RF-01)"""
        if not isinstance(cliente, Cliente):
            raise TypeError("Se esperaba un objeto Cliente")
        self.repo.agregar(cliente)

    def listar_clientes(self) -> list[Cliente]:
        """Retorna todos los clientes registrados (RF-08)"""
        return self.repo.listar_todos()