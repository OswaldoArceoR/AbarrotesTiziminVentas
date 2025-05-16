import uuid

class EntidadBase:
    def __init__(self):
        self.id = self.generar_id()

    def generar_id(self):
        return str(uuid.uuid4())
