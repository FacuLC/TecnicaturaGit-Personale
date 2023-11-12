archivo = open('prueba.txt', 'r',
               encoding='UTF-8')  # La (r) es Read = Leer / La (x) es para crear archivo / La (a) es append
#  print(archivo.read())
#  print(archivo.read(16))
#  print(archivo.read(10)) # continuamos desde la linea anterior
#  print(archivo.readline()) # sirve para ver la primera linea del archivo
#  print(archivo.readline())

#  vamos a iterar el archivo, cada una de las líneas

# for linea in archivo:
# print(linea): iteramos todos los elementos del archivo
# print(archivo.readlines()): nos muestra el archivo como si fuera una lista

# Anexamos informacion, copia a otro

archivo2 = open('copia.txt', 'w', encoding='utf-8')
archivo2.write(archivo.read())
archivo.close()  # cerramos el primer archivo
archivo2.close()  # cerramos el segundo archivo

print('Se ha terminado el proceso de leer y copiar archivos')
