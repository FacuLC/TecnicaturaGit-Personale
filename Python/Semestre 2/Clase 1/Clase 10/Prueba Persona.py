from Persona2 import Persona2

print('Creacion de Objetos'.center(50, '-'))
if __name__ == '__main__':
    persona5 = Persona2('Leonel', 'Cano', 21, 1.78, 75, 43353664)
    persona5.mostrar_detalles()

    print(__name__)

print('Eliminacion de Objetos'.center(30, '-'))

del persona5