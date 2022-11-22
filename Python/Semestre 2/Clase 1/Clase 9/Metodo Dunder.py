class InitDunder:
    def __init__(self, nombre, apellido, edad, *args, **kwargs): # Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido =apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):
        print(f'La clase InitDunder tiene los siguientes Datos -> {self.nombre} {self.apellido} {self.edad}\nLa direccion es: {self.args}\nDatos importantes son: {self.kwargs}')

persona1 = InitDunder('Facundo', 'Cano', 21, 'Telefono', '2974603992', 'Barrio Guemes', 214, 'Solar', 26, Altura = 1.78, Peso = 75, ColorFavorito = 'Gris', Auto = 'TOYOTA', Modelo = '2013')

persona1.mostrar_detalle()
