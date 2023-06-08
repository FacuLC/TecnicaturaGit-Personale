numero = int(input('Digite un numero: '))

lista = []

for i in range(1, 11):
    resultado = i * numero
    lista.append(resultado)
    print(numero, 'X', i, '=', resultado)

print(f'\nTabla de Multiplicar del {numero}: \n{lista}  ')
