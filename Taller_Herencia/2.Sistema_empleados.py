class EmpleadoHospital:
    def __init__(self, nombre, id, departamento, salario_base):
        self.nombre = nombre
        self.id = id
        self.departamento = departamento
        self.salario_base = salario_base

    def mostrar_info(self):
        print(f"ID: {self.id}, Nombre: {self.nombre}")
        print(f"Departamento: {self.departamento}, Salario base: {self.salario_base} pesos")

class Medico(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, especialidad, num_pacientes):
        super().__init__(nombre, id, departamento, salario_base)
        self.especialidad = especialidad
        self.num_pacientes = num_pacientes

    def mostrar_info(self):
        super().mostrar_info()
        print(f"El medico {self.nombre} con especialidad: {self.especialidad}, tiene un número de pacientes atendidos: {self.num_pacientes}")

class Enfermero(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, turno, planta):
        super().__init__(nombre, id, departamento, salario_base)
        self.turno = turno
        self.planta = planta

    def mostrar_info(self):
        super().mostrar_info()
        print(f"El enfermero {self.nombre} tiene el turno de la {self.turno} y pertenece a la planta: {self.planta}")


if __name__ == "__main__":
    medico1 = Medico("Dr. Juan Pérez", "M001", "Cardiología", 4500000, "Cardiología", 120)
    medico2 = Medico("Dra. Ana López", "M002", "Pediatría", 4300000, "Pediatría", 85)
    medico3 = Medico("Dr. Luis Gómez", "M003", "Urgencias", 4700000, "Traumatología", 150)

    enfermero1 = Enfermero("Pedro Fernández", "E001", "Pediatría", 3000000, "Mañana", 3)
    enfermero2 = Enfermero("Lucía Martínez", "E002", "Urgencias", 3200000, "Noche", 1)
    enfermero3 = Enfermero("Laura Sánchez", "E003", "Quirófano", 3100000, "Mañana", 2)

    print("\nInformación de los médicos")
    medico1.mostrar_info()
    medico2.mostrar_info()
    medico3.mostrar_info()

    print("\nInformación de los enfermeros")
    enfermero1.mostrar_info()
    enfermero2.mostrar_info()
    enfermero3.mostrar_info()
