class Vehiculo:
    """
    Crear una clase Padre (Vehiculo) y dos Clases hijas: (Auto y Bicicleta) y deben heredar lo de la clase Padre (Vehiculo)

    La Clase Padre debe tener los siguienetes Atributos y metodos:
    (Vehiculo)
    -Atributos: (color, ruedas)
    -Metodos: (__init__(color, ruedas) y __str__())

    (Auto) - (Clase hija de Vehiculo)
    -Atributos: (Velocidad (Km/hs))
    Metodos: (__init__(color, ruedas, velocidad) y __str__())

    (Bicicleta)
    -Atributos: (tipo(urbana/montaña/etc.))
    -Metodos: (__init__(color, ruedas, tipo) y __str__())
    """

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Clase Vehiculo: [Color del Vehiculo: {self.color}, Ruedas del Vehiculo: {str(self.ruedas)}]'


class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ', Velocidad del Vehiculo(Km/Hrs): ' + str(self.velocidad)


class Bici(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ', Tipo de la Bicicleta: ' + self.tipo


# Primer objeto de la calse Padre Vehiculo
vehiculo = Vehiculo('Blanco', 4)
print(vehiculo)

# Segundo objeto de la calse Hija Auto
auto = Auto('Amarillo', 4, 120)
print(auto)

# Tercer objeto de la calse Hija Bici
bici = Bici('Roja', 2, 'Playera')
print(bici)
