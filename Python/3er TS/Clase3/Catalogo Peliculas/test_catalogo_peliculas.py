from diminio.Pelicula import Peliculas
from servicio.catalogo_pelicula import CatalogoPelis
opcion = None

while opcion != 4:
    try:
        print('Opciones del Menu'.center(50, '-'))
        print('1. Agregar Pelicula')
        print('2. Lista de Peliculas')
        print('3. Eliminar Pelicula')
        print('4. Salir')

        opcion = int(input('\nSeleccione una Opcion del Menu: '))

        if opcion == 1:
            nombre_pelicula = input('Ingrese el Nombre de la Pelicula: ')
            pelicula = Peliculas(nombre_pelicula)
            CatalogoPelis.agregar_peliculas(pelicula)
        elif opcion == 2:
            CatalogoPelis.listar_peliculas()
        elif opcion == 3:
            CatalogoPelis.eliminar_pelicula()
    except Exception as error:
        print(f'La Opcion Seleccionada no es Valida: {error}')
        opcion = None
    else:
        print('Salimos del Programa')
