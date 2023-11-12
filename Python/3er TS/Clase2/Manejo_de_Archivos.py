# Declaramos una Variable
try:
    archivo = open('prueba.txt', 'w', encoding='UTF-8')  # La (w) es de write = escribir
    # El (encoding='UTF.-8') es para los acentos
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras \n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write('Las letras son: \nLa (r) es Read = Leer  \nLa (x) es para crear archivo \nLa (a) es append  \nLa (w) es Escribir')
    archivo.write('La (t) es para texto \nLa (b) es para archivos binarios')
    archivo.write('La (w+) es para leer y escribir\n')
    archivo.write('saludos a todos los alumnos de la tecnicatura\n')
    archivo.write('Con esto terminamos')
except Exception as error:
    print(error)
finally:  # Siempre se ejecuta
    archivo.close()  # Con esto se debe cerrar el archivo
#  archivo.write('Todo quedo Perfecto'): este es un error porque el archivo ya esta cerrado
