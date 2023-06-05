# crear funcion que tenga parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == 'mujer'):
        adjetivo = 'reina'
    elif(sexo == 'hombre'):
        adjetivo = 'titan'
    else:
        adjetivo = 'crack'
    print(f'Hola {nombre}, mi {adjetivo} ¿Como estas?')

saludar('Camila','mujer')
saludar('Facu','hombre')
saludar('Camila','ni idea')

# crear una funcion que retone valores
def crear_contraseña_random(numero):
    chars = 'abcdefghij'
    numero_entero = str(numero)
    numero = int(numero_entero[0])
    c1 = numero - 2
    c2 = numero
    c3 = numero -5
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    return contraseña, numero

# desempaquetando la funcion
password, primer_numero = crear_contraseña_random(1)

# mostrando los resultados obtenidos y los datos utilizados para obtenerlo

print(f'Tu nueva contraseña es: {password}')
print(f'El numero utilizado para crearla fue: {primer_numero}')