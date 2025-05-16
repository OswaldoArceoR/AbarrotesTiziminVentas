class Repositorio:
    def __init__(self):
        self.entidades = {}

    def agregar(self, entidad):
        self.entidades[entidad.id] = entidad

    def buscar(self, id):
        return self.entidades.get(id, None)

    def eliminar(self, id):
        if id in self.entidades:
            del self.entidades[id]

    def listar_todos(self):
        return list(self.entidades.values())

    def __str__(self):
        return f"Repositorio({len(self.entidades)} elementos)"
