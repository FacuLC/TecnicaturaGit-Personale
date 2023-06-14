class Producto:
    contador_productos = 0# Variable de clase

    @classmethod
    def generar_siguiente_producto(cls):
        cls.contador_productos += 1# Aumento para la variable de clase
        return cls.contador_productos

    def __init__(self, nombre, precio):
        self._id_producto = Producto.generar_siguiente_producto()# Asignacion de la variable de clase
        self._nombre = nombre
        self._precio = precio

    # Metodos getters y setters

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    # Sobre escribimos el metodo str
    def __str__(self):
        return f'ID del Producto: {self._id_producto}, Nombre del Producto: {self._nombre}, Precio:{self._precio}$'


if __name__ == '__main__':  # Solo sera visible si la prueba se ejecuta desde aqui
    producto1 = Producto('Camiseta', 100.00)
    producto2 = Producto('Pantalon', 150.00)
