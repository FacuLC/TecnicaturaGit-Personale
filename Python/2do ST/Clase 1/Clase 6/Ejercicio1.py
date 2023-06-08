# Crear Funcion para sumar los valores recibidos de tipo numericos, utilizando argumnetos variables *args
# Como parametro de la funcion y agregar como resultado la suma de todos los valores pasados como argumentos

def suma(*args):
    resultado = 0
    # Iteramos elementos
    for valor in args:
        resultado += valor
    return resultado


print(suma(3, 5, 9))
