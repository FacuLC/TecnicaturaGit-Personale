# forma no optima de sumar valores
#def suma(lista):
#    numero_sumados = 0
#   for numero in lista:
#        numero_sumados = numero_sumados + numero
#    return numero_sumados

#resultado = suma([5,3,9,10,20,3])

# Forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])
resultado = suma_total([5,3,9,10,20,3])

print(resultado)

# utilizando parametro args

def suma(nombre,*numeros):
    return f'{nombre}, la suma de tus numeros es: {sum(numeros)}'

resultado = suma('Facundo',3,4,52,5,45,3)
print(resultado)