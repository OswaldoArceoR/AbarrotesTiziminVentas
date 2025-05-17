from codigo.modelo.ticket import Ticket
from codigo.modelo.venta import Venta
from datetime import datetime


class TicketSimpleFactory:
    def crear_ticket(self, venta: Venta) -> Ticket:
        """Implementación concreta de ticket en texto plano."""
        contenido = f"""
        ╔══════════════════════════════╗
        ║        ABARROTES TIZIMÍN     ║
        ║   {datetime.now().strftime('%d/%m/%Y %H:%M')}   ║
        ╚══════════════════════════════╝
        Cliente: {venta.cliente.nombre}
        {'-' * 30}"""

        detalles = "\n".join(
            f"{detalle.articulo.nombre.ljust(20)} x{detalle.cantidad} ${detalle.subtotal:.2f}"
            for detalle in venta.detalles
        )
        contenido += f"\n{detalles}\n{'-' * 30}\nTotal: ${venta.total:.2f}"

        return Ticket(venta, contenido)