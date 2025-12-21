from typing import List, Tuple

def solicitar_gastos() -> List[float]:
    """
    Solicita al usuario los gastos realizados durante la semana de forma interactiva.
    
    Esta función itera sobre los días de la semana y valida que cada entrada
    sea un número positivo.

    Returns:
        List[float]: Una lista que contiene los montos de los gastos validados.
    """
    lista_gastos: List[float] = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    print("--- Registro de Gastos Semanales ---")
    
    # Iteramos sobre cada día para asegurar un registro completo
    for dia in dias_semana:
        while True:
            try:
                entrada = input(f"Ingrese el gasto del {dia}: $")
                monto = float(entrada)
                
                # Validación de lógica de negocio: no existen gastos negativos
                if monto < 0:
                    print("Error: El gasto no puede ser negativo.")
                else:
                    lista_gastos.append(monto)
                    break # Salimos del ciclo while si el dato es correcto
            except ValueError:
                # Capturamos el error si el usuario introduce texto en lugar de números
                print("Error: Por favor, ingrese un valor numérico válido.")
    
    return lista_gastos

def calcular_estadisticas(gastos: List[float]) -> Tuple[float, float]:
    """
    Calcula el total y el promedio de una lista de gastos.

    Args:
        gastos (List[float]): Lista de valores numéricos representando dinero.

    Returns:
        Tuple[float, float]: Una tupla conteniendo (total_semanal, promedio_diario).
    """
    # Validación para evitar división por cero si la lista está vacía
    if not gastos:
        return 0.0, 0.0
    
    total = sum(gastos)
    promedio = total / len(gastos)
    
    return total, promedio

def main():
    """
    Función principal que orquesta el flujo del programa estructurado.
    """
    # 1. Entrada de datos
    gastos_registrados = solicitar_gastos()
    
    # 2. Procesamiento de datos
    total_semana, promedio_diario = calcular_estadisticas(gastos_registrados)
    
    # 3. Presentación de resultados
    print("\n" + "="*30)
    print("RESUMEN FINANCIERO SEMANAL")
    print("="*30)
    print(f"Gastos procesados : {len(gastos_registrados)} días")
    print(f"Gasto Total       : ${total_semana:.2f}")
    print(f"Promedio Diario   : ${promedio_diario:.2f}")
    print("="*30)

if __name__ == "__main__":
    main()