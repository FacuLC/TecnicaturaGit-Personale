class Persona:  # Esta Clase hereda de la calse object
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self):# Override = Sobrescribir
        return f'Persona: [Nombre: {self._nombre}, Edad: {self._edad}]'


class Empleado(Persona):  # Esta Clase es Hija de la Clase Persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Su sueldo :{self._sueldo}] {super().__str__()}'

    def mostrar_detalles(self):
        print('Datos Importantes'.center(50, '-'))
        print(f'Nombre -> {self._nombre}\nEdad -> {self._edad}\nSu Sueldo -> {self._sueldo}\n')


if __name__ == '__main__':
    empleado1 = Empleado('Facundo', 21, 7500)
    empleado1.mostrar_detalles()

    empleado2 = Empleado('Nicole', 21, 7000)
    empleado2.mostrar_detalles()
    empleado2.nombre = 'Celena'
    empleado2.edad = 22
    empleado2.sueldo = 5000
    empleado2.mostrar_detalles()
