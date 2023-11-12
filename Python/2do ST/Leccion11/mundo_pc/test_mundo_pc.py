from computadora import Computadora
from monitor import Monitor
from orden import Orden
from raton import Raton
from teclado import Teclado


teclado1 = Teclado('HP', 'USB')
monitor1 = Monitor('HP', '15 Pulgadas')
raton1 = Raton('HP', 'USB')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)


teclado2 = Teclado('Acer', 'Bluetooth')
monitor2 = Monitor('Acer', '27 Pulgadas')
raton2 = Raton('Acer', 'Bluetooth')
computadora2 = Computadora('Acer', monitor2, teclado2, raton2)

teclado3 = Teclado('Racer', 'Bluetooth / Membrana')
monitor3 = Monitor('Samsung', '30 Pulgadas')
raton3 = Raton('Racer', 'Bluetooth / Gamer')
computadora3 = Computadora('Gamer', monitor2, teclado2, raton2)

teclado4 = Teclado('Logitech', 'Bluetooth / Rgb Membrana')
monitor4 = Monitor('Sony', '27 Pulgadas')
raton4 = Raton('Logitech', 'Bluetooth / sensor con dpi 100')
computadora4 = Computadora('Gamer', monitor2, teclado2, raton2)


computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)

computadoras2 = [computadora3, computadora4]
orden2 = Orden(computadoras2)
print(orden2)
