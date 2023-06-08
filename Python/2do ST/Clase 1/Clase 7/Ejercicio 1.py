# Cre una funcion para multiplicar los valores recibidos
# de tipo numerico y regresar como resultado la multiplicacion de todos los valores pasados como argumentos

def multi(*args):
    resultado = 1 # El 0 no nos ayuda a multiplicar
    for numero in args:
        resultado *= numero
    return resultado


print(multi(3, 5, 15, 3))
