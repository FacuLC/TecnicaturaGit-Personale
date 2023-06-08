# Forma #1
def calcular():
    precio = float(input('Ingrese el precio del Producto -> '))
    iva = float(input('Ingrese el Porcentaje de Impuesto -> '))
    impuesto = precio + precio * iva / 100
    return print(f'El pago mas Impuestos es de -> {impuesto}')
calcular()

# Forma #2

def calcular2(precio2, iva2):
    impuesto2 = precio2 + precio2 * iva2 / 100
    return impuesto2

precio2 = float(input('\nIngrese el precio del Producto -> '))

iva2 = float(input('Ingrese el Porcentaje de Impuesto -> '))

print(f'El pago total mas impuestos es de -> {calcular2(precio2, iva2)}')