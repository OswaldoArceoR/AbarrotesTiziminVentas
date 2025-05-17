from abc import ABC, abstractmethod
from codigo.modelo.file_manager import FileManager

class Repositorio(ABC):
    def __init__(self, nombreArchivo, campos):
        self.file_manager = FileManager()
        self.nombreArchivo = nombreArchivo  # Nombre del archivo CSV
        self.campos = campos  # Campos del CSV
        self.entidades = self.leerTodos()  # Cargar datos al iniciar

    @abstractmethod
    def crearInstancia(self, datos):
        """Cada subclase debe definir cómo convertir diccionarios CSV a instancias"""
        pass

    def agregar(self, entidad):
        self.entidades.append(entidad.__dict__)
        self.guardarTodos()

    def buscar(self, id):
        for entidad in self.entidades:
            if entidad["id"] == id:
                return self.crearInstancia(entidad)
        return None

    def eliminar(self, id):
        self.entidades = [e for e in self.entidades if e["id"] != id]
        self.guardarTodos()

    def listarTodos(self):
        return [self.crearInstancia(e) for e in self.entidades]

    def guardarTodos(self):
        self.file_manager.guardarCsv(self.nombreArchivo, self.entidades, self.campos)

    def leerTodos(self):
        return self.file_manager.leerCsv(self.nombreArchivo)
