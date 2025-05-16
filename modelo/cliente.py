from modelo.entidad_base import EntidadBase

class Cliente(EntidadBase):
    def __init__(self, nombre, apellido, direccion, telefono):
        super().__init__()
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Cliente({self.nombre} {self.apellido}, Tel: {self.telefono})"
