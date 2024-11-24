class MaterialBiblioteca:
    def __init__(self, titulo, autor, codigo, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El material {self.titulo} ha sido prestado.")
        else:
            print(f"El material {self.titulo} no está disponible.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El material {self.titulo} ha sido devuelto.")
        else:
            print(f"El material {self.titulo} ya está disponible.")

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"Código: {self.codigo}, Título: '{self.titulo}', Autor: {self.autor}, Estado: {estado}")

class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numero_paginas, genero, disponible=True):
        super().__init__(titulo, autor, codigo, disponible)
        self.numero_paginas = numero_paginas
        self.genero = genero

    def mostrar_info(self):
        super().mostrar_info()
        print(f"El libro: {self.titulo} tiene {self.numero_paginas} páginas y ede del género: {self.genero}")

class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numero_edicion, fecha_publicacion, disponible=True):
        super().__init__(titulo, autor, codigo, disponible)
        self.numero_edicion = numero_edicion
        self.fecha_publicacion = fecha_publicacion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"La revista {self.titulo} con edición: {self.numero_edicion} tiene una fecha de publicación: {self.fecha_publicacion}")


if __name__ == "__main__":

    libro1 = Libro("El Quijote", "Miguel de Cervantes", "L001", 800, "Clásico")
    libro2 = Libro("1984", "George Orwell", "L002", 328, "Distopía")
    libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", "L003", 500, "Realismo mágico")

    revista1 = Revista("National Geographic", "Varios", "R001", "Edición Especial", "Noviembre 2024")
    revista2 = Revista("Semana", "Varios", "R002", "No. 45", "Octubre 2024")
    revista3 = Revista("TIME", "Varios", "R003", "Vol. 89", "Septiembre 2024")

    print("\nInformación de los libros")
    libro1.mostrar_info()
    libro2.mostrar_info()
    libro3.mostrar_info()

    print("\nInformación de las revistas")
    revista1.mostrar_info()
    revista2.mostrar_info()
    revista3.mostrar_info()

    print("\nOperaciones de préstamo y devolución")
    libro1.prestar()
    libro1.prestar()
    libro1.devolver()
    libro1.devolver()

    revista2.prestar()
    revista2.devolver()
