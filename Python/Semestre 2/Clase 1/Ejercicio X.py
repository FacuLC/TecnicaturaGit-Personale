class Persona: # Creamos la Clase
    def __init__(self, nombre, apellido, edad): # parametros default self
        self.nombre = nombre # init es un metodo especial dunder
        self.apellido = apellido
        self.edad = edad # Son atributos de metodo

    def mostrar_detalles(self):
        print(f'persona:{self.nombre}{self.apellido}{self.edad}')

persona1 = Persona('Facundo', 'Cano', 21)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Nicole','Flores', 21)
print(f'El objeto de la calse : {persona2.nombre}{persona2.apellido} y su edad es{persona2.edad}')
persona1.mostrar_detalles()
persona2.mostrar_detalles()
