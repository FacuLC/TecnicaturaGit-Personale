
agenda = {}

while True:
    print('\t.:MENU:.')
    print('1. NUEVO CONTACTO')
    print('2. BORRAR CONTACTO')
    print('3. VER LISTA DE CONTACTOS')
    print('4. SALIR')

    opcion = int(input('SELECCIONES UNA OPCION ->'))

    if opcion == 1:
        nombre = input('DIGITE EL NOMBRE DEL CONTACTO ->')
        telefono = input('DIGITE EL NUMERO DE TELEFONO ->')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('CONTACTO GUARDADO')
        else:
            print('ESE CONTACTO YA ESTA EN LA AGENDA')

    elif opcion == 2:
        nombre = input('CUAL CONTACTO DESEAS ELIMINAR -> ')
        if nombre in agenda:
            del (agenda[nombre])
            print('\nCONTACTO ELIMINADO')
        else:
            print('\nEL CONTACTO NO EXISTE')

    elif opcion == 3:
        print('AGENDA DE CONTACTOS\n')
        for nombre_clave, valor in agenda.items():
            print(f'NOMBRE: {nombre_clave}\nTELEFONO: {valor}\n')

    elif opcion == 4:
        print('GRACIAS POR UTILIZAR SU AGENDA DE CONTACTOS')
        break

    else:
        print('!!ERROR DE OPCION!!')
print('')