import math

class Figura3D:
    def calcular_volumen(self):
        print("Método no implementado. Por favor, use una clase derivada.")

class Cubo(Figura3D):
    def __init__(self, lado):
        self.lado = lado

    def calcular_volumen(self):
        volumen = self.lado ** 3
        return volumen

class Esfera(Figura3D):
    def __init__(self, radio):
        self.radio = radio

    def calcular_volumen(self):
        volumen = (4 / 3) * math.pi * (self.radio ** 3)
        return volumen

if __name__ == "__main__":
    cubo1 = Cubo(3)
    cubo2 = Cubo(5)
    esfera1 = Esfera(2)
    esfera2 = Esfera(7)

    print("Volúmenes de las figuras 3D")
    print(f"Cubo con lado {cubo1.lado}: Volumen = {cubo1.calcular_volumen()} unidades cúbicas")
    print(f"Cubo con lado {cubo2.lado}: Volumen = {cubo2.calcular_volumen()} unidades cúbicas")
    print(f"Esfera con radio {esfera1.radio}: Volumen = {esfera1.calcular_volumen():.2f} unidades cúbicas")
    print(f"Esfera con radio {esfera2.radio}: Volumen = {esfera2.calcular_volumen():.2f} unidades cúbicas")
