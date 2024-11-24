# Clase base
class TransportePublico:
    def __init__(self, tipo, capacidad):
        self.tipo = tipo
        self.capacidad = capacidad

    def mostrar_info(self):
        print(f"Tipo: {self.tipo}, Capacidad: {self.capacidad} pasajeros")

class Autobus(TransportePublico):
    def __init__(self, tipo, capacidad, ruta):
        super().__init__(tipo, capacidad)
        self.ruta = ruta

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  Ruta: {self.ruta}")

class Tren(TransportePublico):
    def __init__(self, tipo, capacidad, numero_vagones):
        super().__init__(tipo, capacidad)
        self.numero_vagones = numero_vagones

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  Número de vagones: {self.numero_vagones}")

if __name__ == "__main__":
    autobus1 = Autobus("Autobús urbano", 50, "Ruta 5")
    autobus2 = Autobus("Autobús escolar", 30, "Colegio Santa María")

    tren1 = Tren("Tren interurbano", 300, 10)
    tren2 = Tren("Tren de alta velocidad", 500, 15)

    print("\nInformación de autobuses")
    autobus1.mostrar_info()
    autobus2.mostrar_info()

    print("\nInformación del Metro")
    tren1.mostrar_info()
    tren2.mostrar_info()
