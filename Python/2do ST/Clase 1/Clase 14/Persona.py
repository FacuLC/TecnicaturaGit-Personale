class Persona:
    contador_personas = 0 # Variable de Clases


    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_personas = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad


    def __str__(self):
        return f'Persona[: {self.id_personas}, Nombre: {self.nombre}, Edad: {self.edad}]'

persona1 = Persona('Facundo', 22)
print(persona1)

persona2 = Persona('Lucas', 32)
print(persona2)

persona3 = Persona('Ariel', 52)
print(persona3)

Persona.generar_siguiente_valor() # al llamarlo sigue sumando
print(f'Valor del contador: {Persona.contador_personas}')