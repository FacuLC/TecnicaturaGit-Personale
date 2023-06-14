from Producto import Producto
class Orden:
    contador_ordenes = 0

    @classmethod
    def generar_siguinte_orden(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def __init__(self, productos):
        self._id_ordenes = Orden.generar_siguinte_orden()
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)# Esto es para agregar un nuevo producto

    def calculo_total(self):
        total = 0 # Variable temporal para almacenar el total temporal
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__()+' | '

        return f'Orden: {self._id_ordenes}, \nLista de los Productos: {productos_str}'


if __name__ == '__main__':

    producto1 = Producto('Camiseta', 100.00)
    print(producto1)
    producto2 = Producto('Pantalon', 150.00)
    print(producto2)

    productos1 = [producto1, producto2]# Creamos la listade productos
    orden1 = Orden(productos1)# Primer objeto orden pasado de la lista de productos
    print(orden1)


# Tarea: Modificar la orden2 ingresando nuevos productos con sus nombres y precios
# Crear una nueva lista de productos y agregar a la orden2

    #producto3 = Producto('Zapatillas Nike', 300.00)
    #producto4 = Producto('Buzo de Cuerdos', 250.00)
    #productos2 = [producto3, producto4]
    #orden2 = Orden(productos2)
    #print(orden2)
