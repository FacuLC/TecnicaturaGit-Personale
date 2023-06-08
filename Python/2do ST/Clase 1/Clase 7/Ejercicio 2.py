def desendente(n):
    if n < 0:
        print('Fin')
    else:
        print(n)
        desendente(n - 1)

n = int(input('Digite un numero -> '))

desendente(n)