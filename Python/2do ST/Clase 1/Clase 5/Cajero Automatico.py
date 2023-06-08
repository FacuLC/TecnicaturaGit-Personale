saldo = 1000

while True:
    print('\t.:MENU:.')
    print('1. INGRESAR DENIERO EN SU CUENTA')
    print('2. RETIRAR DINERO DE SU CUENTA')
    print('3. MOSTRAR DINERO DISPONIBLE')
    print('4. SALIR')

    opcion = int(input('Degite una opcion del Menu: '))
    print('')
    if opcion == 1:
        extra = float(input('Cuanto Dinero Desea Ingresar -> '))
        saldo += extra
        print(f'EL Dinero de su Cuenta es de: ${saldo}')
    elif opcion == 2:
        retirar = float(input('Cuanto Dinero Desea Retirar -> '))
        if retirar > saldo:
            print('No Tiene esa Cantidad de Dinero')
        else:
            saldo -= retirar
            print(f'Dinero en su Cuenta: {saldo}')
    elif opcion == 3:
        print(f'El Dinero en su Cuenta es de: ${saldo}')
    elif opcion == 4:
        print('!!GRACIAS POR UTILIZAR SU CAJERO AUTOMATICO!!')
        break
    else:
        print('ERROR SE EQUIVOCO DE OPCION DE MENU')