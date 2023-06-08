# Argumentos, variables en funciones
def lista_nombres(*nombres): # Hacemos eso cuando no sabes la cantidad de elementos q va a recibir la funcion
    for nombre in nombres: # Se convierte en un tupla
        print(nombre)

lista_nombres('Lucas', 'Jose', 'Facundo', 'Renzo', 'Santiago')
lista_nombres('Marcos', 'Ezequiel', 'Veronica', 'Abrigail')