class direccion:
    def __init__(self, calle, numero, colonia, cp, ciudad, estado):
        self.calle = calle
        self.numero = numero
        self.colonia = colonia
        self.cp = cp
        self.ciudad = ciudad
        self.estado = estado

    def __str__(self):
        return f"{self.calle} #{self.numero}, {self.colonia}, {self.ciudad}, {self.estado}, CP:{self.cp}"
