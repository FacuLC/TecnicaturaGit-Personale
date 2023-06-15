from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    # print(objeto)  # De manera indirecta llama al __str__ de la clase Empleado o Gerente
    print(type(objeto))  # Esto es para saber el tipo de dato que recibe
    print(objeto.mostrar_detalles())  # Creamos un metodo para ver el interior del objeto
    if isinstance(objeto, Gerente):  # la funcion (isinstance) muestra una variable que no esta en otra clase
        print(objeto.departamento)


empleado1 = Empleado('Leonel', 100000.00)
imprimir_detalles(empleado1)

gerente1 = Gerente('Facundo', 30000, 'Sistemas')

imprimir_detalles(gerente1)
