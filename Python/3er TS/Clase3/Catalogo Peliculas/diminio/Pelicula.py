class Peliculas:
    def __init__(self, nombre):
        self._nombre = nombre

    #  metodo (__str__)
    def __str__(self):
        return f'Pelicula: {self._nombre}'

    # metodo get y set para nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre