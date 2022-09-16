# Ejercicio  [Clase 5]
a = int(input('Digite de donde va a comenzar la suma: '))
b = int(input('Digite hasta donde quiere llegar la suma: '))
suma = 0
for i in range(a,b+1):
    if i % 2 == 0: # Esto es para el numero par
        suma += i
print(f'\nLa suma de numeros pares es: {suma}')

# Ejercicio 2

numero = int(input('Digite un numero: '))
while numero < 0: # Mientras el numero sea negativo
    print('Error -> El numero tiene que ser positivo')
    numero = int(input('Digite un numero: '))

factorial= 1
if numero!=0:
    for i in range(1, numero+1):
        factorial *= i
    print(f'\nEl factorial del numero {numero} positivo ingresado es: {factorial}')