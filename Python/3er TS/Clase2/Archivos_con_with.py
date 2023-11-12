from ManejoArchivos import Manejo

# Manejo de Contexto With
# with open('prueba.txt', 'r', encoding='utf8') as archivo:
    # print(archivo.read())
# Es un metodo el cual abre y cierra archivos de manera automatica
# No hace falta ni el try, ni el finally
# Utiliza diferentes metodos: __enter__ (este es el que abre)
# Ahora el siguiente metodo el que cierra: __exit__

with Manejo('prueba.txt') as archivo:
    print(archivo.read())
