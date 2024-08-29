
class Hotel:
    def __init__(self):
        # Inicializa las opciones de habitaciones y servicios extra con sus respectivos precios.
        self.habitaciones = {
            1: {'tipo': 'Estándar', 'precio_por_noche': 100},
            2: {'tipo': 'Superior', 'precio_por_noche': 150},
            3: {'tipo': 'Suite', 'precio_por_noche': 250}
        }
        self.servicios_extra = {
            1: {'nombre': 'Uso de la piscina', 'precio': 20},
            2: {'nombre': 'Uso de la cancha de golf', 'precio': 50}
        }

    def mostrar_opciones(self):
        # Muestra las opciones de habitaciones y servicios extra.
        print("Opciones de habitaciones disponibles:")
        for key, value in self.habitaciones.items():
            print(f"{key}. Habitación {value['tipo']} - ${value['precio_por_noche']} por noche")
        print("\nServicios extra disponibles:")
        for key, value in self.servicios_extra.items():
            print(f"{key}. {value['nombre']} - ${value['precio']} por noche")

    def obtener_precio(self, tipo, opcion):
        # Devuelve el precio basado en el tipo (habitacion o servicio) y la opción seleccionada.
        if tipo == 'habitacion':
            return self.habitaciones.get(opcion, {}).get('precio_por_noche', 0)
        elif tipo == 'servicio':
            return self.servicios_extra.get(opcion, {}).get('precio', 0)
        return 0

    def generar_factura(self, habitacion, noches, servicios_extra):
        # Calcula el costo total de la reserva, incluyendo los servicios extra.
        precio_habitacion = self.obtener_precio('habitacion', habitacion)
        total_habitacion = precio_habitacion * noches
        total_servicios = sum(self.obtener_precio('servicio', s) for s in servicios_extra)
        total = total_habitacion + total_servicios

        # Genera una cadena con la factura detallada.
        factura = (f"\nFactura detallada:\n"
                   f"Tipo de habitación: {self.habitaciones[habitacion]['tipo']}\n"
                   f"Precio por noche: ${precio_habitacion}\n"
                   f"Número de noches: {noches}\n"
                   f"Servicios extra:\n")
        for s in servicios_extra:
            factura += f"  {self.servicios_extra[s]['nombre']}: ${self.obtener_precio('servicio', s)}\n"
        factura += f"Total a pagar: ${total}\n"

        return factura

def main():
    # Crea una instancia del objeto Hotel.
    hotel = Hotel()
    
    # Muestra las opciones de habitaciones y servicios extra y permite al usuario hacer una selección.
    hotel.mostrar_opciones()
    
    # Selección de habitación
    opcion_habitacion = int(input("Seleccione el tipo de habitación (1, 2, 3): "))
    precio_habitacion = hotel.obtener_precio('habitacion', opcion_habitacion)
    
    if precio_habitacion == 0:
        print("Opción de habitación inválida.")
        return
    
    # Número de noches de estancia
    noches = int(input("Ingrese el número de noches que permanecerá: "))
    
    # Selección de servicios extra
    servicios_extra = []
    while True:
        opcion_servicio = int(input("Seleccione un servicio extra (0 para terminar): "))
        if opcion_servicio == 0:
            break
        if opcion_servicio in hotel.servicios_extra:
            servicios_extra.append(opcion_servicio)
        else:
            print("Opción de servicio inválida.")
    
    # Genera y muestra la factura final con los detalles de la reserva.
    factura = hotel.generar_factura(opcion_habitacion, noches, servicios_extra)
    print(factura)

if __name__ == "__main__":
    main()
