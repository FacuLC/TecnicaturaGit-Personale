# Lista de comprension
nombres = ['Facundo', 'Franco', 'Santiago', 'Ezequiel']
lista = [p for p in nombres if p [0] == 'F'] # Esto regresa una nueva lista
print(lista)

# Ejemplo con Diccionario
nombres2 = [{'nombre': 'Quilmes', 'Pais': 'Arg'},
            {'nombre': 'Corona', 'Pais': 'Mex'},
            {'nombre': 'Stella Artois', 'Pais': 'Belgica'}
            ]
cerveza = [a for a in nombres2 if a['Pais'] == 'Arg']

print(cerveza)
print(nombres2)