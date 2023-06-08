def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave} : {valor}')

listarTerminos(IDE = 'Integrated Develoment Enviroment', PK = 'Primary Key')
listarTerminos(D10S = 'Leonel Messi', CR7 = 'Cristiano Ronaldo', NEY = 'Neymar Jr.')