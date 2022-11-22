class Persona2:
    def __init__(self, nombre, apellido, edad, altura, peso, dni):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._altura = altura
        self._peso = peso
        self._dni = dni

    def mostrar_detalles(self):
        print(f'\nLos datos a mostrar son los siguientes \nNombre-> {self._nombre} {self._apellido} \nEdad -> {self._edad} Años \nEstatura -> {self._altura} Mts. \nPeso -> {self._peso}Kg \nN° de Documento -> {self._dni}')

    @property  # Decorador (Se necesita para el metodo Geter)
    def nombre(self):  # Metodo Geter
        print('Estamos utilizando el metodo Get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Metodo Seter
        print('Estamos utilizando el metodo Set')
        self._nombre = nombre

    @property
    def apellido(self):
        print('Estamos Utilizando el Metodo Get para el apellido')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        print('Estamos Utilizando el metodo Set para el Apellido')
        self._apellido = apellido

    @property
    def edad(self):
        print('Estamos Utilizando el metodo Get para la Edad')
        return self._edad

    @edad.setter
    def edad(self, edad):
        print('Estamos Utilizando el metodo Set para la Edad')
        self._edad = edad

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

persona1 = Persona2('Facundo', 'Cano', 21, 75, 1.78, 34536262)

# persona1._nombre# (error, esto no se deberia hacer)

# Atributo Nombre
print(persona1.nombre)# Llamamos el metodo Geter
persona1.nombre = 'Daniel'# Llamamos el metodo Seter
print(persona1.nombre)# Otra vez llamamos al metodo Geter

# Atributo Apellido
print(persona1.apellido)
persona1.apellido = 'Chosco'
print(persona1.apellido)

# Atributo Edad
print(persona1.edad)
persona1.edad = 40
print(persona1.edad)

# Atributo Peso
persona1.peso = 94

# Atributo Altura
persona1.altura = 1.75

# Atributo Dni
persona1.dni = 6354136546

persona1.mostrar_detalles()

"""
PARA QUE UN ATRIBUTO SOLO SEA PARA LECTURA
ES CUANDO TENEMOS UN ATRIBUTO ESTA ENCAPSULADO
Y NO ESTA EL METODO SETER PARA PODER MODIFICAR EL ATRIBUTO
ENTONCES QUEDA (READ-ONLY) 
"""


