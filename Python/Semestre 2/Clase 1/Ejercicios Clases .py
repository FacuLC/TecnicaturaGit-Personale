# Ejercicio1
print("Rango de 0 a 10 con numeros divisibles entre 3")
for i in range(11):
    if i % 3 == 0:
        print(i)
print("")

# Ejercicio2
print("Crea un rango de 2 a 7")
rango = range(2, 7)
for i in rango :
    print(i)
print("")

# Ejercicio 3
print("Crea un rango del 3 al 10 con incremento de 2")
for i in range(3, 11, 2):
    print(i)
print(" ")

# Ejercicio 4
tupla = (13, 1, 8, 3, 2, 5, 8)
for i in tupla:
    if i<5:
        print(i, end=" ")

# Ejercicio de la Seleccion - [Clase n° 3]
seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '120 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.75, 'Precio': '100 Millones', 'Posicion': 'Extremo Derecho'},
    23: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '40 Millones', 'Posicion': 'Defensor Central'},
    29: {'Nombre': 'Emiliano Martinez', 'Edad': 33, 'Altura': 1.94, 'Precio': '70 Millones', 'Posicion': 'Portero'},
    19: {'Nombre': 'Julian Alvarez', 'Edad': 22, 'Altura': 1.73, 'Precio': '80 Millones', 'Posicion': 'Delantero Central'},
    9: {'Nombre': 'Lautaro Martinez', 'Edad': 24, 'Altura': 1.77, 'Precio': '90 Millones', 'Posicion': 'Delantero Central'},
    7: {'Nombre': 'Rodrigo De Paoul', 'Edad': 26, 'Altura': 1.78, 'Precio': '80 Millones', 'Posicion': 'Medio Campista'},
    22: {'Nombre': 'Leandro Paredes', 'Edad': 24, 'Altura': 1.82, 'Precio': '70 Millones', 'Posicion': 'Medio Defensivo'}
}
for dorsal, detalles in seleccionArgentina.items():
    print(dorsal, detalles)
print(len(f"{seleccionArgentina}\n"))


# Ejercicio  de Colecciones - [Clase n° 4]

# Eliminar elementos duplicados
lista = [1, 2, 3, 'Facundo', 2001, 7, 7, 3, 'Renzo', 2001]

###
# conjunto = set(lista) # Convertimos la lista a un conjunto de tipo set
# lista = list(conjunto) # Convertimos el conjunto a una lista
###

# Hacemos lo de arriba pero en una linea de codigo
lista = list(set(lista)) # Codigo de Eficiente
print(lista)

# Ejercicio de Coleciones 2

lista4 = [3, 4, 2, 4, 3, 1, 3, 7, 9, 4, 5, 3, 1]
lista5 = [1, 2, 5, 8, 3, 5, 7, 7, 4, 3, 1, 3, 7]

print(f'\nElementos de la primera lista: {lista4}')
print(f'\nElementos de la segunda lista: {lista5}\n')

conjunto1 = set(lista4)
conjunto2 = set(lista5)

union = list(conjunto1 | conjunto2) # Unimos los dos conjuntos
solo1 = list(conjunto1 - conjunto2) # Solo muestra el conjunto1
solo2 = list(conjunto2 - conjunto1) # Solo muestra el conjunto2
interseccion = list(conjunto1 & conjunto2) # Mostramos ambas listas

print(f'Elementos que aparecen en las listas: {union}')
print(f'Lista de palabras que aparecen en la primera lista, pero no en la segunda: {solo1}')
print(f'Lista de palabras que aparecen en la segunda lista, pero no en la primera: {solo2}')
print(f'Lista de palabras que aparecen en ambas listas: {interseccion}')

# Ejercicio 3 de Colecciones - [Clase n° 4]

listaVacia = []

diccionario = {
    'ARA':'Nombre: Aragon\nClase: Guerrero\nRaza: Dunan del Norte',
    'GAN':'Nombre: Gandalf\nClase: Mago\nRaza: Istar',
    'LEO':'Nombre: Legolas\nClase: Arquero\nRaza: Elfo Sindar',
    'SAU':'Nombre: Sauron\nClase: Guerreo\nRaza: Maiar',
    'GOL':'Nombre: Gollum\nClase: Hermitaño\nRaza: Hobbit',
    'GLO':'Nombre: Gloin\nClase: Guerrero\nRaza: Enanos'
}

P = {'Nombre':'Aragon', 'Clase':'Guerrero', 'Raza':'Dunan del Norte'}
listaVacia.append(f'{P}\n')
P = {'Nombre':'Gandalf', 'Clase':'Mago', 'Raza':'Istar'}
listaVacia.append(f'{P}\n')
P = {'Nombre':'Legolas', 'Clase':'Arquero', 'Raza':'Elfo Sindar'}
listaVacia.append(f'{P}\n')
P = {'Nombre':'Sauron', 'Clase':'Guerreo', 'Raza':'Maiar'}
listaVacia.append(f'{P}\n')
P = {'Nombre':'Gollum', 'Clase':'Hermitaño', 'Raza':'Hobbit'}
listaVacia.append(f'{P}\n')
P = {'Nombre':'Gloin', 'Clase':'Guerrero', 'Raza':'Enanos'}
listaVacia.append(f'{P}\n')
print(f'\n{listaVacia}')

# Ejercicio 4 Colecciones - [Clase - n° 4]

# Importamos la calse math para hacer uso de la funcion sqrt (Raiz Cuadrada)
import math

numero = int(input('\nDigite un Numero Posotivo: '))
while numero < 0:
    print('Error -> Deveria ser un Numero Positivo')
    numero = int(input('Digite un Numero Positivo: '))
print(f'\nSu Raiz Cuadrada es: {math.sqrt(numero):.2f}')

# Ejercicio 5 Colecciones [Clase - n° 4]

for i in range (1, 51):
    print(i,end='-')

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