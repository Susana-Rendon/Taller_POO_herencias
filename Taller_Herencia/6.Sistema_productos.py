class ProductoElectronico:
    def __init__(self, nombre, precio, marca):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Marca: {self.marca}")

class TelefonoMovil(ProductoElectronico):
    def __init__(self, nombre, precio, marca, capacidad_bateria):
        super().__init__(nombre, precio, marca)
        self.capacidad_bateria = capacidad_bateria

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  Capacidad de batería: {self.capacidad_bateria} mAh")

class Laptop(ProductoElectronico):
    def __init__(self, nombre, precio, marca, tamano_pantalla):
        super().__init__(nombre, precio, marca)
        self.tamano_pantalla = tamano_pantalla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  Tamaño de pantalla: {self.tamano_pantalla} pulgadas")

if __name__ == "__main__":
    movil1 = TelefonoMovil("iPhone 14", 6000000, "Apple", 3095)
    movil2 = TelefonoMovil("Galaxy S23", 5000000, "Samsung", 3900)

    laptop1 = Laptop("MacBook", 2400000, "Apple", 16)
    laptop2 = Laptop("Laptop", 1200000, "Dell", 13.3)

    print("\nInformación de teléfonos móviles")
    movil1.mostrar_info()
    movil2.mostrar_info()

    print("\n--- Información de laptops ---")
    laptop1.mostrar_info()
    laptop2.mostrar_info()
