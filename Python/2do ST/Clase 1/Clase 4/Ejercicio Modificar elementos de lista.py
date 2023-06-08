lista = list(range (1, 11))
print('Lista Original')
for i in lista:
    print(i, end='-')
valor = int(input('\nDigite un Valor a Multiplicar: '))

# Multiplicamos todos los elemntos de la lista

for indice, i in enumerate(lista):# Funcion Modifica los indeces de la lista
    lista[indice] *= valor# El iterador solo recorre los indices, en esta linea se multiplica

print(f'Lista final con los elementos multiplicados por {valor}')

for i in lista:
    print(i, end='-')