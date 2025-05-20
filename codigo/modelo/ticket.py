class Ticket:
    def __init__(self, venta, contenido=None):
        self.venta = venta
        if contenido is not None:
            self.contenido = contenido
        else:
            self.contenido = self.generar_contenido()

    def generar_contenido(self):
        if not self.venta:
            return "Ticket vacío"
        detalles = "\n".join([f"{d.articulo.nombre} x{d.cantidad} = ${d.subtotal}" for d in self.venta.detalles])
        return f"Ticket de Venta\nCliente: {self.venta.cliente.nombre}\nDetalles:\n{detalles}\nTotal: ${self.venta.total}"

    def mostrar(self):
        print(self.contenido)

    def __str__(self):
        if self.venta:
            return f"Ticket(Venta ID: {self.venta.id}, Total: {self.venta.total})"
        return "Ticket(Sin venta)"
