class Ticket:
    def __init__(self, venta):
        self.venta = venta
        self.contenido = self.generar_contenido()

    def generar_contenido(self):
        detalles = "\n".join([f"{d.articulo.nombre} x{d.cantidad} = ${d.subtotal}" for d in self.venta.detalles])
        return f"Ticket de Venta\nCliente: {self.venta.cliente.nombre}\nDetalles:\n{detalles}\nTotal: ${self.venta.total}"

    def mostrar(self):
        print(self.contenido)

    def __str__(self):
        return f"Ticket(Venta ID: {self.venta.id}, Total: {self.venta.total})"
