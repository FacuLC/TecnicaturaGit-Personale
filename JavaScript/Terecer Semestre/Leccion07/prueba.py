def bienvenida(nombre, genero):
    genero = genero.lower()
    if genero == 'hombre':
        return f'Hola {nombre}, BIENVENIDO CRACK'
    elif genero == 'mujer':
        return f'Hola {nombre}, Te Damos La BIENVENIDA REINA'
    else:
        return 'ERROR EN EL INGRESO DE DATOS'
    
print(bienvenida('Facundo', 'HomBre'))
print(bienvenida('Erika', 'MuJer'))
print(bienvenida('Facundo', 'Hom'))