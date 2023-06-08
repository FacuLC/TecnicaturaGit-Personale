"""
# Ejercicio 1: Crear un rango del 0 al 10 e imprimir numeros divicibles entre 3

divisor = int(input('\nCual es el divisor que desea usar: '))
rango = int(input(f'\nHasta que numero quiere saber si es divisible el {divisor}? : '))

for numero in range(0, rango+1):
    if numero % divisor == 0:
        print(numero)
print('Fin del Programa LOKITO')


# Ejercicio 2: Crear un rango del 2 al 6 e imprimelos

def rangos(a, b):
    print(f'El Rango de numeros es del ({a}) hasta el ({b})')
    for numero in range(a, b + 1):
        print(numero)

print(rangos(2, 6))


# Ejercicio 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2
for numero in range(3, 10, 2):# en el metodo {range()}, podemos agregar un incremento en el ultimo slot
    print(numero)
"""

# Ejercicio 4: Dada la siguiente tupla crear una lista que solo inluya los numeros menors a 5

tupla = (13, 1, 8, 3, 2, 5, 8)
lista = list(tupla)
lista.sort()
print(lista[:4])
