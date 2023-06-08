frutas = ['naranja','banana','cereza','manzana','pera','durazno']
cadena = 'Hola perrillo deja la puta paja'
numeros = [2, 5, 8, 10]
# evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'Me voy a comer una: {fruta}')


# evitar que el bulce siga ejecutandose
for fruta in frutas:
    print(f'Me voy a comer una: {fruta}')
    if fruta == 'manzana':
        break
else:
    print('bucle terminado')

# for un una sola linea de codigo (duplicando los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)