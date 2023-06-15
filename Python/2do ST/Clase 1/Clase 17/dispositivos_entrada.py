class DispositivoEntrada:
    def __init__(self, marca, tipo_entrada):
        self._marca = marca
        self._tipo_entrada = tipo_entrada

    property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tipoEntrada(self):
        return self._tipoEntrada

    @tipoEntrada.setter
    def tipoEntrada(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada

    def __str__(self):
        return f'Marca: {self._marca}, Tipo de Entrada: {self._tipoEntrada}'
