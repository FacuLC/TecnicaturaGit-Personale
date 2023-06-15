

from raton import Raton
from monitor import Monitor
from teclado import Teclado


class Computadora:

    contador_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadora += 1
        self._id_computadora = Computadora.contador_computadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton


    def __str__(self):
        return f'''
        {self._nombre} : {self._id_computadora},
        Monitor : {self._monitor}
        Teclado : {self._teclado}
        Ratón : {self._raton}
        '''
    
if __name__ == '__main__':
    raton1 = Raton('SAMSUNG', 'USB')
    teclado1 = Teclado('SANSUNG', 'USB')
    monitor1 = Monitor('SAMSUNG', '23')
    computadora1 = Computadora('SAMSUNG', monitor1, teclado1, raton1)
   
    raton2 = Raton('ASUS', 'Bluetooth')
    teclado2 = Teclado('ASUS', 'Bluetooth')
    monitor2 = Monitor('ASUS', '23')
    computadora2 = Computadora('ASUS', monitor2, teclado2, raton2)
    