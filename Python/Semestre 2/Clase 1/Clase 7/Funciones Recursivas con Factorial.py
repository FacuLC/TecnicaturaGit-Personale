# Funciones Recursivas
def factorial(n):
    if n == 1: # Caso base
        return 1
    else:
        return n * factorial(n - 1) # Caso Recursivo



numero1 = int(input('Digite el numero del cual desea saber el factorial -> '))

print(f'EL factorial del numero {numero1} es: {factorial(numero1)}')