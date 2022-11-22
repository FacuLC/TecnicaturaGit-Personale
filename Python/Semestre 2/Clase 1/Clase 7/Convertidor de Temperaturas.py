def celcius(celcius):
    return celcius * 9 / 5 + 32 # La presedencia : Multiplicacion, Divicion Y Suma

n = float(input(f'Digite el valor de grados Celcius -> '))
resultado = celcius(n)
print(f'{n} C° a F° -> {resultado:.2f}') # El (:.2f) es para mostrar dos valores despues de la coma o el punto

def farenheit(farenheit):
    return (farenheit - 32) * 5 / 9

n2 = float(input(f'\nDigite el valor de grados Farenheit -> '))
resultado2 = farenheit(n2)
print(f'{n2} F° a C° -> {resultado2:.2f}')