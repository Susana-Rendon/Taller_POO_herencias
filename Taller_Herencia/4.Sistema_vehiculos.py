class VehiculoCarreras:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")
        print(f"  Velocidad máxima: {self.velocidad_maxima} km/h")

class CocheF1(VehiculoCarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_neumaticos):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_neumaticos = tipo_neumaticos

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  Tipo de neumáticos: {self.tipo_neumaticos}")

class MotoGP(VehiculoCarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_carenado):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_carenado = tipo_carenado

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  Tipo de carenado: {self.tipo_carenado}")

if __name__ == "__main__":
    coche1 = CocheF1("Ferrari", "SF21", 360, "Lluvia")
    coche2 = CocheF1("Mercedes", "W12", 350, "Medios")
    coche3 = CocheF1("Red Bull", "RB16B", 355, "Blandos")

    moto1 = MotoGP("Yamaha", 2020, 300, "Integral")
    moto2 = MotoGP("Ducati", 2021, 310, "Deportivo")
    moto3 = MotoGP("Honda", 2015, 305, "Minimalista")

    print("\nInformación de los coches de F1")
    coche1.mostrar_info()
    coche2.mostrar_info()
    coche3.mostrar_info()

    print("\nInformación de las motos de MotoGP")
    moto1.mostrar_info()
    moto2.mostrar_info()
    moto3.mostrar_info()
