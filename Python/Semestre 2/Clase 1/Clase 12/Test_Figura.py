from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creacion de objeto clase Cuadrado'.center(50, '_'))
cuadrado1 = Cuadrado(8, 'Azul')
cuadrado1.alto = -7 # omitio el valor x ser negativo
cuadrado1.ancho = 7
print(f'El calculo del Cuadrado es: {cuadrado1.calcular_area()}\n')

# MRO = Method Resolution Order
# print(Cuadrado.mro())# Sirve para saber el orden de las clases Padres cargadas

print(cuadrado1)

print('Creacion de objeto clase Rectangulo'.center(50, '_'))
rectangulo1 = Rectangulo(3, 9, 'Verde')
rectangulo1.ancho = 8 # omite la reacignacion
print(f'Calculo del area del Rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

# figura1 = FiguraGeometrica()# no se puede instanciar porque es abstracta

print(Cuadrado.mro())