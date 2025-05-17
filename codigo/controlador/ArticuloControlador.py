from codigo.modelo.articulo import Articulo
from codigo.modelo.repositorio_articulos import RepositorioArticulos

class ArticuloControlador:
    def __init__(self, repo_articulos: RepositorioArticulos):
        self.repo = repo_articulos  # Repositorio inyectado (usando el de Tienda)

    def registrar_articulo(self, articulo: Articulo) -> None:
        """Registra un nuevo artículo (RF-02). Valida stock mínimo."""
        if not isinstance(articulo, Articulo):
            raise TypeError("Se esperaba un objeto Articulo")
        if articulo.stock < 0:
            raise ValueError("El stock no puede ser negativo (RF-02)")
        self.repo.agregar(articulo)

    def listar_articulos(self) -> list[Articulo]:
        """Retorna todos los artículos registrados (RF-08)."""
        return self.re