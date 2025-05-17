class AlertaStock:
    def __init__(self, umbral_stock: int = 5):
        self.umbral_stock = umbral_stock  # Nivel mínimo de stock para alertar (RF-10)

    def verificar_stock(self, articulo_nombre: str, stock_actual: int) -> None:
        """Notifica si el stock está por debajo del umbral (RF-10)."""
        if stock_actual < self.umbral_stock:
            print(f"¡ALERTA! Stock bajo en {articulo_nombre}. Unidades restantes: {stock_actual}")
            # Aquí podrías agregar más acciones (email, logs, etc.)