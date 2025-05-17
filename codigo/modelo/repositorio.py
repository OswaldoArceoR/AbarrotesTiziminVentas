from abc import ABC, abstractmethod

class Repositorio(ABC):  # Hereda de ABC para ser abstracta
    def __init__(self):
        self.entidades = {}

    @abstractmethod
    def agregar(self, entidad):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass

    @abstractmethod
    def listar_todos(self):
        pass
