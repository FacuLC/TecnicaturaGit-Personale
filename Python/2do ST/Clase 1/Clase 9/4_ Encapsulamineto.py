class Encapsulamineto:
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # Se lo llama metodo Init Dunder
        self.__nombre = nombre # Esta encapsulado totalmente
        self.apellido = apellido
        self._dni = dni # Esta Articulo esta esncapsulado de una manera suguerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):
        print(f'La clase InitDunder tiene los siguientes Datos -> {self.__nombre} {self.apellido} {self._dni} {self.edad}\nLa direccion es: {self.args}\nDatos importantes son: {self.kwargs}')

persona1 = Encapsulamineto('Facundo', 'Cano', 632478368, 21, 'Telefono', '2974603992', 'Barrio Guemes', 214, 'Solar', 26, Altura = 1.78, Peso = 75, ColorFavorito = 'Gris', Auto = 'TOYOTA', Modelo = '2013')
persona1.mostrar_detalle()

# print(persona1._dni) # Esto no se debe utilizar (esta encapsulado), esto dice que lo desconocemos python

# persona1.__nombre # Esta Totalmente encapsulado