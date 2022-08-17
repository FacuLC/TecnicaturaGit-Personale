# lista = Ariel, Liliana, Naty, Osvaldo

nombres = ["Naty", "Osvaldo", "Liliana", "Ariel"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[2])

# Si queremos saber el final de la lista
print(nombres[-1])

# Solo muestra el indice 0, 1 pero no el indice 2
print(nombres[0:2])

# Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])  # Indices a mostrar 0, 1, 2

# Desde el indicado hasta el final
print(nombres[1:])

# Modificamos un valor
nombres[2] = "Lili"
nombres [0] = "Natalia"
print(nombres)

# Iterar la lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print("Se terminaron los elemento de la lista")
print("")

# Preguntamos cuantos elementos tiene  una lista
print(len(nombres))# le pasamos como parametro la lista

# Agregamos un elemento
nombres.append("Facundo")
print(nombres)# Se agrega al final de la lista

# Insertar un elemento en un indice especifico
nombres.insert(1, "Leonel")# Primero indicamos la posicion, luego el nombre
print(nombres)

nombres.insert(3, "Cano")
print(nombres)

# Eliminamos un elemento
nombres.remove("Cano")
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indicde especifico
del nombres[2]# del= es eliminar
print(nombres)

# Eliminar todos los elementos de la lista
nombres.clear()
print(nombres)

# Eliminar toda la lista
del nombres
print(nombres)
