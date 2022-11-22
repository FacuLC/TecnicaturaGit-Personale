def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlo']

desplegarNombres(nombres2)

desplegarNombres('Carla')

# desplegarNombres(10) # No es un objeto iterable

desplegarNombres((10, 11)) # Las convertimos a una tupla

desplegarNombres([22, 55]) # La combertimos a una Lista