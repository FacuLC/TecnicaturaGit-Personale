class Persona:
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, objeto):
        self.objeto = objeto

    @staticmethod
    def meotodo_estatico():# Metodo estatico se asocia a la clase
        print(Persona.variable_clase)

    @classmethod
    def metodo_calse(cls):# el (cls) es una referencia a la clase
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_calse()
        self.meotodo_estatico()
        print(self.variable_clase)
        print(self.objeto)

print(Persona.variable_clase)

persona1 = Persona('\nEsta es una variable de objeto')
print(persona1.objeto)
print(persona1.variable_clase)

persona2 = Persona('Otra Variable de Objeto')
print(persona2.objeto)
print(persona2.variable_clase)

# Creamos otra variable de clase sin estar dentro de la calse Persona
Persona.variable_clase2 = 'Variable de clase Nueva'
print(Persona.variable_clase2)

# Ahora podemos llamarla desde los demas objetos
print(persona1.variable_clase2)
print(persona2.variable_clase2)

Persona.meotodo_estatico()

Persona.metodo_calse()

persona1.metodo_instancia()
