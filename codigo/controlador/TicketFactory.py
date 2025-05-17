from typing import Protocol
from codigo.modelo.ticket import Ticket
from codigo.modelo.venta import Venta

class TicketFactory(Protocol):
    def crear_ticket(self, venta: Venta) -> Ticket:
        """Protocolo (interfaz) para crear tickets. Todas las fábricas deben implementar esto."""
        ...