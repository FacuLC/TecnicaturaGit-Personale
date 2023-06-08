class Persona:  # Creamos una Clase o Plantilla

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Facundo', 'Cano', 21)  # Necesitamos enviar Argumentos

print(f'El Objeto de la calse persona : {persona1.nombre} {persona1.apellido} \nSu edad es : {persona1.edad}')

persona2 = Persona('Nicole', 'Sivitariale', 21)

print(f'\nEl Objeto de la clase persona : {persona2.nombre} {persona2.apellido} \nSu edad es: {persona2.edad}')

# Editando el objeto1 de la calse Persona

persona1.nombre = 'Ariel'
persona1.apellido = 'Franco'
persona1.edad = 20

print(
    f'\nEl objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} \nSu edad es: {persona1.edad}')

# Los Atributos son: caracteristicas
# Los Metodos son: El comportamiento que va a tener los objetos (acciones)
persona1.mostrar_detalle() # La referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

# Persona.mostrar_detalle() # Debemos pasarle una referencia para el self o dara error

Persona.mostrar_detalle(persona1)



# CLASE 9 (CREAR UN ATRIBUTO DESDE UN OBJETO)

persona1.telefono = '448462748'
print(f'Este es el telefono de: {persona1.nombre} - {persona1.telefono}')# Hemos creado un atributo de un objeto

# print(persona2.telefono) - El objeto persona2 no tiene este atributo, da error

