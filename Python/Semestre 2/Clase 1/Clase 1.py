# lista = Ariel, Liliana, Naty, Osvaldo
# Colecciones en Python

# Las lsitas es lo que se conoce en otros lenguajes como arreglos o vectores

from builtins import print

nombres = ["Naty", "Osvaldo", "Liliana", "Ariel"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[2])

# Si queremos saber el final de la lista
print(nombres[-1])

# Solo muestra el indice 0, 1 pero no el indice 2
print(nombres[0:2])

# Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])  # Indices a mostrar 0, 1, 2

# Desde el indicado hasta el final
print(nombres[1:])

# Modificamos un valor
nombres[2] = "Lili"
nombres [0] = "Natalia"
print(nombres)

# Iterar la lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print("Se terminaron los elemento de la lista")
print("")

# Preguntamos cuantos elementos tiene  una lista
print(len(nombres))# le pasamos como parametro la lista

# Agregamos un elemento
nombres.append("Facundo")
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)# Se agrega al final de la lista

# Insertar un elemento en un indice especifico
nombres.insert(1, "Leonel")# Primero indicamos la posicion, luego el nombre
print(nombres)

nombres.insert(3, "Cano")
print(nombres)

# Eliminamos un elemento
nombres.remove("Cano")
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indicde especifico
del nombres[2]# del= es eliminar
print(nombres)

# Eliminar todos los elementos de la lista
nombres.clear()
print(nombres)

# Eliminar toda la lista
del nombres
# print(nombres)

# Definimos una tupla
cocina = ("cuchara", "cuchillo", "tenedor")
print(len(cocina))# con "len" sabemos cuantos elementos tenemos en la tupla

# Accder a un elemento, para esto utilizamos corchetes no parentecis
print(cocina[0])

# Manera Iversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])

# Ejemplo
verduras = ("papa" ,) # Una tupla necesita aunque sea un elemento: la "," (sino seria un tipo cadena)

# Recordemos los elementos de tupla
for cocinar in cocina:# Print esta usando \n saltos de linea
    print(cocinar, end=" ")# Usamos "end=" para eliminar los saltos de linea

# Modificamos un objeto espesifico de la tupla y pasamos de tupla a lista y de lista a tupla
cocinaLista = list(cocina)
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista)
print("\n",cocina)


# Tipo Set
planetas = {"Marte", "Jupiter", "Venus"}
print(len(planetas)) # usamos la funcion (len) para saber la cantidad de elemntos

# Revisar si un elemento existe dentro de set
print("Marte" not in planetas)

# Agregamos un elemento
planetas.add("Tierra") # add es una funcion para agregar elemntos
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove("Jupiter") # Esta funcion al tomar un mal ingreso de un elemento da error
print(planetas)
planetas.discard("Tierra") # Esta funcion no nos presenta ningun tipo de error
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Para eliminar
#del planetas
#print(planetas)

# "Maradona" :10 Un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(Key,value)
diccionario = {
    "IDE":"Integrated Development Environment",
    "POO":"Programacion Orientada a Objetos",
    "SABD":"Sistema de Administracion de Base de Datos"
}
# Vrificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder al diccionario con la llave (key)
print(diccionario["IDE"])

# Otras Formas de recuperar un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

#Modificamos elementos
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: #Recorremos mostrando solo las llaves
    print(termino)

# Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) # Muestra solo las llaves

# Usamos una funcion para acceder al valor
for valor in diccionario.values():
    print(valor)

# Comprobar la existencia de un elemento
print("IDE" in diccionario) # Devuelve un booleano

# Agregar un elemento
diccionario["PK"] = "Primary key"
print(diccionario)

# Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar un diccionario
del diccionario
#print(diccionario) # El diccionario se borro

# Concatenar listas
lista1 =[1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2
print(lista3)

# Esta es una funcion para agregar varios elementos a una lista
lista3.extend([7, 8, 9, 1])
print(lista3)

# Funcion que nos permite saber en que indice esta un elemento
print(lista3.index(5))

# Para saber cuantos valores repetidos hay en una lista
print(lista3.count(1)) # Cuenta cuantos valores hay repetidos dentro de la lista

# Para poner nustra lista al reves
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3*2
print(lista3)

# Metodos de Ordenamiento
lista3.sort()
print(lista3)
# Ordena de manera descendente
lista3.sort(reverse=True)
print(lista3)

# Una tupla puede tener diferentes tipos de datos adentro
tupla = (4, "Hola", 6.78, [1, 2, 78], 4, "Hola")
print(tupla)

# Accion booleana, su respuesta es en tipo booleana
print(4 in tupla)
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

# Repaso de set o conjunto
# para definir un conjunto
conjunto1 = set()
conjunto2 = {"bye",}
conjunto1.add(7)
conjunto1.add("Hola")
print(conjunto1)
conjunto2.add("Hola de nuevo")
print(conjunto2)
print(3 not in conjunto2) #Preguntamos si el numero "3" NO esta en el conjunto1

# Como hacer la igualdad de dos conjuntos
print(conjunto2 == conjunto1) # Nos devuelve como respuesta un booleano

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La linea une los conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Que elementos tienen en comun
print(conjunto3)

# Asigna el valor que esta en el conjunto1 y no en el conjunto2
conjunto3 = conjunto1 - conjunto2
print(conjunto3)
# Lo mismo pero de manera inversa
conjunto3 = conjunto2 - conjunto1

# Elementos que no comparten o que son diferentes entre ambos
conjunto3 = conjunto1 ^ conjunto2
print(conjunto3)

conjunto3 = conjunto1|conjunto2
print(conjunto2.issubset(conjunto3)) # Aqui preguntamos si un conjunto es un subconjunto de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto1 estan dentro del conjunto3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elemtos en comun
print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en comun

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso de Dicconarios
diccionarioNuevo = {"Azul":'Blue', 'Rojo':'Red', 'Verde':'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)
del (diccionarioNuevo["Azul"])
print(diccionarioNuevo)

# Los Diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Facundo':{'Edad': 21, 'Altura': 1.78}, 'Renzo':[21, 1.77], 'Bueno': [20, 1.70]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '120 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.75, 'Precio': '100 Millones', 'Posicion': 'Extremo Derecho'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '40 Millones', 'Posicion': 'Defensor Central'},
    29: {'Nombre': 'Emiliano Martinez', 'Edad': 33, 'Altura': 1.94, 'Precio': '70 Millones', 'Posicion': 'Portero'},
}
print(seleccionArgentina[10])

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# Pilas Usando Listas
pila = [1, 2, 3]

# Agregamos elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Eliminamos ellemntos desde el final
# pila.pop()
# print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop() # Quita el ultimo elemento y lo guarda en la variable
print(f'Sacamos el elemento: {elementoBorrado}')
print(f'La pila ahora queda asi: {pila}')

# Cola con Listas
# Estructura de datos de tipos fifo (first input / first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(f'\n{cola}')

# Sacamos elementos de la cola
fuera = cola.pop(0)
print(f'\nAtendido/a: {fuera}')
print(f'Proximo a ateder: {cola}')

fuera = cola.pop(0)
print(f'\nAtendido/a: {fuera}')
print(f'Proximo a ateder: {cola}')

fuera = cola.pop(0)
print(f'\nAtendido/a: {fuera}')
print(f'Proximo a ateder: {cola}')

fuera = cola.pop(0)
print(f'\nAtendido/a: {fuera}')
print(f'Proximo a ateder: {cola}')

fuera = cola.pop(0)
print(f'\nAtendido/a: {fuera}')
print(f'Proximo a ateder: {cola}')

#Seguimos mostrando como recorrer un diccionario con el ciclo for

for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')