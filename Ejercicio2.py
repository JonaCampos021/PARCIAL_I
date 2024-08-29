class Libro:
    def __init__(self):
        #solicitamos al usuario los datos del libro y los asigna a los atributos de la instancia
        self.titulo = input("Ingrese el título del libro: ")
        self.autor = input("Ingrese el autor del libro: ")
        self.disponible = True  # Indica si el libro está disponible para prestar

    def __str__(self):
        #devuelve una representación en cadena del libro
        return f"'{self.titulo}' de {self.autor}"


class Usuario:
    def __init__(self):
        #solicitamos al usuario los datos del usuario y los asigna a los atributos de la instancia
        self.nombre = input("Ingrese el nombre del usuario: ")
        self.tarjeta_id = input("Ingrese el ID de la tarjeta del usuario: ")

    def __str__(self):
        return f"{self.nombre} (ID: {self.tarjeta_id})"


class Prestamo:
    def __init__(self, usuario, libro):
        #se le asigna el usuario y el libro a los atributos de la instancia de Préstamo
        self.usuario = usuario
        self.libro = libro
        #se le solicita al usuario las fechas de préstamo y devolución
        self.fecha_prestamo = input("Ingrese la fecha de préstamo (YYYY-MM-DD): ")
        self.fecha_devolucion = input("Ingrese la fecha de devolución (YYYY-MM-DD): ")

    def __str__(self):
        #nos devuelve una representación en cadena del préstamo
        return f"Préstamo de {self.libro} a {self.usuario} el {self.fecha_prestamo}"


class Biblioteca:
    def __init__(self):
        self.prestamos = [] 

    def prestar_libro(self):
        #creamos un metodo para prestar un libro
        print("\nDatos del Libro:")
        libro = Libro()  
        print("\nDatos del Usuario:")
        usuario = Usuario() 

        if libro.disponible:
            #en el caso que el libro está disponible, se crea un préstamo y si no mostrara un mensaje
            prestamo = Prestamo(usuario, libro)
            self.prestamos.append(prestamo)  
            libro.disponible = False  
            print(f"\nLibro '{libro.titulo}' prestado a {usuario.nombre} hasta el {prestamo.fecha_devolucion}.")
        else:
            print(f"Lo sentimos, el libro '{libro.titulo}' no está disponible.")

    def mostrar_prestamos(self):
        #creamos un metodo para mostrar todos los préstamos activos
        print("\nListado de Préstamos:")
        for prestamo in self.prestamos:
            print(prestamo)

#creamos una instancias
biblioteca = Biblioteca() 
biblioteca.prestar_libro()  
biblioteca.prestar_libro()
biblioteca.mostrar_prestamos()