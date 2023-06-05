#Creando diccionarios con dict()
diccionario = dict(nombre='facundo', apellido='cano')


#las listas no pueden ser calves y usamos frozenset para meter conjuntos
diccionario = {frozenset(['dalto','rancio']):'jajas'}

#creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(['nombre','aplleido'])

#creando diccionarios con fromkeys() cambiando el valor por defecto a 'nose'
diccionario = dict.fromkeys(['nombre','apellido'],'no se')

print(diccionario)

diccionario = {
    'nombre':'facundo',
    'apellido':'cano',
    'edad': 22,
    'altura': 1.78
}

# esta es la manera de iterar un diccionario con (.items)

for key, value in diccionario.items():
    print(f'La calve es :{key} y el valor es: {value}')