# ABSTRACCIÓN
# Definimos la esencia de un "Libro" 
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn  # ISBN único para cada libro
        self.__disponible = True  # Encapsulado: solo modificable internamente
    
    def mostrar_info(self):
        return f"'{self.titulo}' por {self.autor}"
    
    def esta_disponible(self):
        return self.__disponible
    
    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False
    
    def devolver(self):
        self.__disponible = True


# ENCAPSULAMIENTO
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.__libros_prestados = []  # Atributo privado
    
    def get_libros_prestados(self):  # Para acceder de forma controlada
        return self.__libros_prestados.copy()
    
    def tomar_prestado(self, libro):
        if libro.esta_disponible():
            libro.prestar()
            self.__libros_prestados.append(libro)
            return True
        return False
    
    def devolver_libro(self, libro):
        if libro in self.__libros_prestados:
            libro.devolver()
            self.__libros_prestados.remove(libro)
            return True
        return False


# HERENCIA
# Libros especializados heredan de Libro
class LibroTexto(Libro):
    def __init__(self, titulo, autor, isbn, materia, nivel):
        super().__init__(titulo, autor, isbn)
        self.materia = materia
        self.nivel = nivel  # "Escuela", "Colegio", "Universidad"
    
    # Sobrescribimos el método (Polimorfismo)
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base} - {self.materia} ({self.nivel})"


class Novela(Libro):
    def __init__(self, titulo, autor, isbn, genero, paginas):
        super().__init__(titulo, autor, isbn)
        self.genero = genero  # "Romance", "Misterio", "Ciencia Ficción"
        self.paginas = paginas
    
    # Sobrescribimos de forma diferente (Polimorfismo)
    def mostrar_info(self):
        return f"Novela: '{self.titulo}' ({self.genero}, {self.paginas} páginas)"


# POLIMORFISMO
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []
    
    def agregar_libro(self, libro):
        self.catalogo.append(libro)
    
    def mostrar_catalogo(self):
        print(f"\n=== CATÁLOGO: {self.nombre} ===")
        for libro in self.catalogo:
            print(f"- {libro.mostrar_info()}")  # Llamada polimórfica
    
    def buscar_por_titulo(self, titulo):
        for libro in self.catalogo:
            if titulo.lower() in libro.titulo.lower():
                return libro
        return None
    
    def libros_disponibles(self):
        disponibles = []
        for libro in self.catalogo:
            if libro.esta_disponible():
                disponibles.append(libro)
        return disponibles


# --DEMOSTRACIÓN--
def main():
    print("=== SISTEMA DE BIBLIOTECA ===")
    
    # 1. Crear biblioteca
    mi_biblioteca = Biblioteca("Biblioteca Central")
    
    # 2. Crear libros de diferentes tipos (Abstracción)
    libro1 = LibroTexto("Matemáticas Básicas", "Carlos Ruiz", "123-456", "Matemáticas", "Colegio")
    libro2 = Novela("Cien Años de Soledad", "Gabriel García Márquez", "789-012", "Realismo Mágico", 417)
    libro3 = Libro("Python para Todos", "Ana López", "345-678")
    libro4 = Novela("El Principito", "Antoine de Saint-Exupéry", "901-234", "Fábula", 96)
    
    # 3. Agregar libros a la biblioteca
    mi_biblioteca.agregar_libro(libro1)
    mi_biblioteca.agregar_libro(libro2)
    mi_biblioteca.agregar_libro(libro3)
    mi_biblioteca.agregar_libro(libro4)
    
    # 4. Mostrar catálogo completo
    mi_biblioteca.mostrar_catalogo()
    
    # 5. Crear usuarios
    print("\n= USUARIOS =")
    usuario1 = Usuario("Alexander Rosado", "U001")
    usuario2 = Usuario("Jose Sanchez", "U002")
    
    # 6. Demostrar Encapsulamiento y funcionalidad
    print(f"\n{usuario1.nombre} quiere tomar prestado 'Cien Años de Soledad'")
    
    libro_buscado = mi_biblioteca.buscar_por_titulo("Cien Años")
    if libro_buscado:
        if usuario1.tomar_prestado(libro_buscado):
            print(f"✓ {usuario1.nombre} tomó prestado: {libro_buscado.mostrar_info()}")
        else:
            print("✗ El libro no está disponible")
    
    print(f"\nLibros prestados a {usuario1.nombre}:")
    for libro in usuario1.get_libros_prestados():  # Usando getter
        print(f"- {libro.mostrar_info()}")
    
    # 7. Demostrar Polimorfismo con diferentes tipos de libros
    print("\n=== INFORMACIÓN DE LIBROS (POLIMORFISMO) ===")
    libros = [libro1, libro2, libro3, libro4]
    for libro in libros:
        print(f"> {libro.mostrar_info()}")  # Cada tipo muestra info diferente
        print(f"  Disponible: {'Sí' if libro.esta_disponible() else 'No'}")
    
    # 8. Demostrar que no podemos acceder directamente a atributos privados
    print("\n= DEMOSTRACIÓN ENCAPSULAMIENTO =")
    print(f"¿Podemos ver libros prestados directamente? usuario1.__libros_prestados")
    print("No, porque está encapsulado. Debemos usar el getter: usuario1.get_libros_prestados()")
    
    # 9. Devolver libro
    print(f"\n{usuario1.nombre} devuelve el libro")
    if usuario1.devolver_libro(libro_buscado):
        print("✓ Libro devuelto exitosamente")
    
    print(f"\nLibros disponibles ahora: {len(mi_biblioteca.libros_disponibles())}")


if __name__ == "__main__":
    main()