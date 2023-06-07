class Persona:
    variable_clase = 'Esta es unavariable de clase'

    def __init__(self, objeto):
        self.objeto = objeto


print(Persona.variable_clase)

persona1 = Persona('\nEsta es una variable de objeto')
print(persona1.objeto)
print(persona1.variable_clase)

persona2 = Persona('Otra Variable de Objeto')
print(persona2.objeto)
print(persona2.variable_clase)
