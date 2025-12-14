# Comparación de Billetera inteligente en Python

## Descripción del Proyecto
Este proyecto tiene como objetivo demostrar las diferencias fundamentales, ventajas y estructura lógica entre la **Programación Tradicional (Estructurada)** y la **Programación Orientada a Objetos (POO)**.

Para ello, se han implementado dos soluciones para un mismo problema de negocio: **Un Sistema de Registro y Análisis de Gastos Personales**.

---

## Estructura del Repositorio

1. **`S3-2.1.1 Billetera inteligente - Programacion tradicional.py`**: Solución utilizando funciones secuenciales y estructuras lógicas simples.
2. **`S3-2.1.2 Billetera inteligente -POO.py`**: Solución utilizando Clases, Objetos y los 4 pilares de la POO.

---

## Análisis Técnico del Código

### 1. Enfoque Tradicional (`Billetera inteligente - Programacion tradicional.py`)
Este script se centra en el flujo de ejecución paso a paso y la manipulación directa de datos a través de funciones.

* **Bloque de Entrada (`solicitar_gastos`):**
    * Utiliza un ciclo `for` iterando sobre una lista predefinida de días.
    * Implementa un bucle `while True` anidado con bloques `try-except` para garantizar que el usuario ingrese únicamente valores numéricos válidos.
    * Valida la lógica de negocio (no gastos negativos) antes de agregar datos a la lista.
    * **Propósito:** Retornar una lista "limpia" de datos crudos (`List[float]`).

* **Bloque de Proceso (`calcular_estadisticas`):**
    * Función pura que recibe datos y retorna resultados.
    * Maneja casos borde, como listas vacías, para evitar errores de división por cero (`ZeroDivisionError`).
    * **Propósito:** Separar la lógica matemática de la entrada de datos.

* **Bloque Principal (`main`):**
    * Orquesta el llamado de funciones de manera secuencial: `Entrada -> Proceso -> Salida`.

### 2. Enfoque Orientado a Objetos (`Billetera inteligente - POO.py`)
Este script modela el problema basándose en entidades ("Billetera") que poseen sus propios datos y comportamientos.

* **Clase `BilleteraBase`:**
    * Actúa como el componente de almacenamiento seguro.
    * Utiliza un **Constructor (`__init__`)** para inicializar la lista de transacciones cada vez que se crea un objeto.
    * Protege los datos usando atributos privados.

* **Clase `ReporteFinanciero`:**
    * Extiende la funcionalidad base.
    * Contiene la lógica para transformar datos crudos en información útil (métricas y reportes visuales).

---

## Aplicación de los Pilares de la POO

A continuación se detalla explícitamente qué líneas de código en `billetera_inteligente_poo.py` corresponden a cada pilar:

### 1. Abstracción
**Concepto:** Ocultar la complejidad interna y exponer solo lo necesario.
**En el código:**
El usuario interactúa con métodos claros como `registrar_transaccion()` o `generar_reporte()`, sin necesidad de entender cómo se gestionan internamente las listas o los cálculos matemáticos.

### 2. Encapsulamiento
**Concepto:** Proteger los datos sensibles de modificaciones no autorizadas.
**En el código:**
* **Línea:** `self.__transacciones: List[float] = []`
* **Explicación:** El uso del doble guion bajo (`__`) hace que este atributo sea **privado**. No se puede acceder a él directamente desde fuera de la clase (ej. `objeto.__transacciones` daría error). El acceso solo es posible mediante métodos controlados como `registrar_transaccion`.

### 3. Herencia
**Concepto:** Reutilización de código permitiendo que una clase derive de otra.
**En el código:**
* **Línea:** `class ReporteFinanciero(BilleteraBase):`
* **Explicación:** La clase `ReporteFinanciero` (Hija) hereda automáticamente el constructor y los métodos de almacenamiento de `BilleteraBase` (Padre). Esto evita duplicar el código de validación y almacenamiento.

### 4. Polimorfismo
**Concepto:** Capacidad de presentar una interfaz única para diferentes formas subyacentes.
**En el código:**
* **Método:** `generar_reporte(self)`
* **Explicación:** Este método toma los datos heredados y define una forma específica de presentarlos para esta clase. En un sistema más grande, podríamos tener otra clase (ej. `ReporteFiscal`) que use los mismos datos pero tenga su propio método de reporte con formato diferente.

---

## Instrucciones de Ejecución

1. **Para ejecutar la versión tradicional:**
   ```bash
   Billetera inteligente - Programacion tradicional.py
````

2.  **Para ejecutar la versión POO:**
    ```bash
    Billetera inteligente - POO.py
    ```

-----

**Autor:** Segundo Rosado/Segalexrm
**Asignatura: Programación Orientada a Objetos

```
```
