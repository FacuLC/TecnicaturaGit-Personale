a = int(input('Digite de donde quiere comezar la suma: '))
b = int(input('Digite hasta donde quiere llegar la suma: '))
suma = 0
for i in range(a, b +1): # El [+1] es porque simpre toma un numero menos en la funcion {range}
    if i % 2 == 0: # Esto es para los numeros pares
        suma += i
print(f'\nLa suma de numeros pares dentro del rango es: {suma}')