# Leccion 12 - Clase 15 POO Parte 8 Diseño de clases y Sobrecarga de Operadores

# Alumno: FACUNDO LEONEL CANO

class Persona:
    def __init__(self, Nombre, Edad, ComidaFavorita):
        self.Nombre = Nombre
        self.Edad = Edad
        self.ComidaFavorita = ComidaFavorita

    def __add__(self, other):  # Esta es la (Suma, Otro - Other)
        return f"{self.Nombre} {other.Nombre} {self.ComidaFavorita} {other.ComidaFavorita}"

    def __sub__(self, Otro):  # Esta es la Resta
        return self.Edad - Otro.Edad

# Ingreso de Datos


Persona1 = Persona("Facundo", 21, ["Sandia", "Naranja"])

Persona2 = Persona("Loenel", 18, ["Granada", "Mandarina"])

#  Persona1.__add__(Persona2) Sintaxis Interna y Automatica

print(f'Datos Importantes'.center(50, '-'))

print(f'Suma de los Objetos: {Persona1 + Persona2}')

print(f'Resta de los Objetos: {Persona1 - Persona2}')

print(f'Suma de las Comidas Favoritas: {Persona1.ComidaFavorita + Persona2.ComidaFavorita}')
