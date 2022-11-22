# En las listas se usan []
# En las tuplas se usan ()
# En los Diccionarios {}

# Desempaquetado de listas o list Unpacking

def show(name, lastname):
    print(name+' '+lastname)
persona = ['Facundo', 'Cano']
# Pasamos uno por uno los datos de la lista a la funcion
show(persona[0], persona[1])

# Esto es lo mismo que lo anterior pero le pasamos todo junto
show(*persona)

# Desempaquetamos a travez de una tupla
persona2 = ('Leonel', 'Cano')
show(*persona2)

# Desempaquetamos a travez de un Diccionario
persona3 = {'lastname': 'Cano', 'name': 'Rodrigo'}
show(**persona3) # Dos (**) porque son dos en los diccionarios
