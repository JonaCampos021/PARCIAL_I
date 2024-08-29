class Vehiculo:
    def __init__(self):
        #se solicita al usuario los datos del vehículo y los asigna a los atributos de la instancia
        self.tipo = input("Ingrese el tipo de vehículo (ej. Auto, Camioneta, Motocicleta): ")
        self.marca = input("Ingrese la marca del vehículo: ")
        self.modelo = input("Ingrese el modelo del vehículo: ")
        self.anio = input("Ingrese el año del vehículo: ")
        self.costo_renta = float(input("Ingrese el costo de renta por día: "))
        self.disponible = True 

    def __str__(self):
        #nosdevuelve una representación en cadena del vehículo
        return f"{self.tipo} {self.marca} {self.modelo} ({self.anio}) - ${self.costo_renta}/día"

class Cliente:
    def __init__(self):
        #solicitamos al usuario los datos del cliente y los asigna a los atributos de la instancia
        self.nombre = input("Ingrese el nombre del cliente: ")
        self.licencia = input("Ingrese el número de licencia del cliente: ")

    def __str__(self):
        #devuelve una representación en cadena del cliente
        return f"{self.nombre} (Licencia: {self.licencia})"

class Renta:
    def __init__(self, cliente, vehiculo):
        #se le asigna el cliente y el vehículo a los atributos de la instancia de Renta
        self.cliente = cliente
        self.vehiculo = vehiculo
        #se le solicita al usuario las fechas de inicio y fin de la renta
        self.fecha_inicio = input("Ingrese la fecha de inicio de la renta (YYYY-MM-DD): ")
        self.fecha_fin = input("Ingrese la fecha de fin de la renta (YYYY-MM-DD): ")

    def __str__(self):
        #nos devuelve una representación en cadena de la renta
        return f"Renta de {self.vehiculo} a {self.cliente} del {self.fecha_inicio} al {self.fecha_fin}"

class EmpresaRenta:
    def __init__(self):
        self.vehiculos = []
        self.rentas = []   

    def registrar_vehiculo(self):
        #hacemos un metodo para registrar un nuevo vehículo
        print("\nRegistrando un nuevo vehículo...")
        vehiculo = Vehiculo()  
        self.vehiculos.append(vehiculo)  
        print(f"Vehículo registrado: {vehiculo}")

    def rentar_vehiculo(self):
        #realizamos otro metodo para rentar un vehículo
        #y nos filtra una lista de los vehiculos que estan disponibles
        print("\nVehículos disponibles para rentar:")
        vehiculos_disponibles = [v for v in self.vehiculos if v.disponible]
        for idx, vehiculo in enumerate(vehiculos_disponibles):
            print(f"{idx + 1}. {vehiculo}")

        if not vehiculos_disponibles:
            #en el caso de que no hay vehículos disponibles, muestra un mensaje y retorna
            print("No hay vehículos disponibles para rentar.")
            return

        #solicita al usuario que seleccione un vehículo
        vehiculo_idx = int(input("Seleccione el vehículo a rentar: ")) - 1
        vehiculo = vehiculos_disponibles[vehiculo_idx]

        print("\nDatos del Cliente:")
        cliente = Cliente() 

        #creamos una nueva instancia de Renta con el cliente y el vehículo seleccionado
        renta = Renta(cliente, vehiculo)
        self.rentas.append(renta)  
        vehiculo.disponible = False 
        print(f"\nVehículo {vehiculo} rentado a {cliente}.")

    def mostrar_rentas(self):
        #creamos un metodo para mostrar todas las rentas activas
        print("\nListado de Rentas Activas:")
        for renta in self.rentas:
            print(renta)  


#creamos instancias 
empresa = EmpresaRenta()  
empresa.registrar_vehiculo()  
empresa.registrar_vehiculo()  
empresa.rentar_vehiculo()  
empresa.rentar_vehiculo()  
empresa.mostrar_rentas()
