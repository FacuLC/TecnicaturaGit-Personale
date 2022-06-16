# Ciclo While (Mientras o durante)
"""
contador = 0
while contador < 78:
    print("Ejecutamos nuestro ciclo while ", + contador)
    contador += 1
else:
    print("Fin del ciclo while")
"""
# Imprimir numeros del 0 al 5 con el ciclo while

"""
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1
"""

"""
minimo = 0
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1
"""
"""

# Ciclo for

cadena = "Hola"
for letra in cadena:
    print(letra)
else:
    print("Fin del ciclo for")
"""
"""

# Palabra reservada Break
for letra in "Argentina Campeon":
    if letra == "a":
        print(f"Letra encontrada: {letra}")
        break
else:
    print("Fin del ciclo for")

"""

# Palabra reservada continue
for i in range(6):
    if i % 2 == 0:
        print(f"Valor: {i}")

for i in range(6):
    if i % 2 != 0:
        continue
    print(f"Valor: {i}")