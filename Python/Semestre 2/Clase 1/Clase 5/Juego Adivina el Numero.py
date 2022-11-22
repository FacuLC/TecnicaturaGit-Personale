import random
aleatorio = random.randint(0, 100) # Toma del 0 a 100 de manera literal, genermaos un numero aletaorio
contador = 0

while True:
    numero = int(input('Digite un numero: '))
    contador += 1
    if numero > aleatorio:
        print('\tNo es el Numero, digite un numero menor')
    elif numero < aleatorio:
        print('\tNo es el Numero, digite un numero mayor')
    else:
        print('!!!FELICIDADES!!!\nAcabas de adivinar el numero', aleatorio)
        break

print('Numero de Intentos Realizados: ',contador)