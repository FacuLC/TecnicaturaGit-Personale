#def frase(nombre, apellido, adjetivo):
#    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'
#frase_final = frase('facundo','cano','cabeza')

# utilizando keywords arguments
# frase_final = frase(adjetivo = 'capo',nombre = 'leo',apellido = 'kano')


# creando lamisma funcion con un parametro opcional y un valor por defecto
def frase2(nombre,apellido,adjetivo='tonto'):
    return f'hola {nombre} {apellido}, sos muy {adjetivo}'

frase_final2 = frase2('leonel','silva','distraido')
print(frase_final2)