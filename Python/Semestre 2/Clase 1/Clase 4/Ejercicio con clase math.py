# Ejercicio 4 Colecciones - [Clase - n° 4]

# Importamos la calse math para hacer uso de la funcion sqrt (Raiz Cuadrada)
import math

numero = int(input('\nDigite un Numero Posotivo: '))
while numero < 0:
    print('Error -> Deveria ser un Numero Positivo')
    numero = int(input('Digite un Numero Positivo: '))
print(f'\nSu Raiz Cuadrada es: {math.sqrt(numero):.2f}')
