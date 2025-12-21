from entidades import Mesa, Cliente
from gestion import Restaurante

def iniciar_app():
    print("--- Sistema de Reservas SARM Grill ---")

    # 1. Creamos el restaurante
    mi_restaurante = Restaurante("SARM Grill")

    # 2. Configuramos las mesas (Número, Capacidad)
    # Mesa 1 para parejas, Mesa 5 familiar, etc.
    mi_restaurante.agregar_mesa(Mesa(1, 2)) 
    mi_restaurante.agregar_mesa(Mesa(2, 2))
    mi_restaurante.agregar_mesa(Mesa(5, 6))

    # 3. Mostrar mesas libres
    mi_restaurante.mostrar_disponibilidad()

    # 4. Llega un cliente
    cliente1 = Cliente("Alejandro Martinez", "0991234567")

    # 5. El cliente reserva la mesa 5 (la familiar)
    mi_restaurante.registrar_reserva(cliente1, 5)

    # 6. Intento de doble reserva (para probar la lógica)
    cliente2 = Cliente("Elsa Gutierrez", "0987654321")
    mi_restaurante.registrar_reserva(cliente2, 5)

    # 7. Mostrar estado final
    mi_restaurante.mostrar_disponibilidad()

if __name__ == "__main__":
    iniciar_app()
