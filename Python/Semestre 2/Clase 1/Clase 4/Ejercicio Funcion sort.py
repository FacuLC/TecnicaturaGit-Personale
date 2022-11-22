# Ejecicio: Insertar elementos y ordenralos
# Pedir numeros al ususario y agg a una lista, cuando el usuario ingrese el 0 el programa deja de insertar
# Mostar los numeros ordenados de menor a mayor

lista = []
salir = False
while not salir: # El operador [not] esta cambiando el salir a Verdadero [true]
    numero = int(input('Digite un Numero: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort() # La lsita esta ordenada con esta funcion
print(f'\nLista Ordenada: \n{lista}')