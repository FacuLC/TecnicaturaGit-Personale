# Ejercicio de Coleciones 2

lista1 = [3, 4, 2, 4, 3, 1, 3, 7, 9, 4, 5, 3, 1]
lista2 = [1, 2, 5, 8, 3, 5, 7, 7, 4, 3, 1, 3, 7]

print(f'\nElementos de la primera lista: {lista1}')
print(f'\nElementos de la segunda lista: {lista2}\n')

conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2)# Unimos los dos conjuntos
solo1 = list(conjunto1 - conjunto2)# Solo muestra el conjunto1
solo2 = list(conjunto2 - conjunto1)# Solo muestra el conjunto2
ambos = list(conjunto1 & conjunto2)# Mostramos ambas listas

print(f'Elementos que aparecen en las listas: {union}')
print(f'Lista de palabras que aparecen en la primera lista, pero no en la segunda: {solo1}')
print(f'Lista de palabras que aparecen en la segunda lista, pero no en la primera: {solo2}')
print(f'Lista de palabras que aparecen en ambas listas: {ambos}')
