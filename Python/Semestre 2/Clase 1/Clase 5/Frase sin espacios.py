frase = input('Escriba una Frase: ')
frase2 = ' '
for i in frase:
    if i != ' ':
        frase2 += i
frase = frase2
print(f'\nFrase Final:{frase}')
print(f'N° de Caracteres: {len(frase)}')