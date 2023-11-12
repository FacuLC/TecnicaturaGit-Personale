from NumerosIgualesExceptions import NumerosIguales

resultado = None

try:
    a = int(input('Digite el primer numero: '))
    b = int(input('Digite el segundo numero: '))
    if a == b:
        raise NumerosIguales('Son Numeros Iguales')  # La palabra (raise) se utiliza para arrojar una exception
    resultado = a / b  # Lo modificamos

except TypeError as error:
    print(f'TypeError - Ocurrio un error: {type(error)}')

except ZeroDivisionError as error:
    print(f'ZeroDivisionError - Ocurrio un error: {type(error)}')

except Exception as error:  # Es mejor usar la Clase Padre (Exception)
    print(f'Exception - Ocurrio un Error: {error}')
else:
    print('No se arrojo ninguna excepcion ')

finally:  # Siempre se va ejecutar
    print('Ejecucion de este bloque finally')

print(f'El resultado es: {resultado}')
print('seguimos...')
