class Mesa:
    """
    Representa una mesa en el restaurante.
    Tiene número, capacidad de personas y estado.
    """
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.esta_reservada = False

    def ocupar(self):
        """Cambia el estado de la mesa a reservada."""
        if not self.esta_reservada:
            self.esta_reservada = True
            return True
        return False

    def liberar(self):
        """Libera la mesa."""
        self.esta_reservada = False

    def __str__(self):
        estado = "Reservada" if self.esta_reservada else "Libre"
        return f"[Mesa {self.numero}] - Capacidad: {self.capacidad} pers. - {estado}"


class Cliente:
    """
    Representa a la persona que hace la reserva.
    """
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} (Telf: {self.telefono})"
