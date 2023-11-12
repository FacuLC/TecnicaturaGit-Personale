import os


class CatalogoPelis:
    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregar_peliculas(cls, pelicula_nueva):
        with open(cls.ruta_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(f'{pelicula_nueva.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf-8') as archivo:
            print(f'Catalogo de Peliculas'.center(50, '-'))
            print(archivo.read())

    @classmethod
    def eliminar_pelicula(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo Eliminado: {cls.ruta_archivo}')
