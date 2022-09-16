# Ejercicio 6 Colecciones [Clase - n° 4]

lista = list(range(1, 11))
for i in lista:
    print(i, end='-')
valor = int(input('\nDigite un valor a multiplicar: '))

# Multiplicamos todos los elementos de la lista

for indice, i in enumerate(lista): # Funcion para modificar los indices de la lista
    lista[indice] *= valor # El iterador solo recorre los indices, en esta linea se multiplica

print(f'Lista Final con los elementos multiplicados por {valor}')
for i in lista:
    print(i, end='-')