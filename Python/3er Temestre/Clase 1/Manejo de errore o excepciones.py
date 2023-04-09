from Excep_Numero_Iguales import NumerosIgualesException
resultado = None
try:
    a = int(input('Digite el Primer Numero: '))
    b = int(input('Digite el Segundo Numero: '))

    resultado = a/b # Modificamos el Proceso

    if a == b:
        raise NumerosIgualesException('Los Numeros son Iguales') # La palabara (Raise) sirve para hcer una excepcion

except TypeError as e:
    print(f'Ocurrio un Error {e}')

except ZeroDivisionError as e:
    print(f'Ocurrio un Error {e}')

except Exception as e:
    print(f'Ocurrio un Error {e}')

else:
    print('No se arrojo ninguna excepcion')

finally:
    print('Ejecucion de Bloque finally')

print(f'El resultado es: {resultado}')
print('Seguimos. . .')