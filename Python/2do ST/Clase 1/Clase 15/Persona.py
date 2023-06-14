class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Esta funcion nos permite sumar objetos dentro de una clase
    def __add__(self, other): # Other =  otro
        return f'{self.nombre} {other.nombre}'

    # __sub__ sirve para restar
    def __sub__(self, otro):
        return self.edad - otro.edad



objeto1 = Persona('Facundo', 22)

objeto2 = Persona('Leonel', 19)

# objeto1.__add__(objeto2); Esta es la sintaxis interna y automatica

print(objeto1 + objeto2)

print(objeto1- objeto2)