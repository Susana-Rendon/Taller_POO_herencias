class Mascota:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def mostrar_info(self):
        print(f"La mascota de nombre {self.nombre} tiene {self.edad} años de edad y pertenece a la especie de {self.especie}")

class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, "Perro")
        self.raza = raza

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  Raza: {self.raza}")

    def ladrar(self):
        print("Guau, guau")

class Gato(Mascota):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad, "Gato")
        self.color = color

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  Color: {self.color}")

    def maullar(self):
        print("Miau")

if __name__ == "__main__":
    perro1 = Perro("Max", 5, "Labrador")
    perro2 = Perro("Bella", 3, "Golden Retriever")
    perro3 = Perro("Rocky", 2, "Bulldog")

    gato1 = Gato("Luna", 4, "Negro")
    gato2 = Gato("Simba", 6, "Blanco")
    gato3 = Gato("Mimi", 1, "Gris")

    print("\nInformación de los perros")
    perro1.mostrar_info()
    perro1.ladrar()
    perro2.mostrar_info()
    perro2.ladrar()
    perro3.mostrar_info()
    perro3.ladrar()

    print("\nInformación de los gatos")
    gato1.mostrar_info()
    gato1.maullar()
    gato2.mostrar_info()
    gato2.maullar()
    gato3.mostrar_info()
    gato3.maullar()
