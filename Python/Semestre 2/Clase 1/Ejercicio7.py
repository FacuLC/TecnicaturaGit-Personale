# Ejercicio 7 Colecciones [Clase - n° 4]

lista3 = []
salir = False
while not salir:
    numero = int(input('Digite un numero: '))
    if numero == 0:
        salir = True
    else:
        lista3.append(numero)
lista3.sort() # La lista esta ordenada con esta funcion
print(f'\nLista Ordenada: \n{lista3}')