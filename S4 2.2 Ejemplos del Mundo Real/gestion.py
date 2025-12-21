class Restaurante:
    """
    Administra las mesas y gestiona las reservas.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.mesas = [] # Inventario de mesas

    def agregar_mesa(self, mesa):
        """Añade una mesa a la lista del restaurante."""
        self.mesas.append(mesa)

    def mostrar_disponibilidad(self):
        print(f"\n--- Estado del Restaurante '{self.nombre}' ---")
        for mesa in self.mesas:
            print(mesa)
        print("---------------------------------------------\n")

    def registrar_reserva(self, cliente, numero_mesa):
        """
        Intenta reservar una mesa específica para un cliente.
        """
        mesa_encontrada = None
        
        # Buscamos la mesa por su número
        for m in self.mesas:
            if m.numero == numero_mesa:
                mesa_encontrada = m
                break
        
        if mesa_encontrada:
            print(f"Hola {cliente.nombre}, verificando mesa {numero_mesa}...")
            
            if mesa_encontrada.ocupar():
                print(f" Reserva exitosa. Te reservamos la mesa {numero_mesa}.")
            else:
                print(f" Lo sentimos, mesa {numero_mesa} ya reservada.")
        else:
            print(f" Error - Mesa número {numero_mesa} no existe.")
