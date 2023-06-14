class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f'Nombre del empleado: {self.nombre}, Sueldo: {self.sueldo}'
