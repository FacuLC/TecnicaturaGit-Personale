animales = ['pez', 'gato', 'perro', 'loro']
numeros = []

# recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es: {animal}')

# recorriendo la lista numeros y multiplicando el valor x2
for numero in numeros:
    resultado = numero*2
    print(resultado)

# recorrer dos listas del mismo tamaño al mismo tiempo
for animal, numero in zip(animales, numeros):
    print(f'recorriendo lista 1: {animal}')
    print(f'recorriendo lista 2: {numero}')

# forma no correcta de recorrer una lista con su indice (no funciona en conjuntos o set)
for num in range(len(numeros)):
    print(numeros[num])

# forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indide = num[0]
    valor = num[1]
    print(f'El indice es: {indide} y el valor es: {valor}')

# este queda mas cheto
for i, val in enumerate(numeros):
    print(f'El indice es: {i} y el valor es: {val}')

# usando for / else
for numero in numeros:
    print(f'ejecutandi el ultimo bucle, valor actual: {numeros}')
else:
    print('el bulce termino')