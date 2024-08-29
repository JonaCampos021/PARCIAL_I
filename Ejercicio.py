class Consultorio: 
    def __init__(self, nombre, edad, genero):
        self.nombre_pa = nombre
        self.edad = edad
        self.genero = genero

    def datos(self):
        print(f"Nombre del paciente: {self.nombre_pa}")
        print(f"Edad del paciente: {self.edad}")
        print(f"Género del paciente: {self.genero}")


class Consultas(Consultorio):
    pacientes_atendidos = {}  # Diccionario para almacenar los pacientes atendidos

    def __init__(self):
        nombre = input("Ingrese el nombre del paciente: ")
        
        # Verificar si el paciente ya tiene una consulta previa
        if nombre in Consultas.pacientes_atendidos:
            print(f"El paciente {nombre} ya tiene una consulta previa. Se le pasará a la sala de espera.")
            return  # No tomamos más datos ni continuamos

        # Si no tiene consulta previa, se toman los datos
        edad = input("Ingrese la edad del paciente: ")
        genero = input("Ingrese el género del paciente: ")
        super().__init__(nombre, edad, genero)

        self.motivo = input("Ingrese el motivo de la consulta: ")
        self.fecha = input("Ingresar la fecha de la consulta(DD-MM-YY): ")
        
        # Almacenar al paciente en el diccionario de pacientes atendidos
        Consultas.pacientes_atendidos[nombre] = self

    def secretaria(self):
        if self.nombre_pa not in Consultas.pacientes_atendidos:
            return  # Si el paciente está en sala de espera, no mostramos datos

        print("-----------")
        print("Datos de la consulta: ")
        super().datos()
        print(f"Motivo de la consulta: {self.motivo}")
        print(f"Fecha de la consulta: {self.fecha}")
        print("-----------")


# Ejemplo de uso
consu1 = Consultas()
if hasattr(consu1, 'nombre_pa'):  # Verificar si el paciente no fue enviado a la sala de espera
    consu1.secretaria()

consu2 = Consultas()  # Intentar registrar al mismo paciente nuevamente
if hasattr(consu2, 'nombre_pa'):  # Verificar si el paciente no fue enviado a la sala de espera
    consu2.secretaria()
