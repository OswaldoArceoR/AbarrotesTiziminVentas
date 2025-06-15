#Factory

from codigo.modelo.ticket import Ticket
from datetime import datetime
import os
import csv
from .TicketFactory import TicketFactory  # Importa la interfaz/protocolo

class TicketSimpleFactory(TicketFactory):  # Hereda explícitamente
    def crear_ticket(self, venta=None) -> Ticket:  # Firma compatible con la interfaz
        """
        Genera el ticket usando los datos del registro más reciente en el CSV de ventas.
        Utiliza la librería fpdf para crear el PDF.
        """
        # Ruta al CSV de ventas
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(base_dir, "vista", "registroVentas.csv")

        # Leer el último registro del CSV
        ultima_venta = None
        with open(csv_path, mode="r", encoding="utf-8") as f:
            reader = list(csv.reader(f))
            if len(reader) > 1:
                encabezado = reader[0]
                ultima_venta = reader[-1]
            else:
                raise Exception("No hay ventas registradas en el CSV.")

        # Extraer datos
        id_venta = ultima_venta[0]
        cliente = ultima_venta[1]
        fecha = ultima_venta[2]
        productos = ultima_venta[3]
        total = ultima_venta[4]

        # Procesar productos
        detalles = []
        for prod in productos.split(";"):
            partes = prod.split(":")
            if len(partes) == 3:
                codigo, nombre, precio = partes
                detalles.append(f"{nombre.ljust(20)} ${precio}")

        detalles_str = "\n".join(detalles)

        contenido = f"""
        ╔══════════════════════════════╗
        ║        ABARROTES TIZIMÍN     ║
        ║   {fecha}   ║
        ╚══════════════════════════════╝
        Cliente: {cliente}
        {'-' * 30}
        {detalles_str}
        {'-' * 30}
        Total: ${total}
        """

        # --- Generar PDF con fpdf ---
        pdf_path = None
        try:
            from fpdf import FPDF
        except ImportError as e:
            print("fpdf no está instalado. El ticket PDF no se generó.")
            print(f"Detalles del error: {e}")
            pdf_path = None
        else:
            tickets_dir = os.path.join(base_dir, "tickets")
            os.makedirs(tickets_dir, exist_ok=True)
            pdf_filename = f"ticket_{id_venta}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            pdf_path = os.path.join(tickets_dir, pdf_filename)
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 14)
            pdf.cell(0, 10, "ABARROTES TIZIMÍN", ln=True, align="C")
            pdf.set_font("Arial", "", 10)
            pdf.cell(0, 8, fecha, ln=True, align="C")
            pdf.ln(2)
            pdf.cell(0, 8, f"Cliente: {cliente}", ln=True)
            pdf.cell(0, 8, "-" * 40, ln=True)
            for prod in detalles:
                pdf.cell(0, 8, prod, ln=True)
            pdf.cell(0, 8, "-" * 40, ln=True)
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, f"Total: ${total}", ln=True)
            pdf.output(pdf_path)

        # Crear ticket (usa el modelo Ticket, aunque no use Venta real)
        ticket = Ticket(None)
        ticket.contenido = contenido
        ticket.pdf_path = pdf_path
        return ticket
