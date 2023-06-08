#creamos una lista con list()
lista = list(['hola', 'cano', 45, 643, 63, 6])


#devuelve la cantidad de elementos que tenemos en una lista
cantidad_Elementos = len(lista)
print(cantidad_Elementos)


#agregando elementos a la lista
lista.append('JAJAJA')
print(lista)


#agregando un elemento a la lista en un indice especifico
lista.insert(2, 'vamo boca')
print(lista)


#agrgando varios elementos
lista.extend([16, 4])
print(lista)


#eliminamos elementos de la lista (por indice)
print(len(lista))
lista.pop(2)
print(len(lista))


#removiendo elementos de la lista por valor
lista.remove('hola')
print(lista)

"""
#eliminando todos los elementos de la lista
lista.clear()
print(lista)


#ordenamos elementos de la lista (si usamos el parametro reverse = True lo ordena de reversa)
lista.sort()#nececita que sean solo numeros

#invirtiendo elementos de una lista sin ordenarlos
lista.reverse()#nececita que sean solo numeros
"""

