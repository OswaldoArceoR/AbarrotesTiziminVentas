from codigo.modelo.detalle_venta import DetalleVenta
from codigo.modelo.repositorio_ventas import RepositorioVentas
from codigo.controlador.TicketFactory import TicketFactory
from codigo.modelo.venta import Venta
from codigo.modelo.ticket import Ticket
from codigo.modelo.excepciones import StockInsuficienteError


class VentaControlador:
    def __init__(self):
        self.repo = RepositorioVentas()  # Inyección de dependencia
        self.fabrica_ticket = TicketFactory()  # Patrón Factory

    def iniciar_venta(self, cliente) -> Venta:
        """Crea una nueva venta asociada a un cliente (RF-03)."""
        venta = Venta(cliente)
        return venta

    def agregar_detalle(self, venta, articulo, cantidad):
        cantidad_existente = sum(
            d.cantidad for d in venta.detalles if d.articulo == articulo
        )
        cantidad_total = cantidad_existente + cantidad

        if not articulo.validar_stock(cantidad_total):
            raise StockInsuficienteError(f"Stock insuficiente: {articulo.nombre}")

        detalle = DetalleVenta(articulo, cantidad)
        venta.agregar_detalle(detalle)
        return venta

    def generar_ticket(self, venta) -> Ticket:
        """Genera un ticket para la venta (RF-05)."""
        ticket = self.fabrica_ticket.crear_ticket(venta)
        return ticket

    def finalizar_venta(self, venta):
        """Guarda la venta y actualiza stock (RF-03, RF-07)."""
        self.repo.agregar(venta)
        for detalle in venta.detalles:
            detalle.articulo.actualizar_stock(-detalle.cantidad)  # Reduce stock
        return self.generar_ticket(venta)

    def listar_ventas(self) -> list[Venta]:
        """Retorna el historial de ventas (RF-09)."""
        return self.repo.listar_todos()

    def listar_ventas_por_cliente(self, cliente) -> list[Venta]:
        """Filtra ventas por cliente (RF-09)."""
        return self.repo.listar_por_cliente(cliente)
