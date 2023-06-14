from Orden import Orden
from Producto import Producto

producto1 = Producto('Zapatillas Nike', 300.00)
producto2 = Producto('Buzo de Cuerdos', 250.00)
producto3 = Producto('Camiseta', 150.00)
producto4 = Producto('Remera', 100.00)
producto5 = Producto('Pantalon', 350.00)
producto6 = Producto('Campera', 200.00)

productos1 = [producto1, producto2] # Lista de Productos
orden1 = Orden(productos1)# Primer objeto pasado la lista de productos

print(orden1)
print(f'Total de la Orden1: {orden1.calculo_total()}\n')
productos2 = [producto3, producto4]
orden2 = Orden(productos2)
orden2.agregar_producto(producto6)
orden2.agregar_producto(producto5)
print(orden2)
print(f'Total de la Orden2: {orden2.calculo_total()}')