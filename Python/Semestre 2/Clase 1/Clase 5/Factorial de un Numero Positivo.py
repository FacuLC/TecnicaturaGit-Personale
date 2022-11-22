numero = int(input('Digite un numero: '))
while numero < 0:
    print('Error -> El Numero debe ser Positivo: ')
    numero = int(input('Digite un numero: '))

factorial = 1
for i in range(1, numero+1):
    factorial *= i
print(f'\nEl Factoril del numero {numero} positivo ingresado es: {factorial}')