from typing import List, Tuple, Union

class BilleteraBase:
    """
    Clase base que gestiona el almacenamiento seguro de transacciones financieras.
    
    Esta clase implementa el pilar de ENCAPSULAMIENTO protegiendo la lista
    de transacciones para evitar modificaciones directas no autorizadas.
    """
    
    def __init__(self):
        """Inicializa la billetera con una lista de transacciones vacía y privada."""
        # Atributo privado (__) para encapsulamiento
        self.__transacciones: List[float] = []

    def registrar_transaccion(self, monto: Union[int, float]) -> bool:
        """
        Agrega una transacción al registro si cumple con las validaciones.

        Args:
            monto (Union[int, float]): El valor monetario a registrar.

        Returns:
            bool: True si el registro fue exitoso, False en caso contrario.
        """
        if isinstance(monto, (int, float)) and monto >= 0:
            self.__transacciones.append(float(monto))
            return True
        else:
            print("Error: Monto inválido o negativo.")
            return False

    def _obtener_datos_protegidos(self) -> List[float]:
        """
        Getter protegido para permitir acceso de lectura a las clases hijas.
        
        Returns:
            List[float]: Copia de la lista de transacciones.
        """
        return self.__transacciones


class ReporteFinanciero(BilleteraBase):
    """
    Clase derivada que extiende la funcionalidad de BilleteraBase.
    
    Esta clase implementa el pilar de HERENCIA para reutilizar la lógica de
    almacenamiento y añade capacidades de análisis y reporte.
    """
    
    def calcular_metricas(self) -> Tuple[float, float]:
        """
        Realiza cálculos estadísticos sobre las transacciones almacenadas.

        Returns:
            Tuple[float, float]: (Total acumulado, Promedio por transacción).
        """
        # Accedemos a los datos a través del método protegido de la clase padre
        datos = self._obtener_datos_protegidos()
        
        if not datos:
            return 0.0, 0.0
        
        total = sum(datos)
        promedio = total / len(datos)
        return total, promedio

    def generar_reporte(self):
        """
        Muestra un reporte detallado en consola.
        
        Este método representa una forma de POLIMORFISMO, presentando los datos
        de una manera específica para esta clase de reporte.
        """
        total, promedio = self.calcular_metricas()
        cantidad = len(self._obtener_datos_protegidos())
        
        print("\n" + "*"*40)
        print(" SISTEMA DE GESTIÓN FINANCIERA (POO)")
        print("*"*40)
        print(f"| Transacciones : {cantidad}")
        print(f"| Saldo Total   : ${total:,.2f}")
        print(f"| Promedio      : ${promedio:,.2f}")
        print("*"*40)


if __name__ == "__main__":
    print("--- Inicializando Billetera Virtual ---")
    
    # Instanciamos la clase hija (que contiene la lógica de base + reporte)
    mi_billetera = ReporteFinanciero()
    
    # Simulación de interacción con el usuario
    try:
        num_movimientos = int(input("Ingrese cantidad de movimientos a registrar: "))
        
        for i in range(num_movimientos):
            while True:
                try:
                    entrada = float(input(f"  > Movimiento {i+1}: $"))
                    # Delegamos la validación al método de la clase
                    if mi_billetera.registrar_transaccion(entrada):
                        break
                except ValueError:
                    print("    [!] Error: Ingrese solo números.")
        
        # Generación del reporte final
        mi_billetera.generar_reporte()
        
    except ValueError:
        print("Error crítico en la entrada de datos inicial.")