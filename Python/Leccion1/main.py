"""
miVariable = 3
print(miVariable)
miVariable = "Hola a todos los student de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(z)
print(id(x))
# Las literales se escriben x=152, la variable y =896 y la variable z=216
print(id(y))
print(id(z))

# Tipos int, float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola Alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de Cadenas

miGrupoFavorito = "Mirror Park:"
caracteristicas = "La mejor estacion de Radio"
print("Mi Grupo Favorito es:", miGrupoFavorito, caracteristicas)
# El simbolo "+" sirve para concatenar la varaible

# El Int sirve para transformar las variables de String a enteros y poder sumarlos
numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

# Tipos Booleanos (bool), (True) o (False)
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada de el usuario

# Funcion input
# Regresa un dato Tipo String
resultado = input("Digite un numero: ")
print(resultado)

# Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
"""
"""
OperandoA = 8
OperandoB = 5
suma = OperandoA + OperandoB
# print("El resultado de la suma es: ", suma)
print(f"El resultado de la suma es: {suma}")

resta = OperandoA - OperandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = OperandoA * OperandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

divicion = OperandoA / OperandoB
print(f"El resultado de la divicion es: {divicion}")
divicion = OperandoA // OperandoB  # Doble barra para q el resultado de la divicion sea entero
print(f"El resultado de la divicion es: {divicion}")
modulo_residuo = OperandoA % OperandoB
print(f"El resultado de la divicion o residuo (modulo) es: {modulo_residuo}")
exponente = OperandoA ** OperandoB
print(f"El resultado del exponente es: {exponente}")
"""
"""
altura = int(input("Digite la altura: "))
ancho = int(input("Digite el ancho: "))
area = altura * ancho
perimetro = (altura + ancho)*2

print(f"El area del rectangulo seria: {area}")
print(f"El perimetro de el rectangulo seria: {perimetro}")
"""
"""
miVariable3 = 10
print(miVariable3)

# Operadores de resignacion

miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 - 2

miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 * 3

miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable3 / 2

miVariable3 /= 2
print(miVariable3)

# Operadores de Comparacion

d = 4
b = 6
resultado = d == b  # Comprobamos si son iguales
print(resultado)

# Operador Diferente

resultado = d != b
print(resultado)

# Operador Mayor

resultado = d > b
print(resultado)

# Operador Menor

resultado = d < b
print(resultado)

# Operador Menor o Igual

resultado = d <= b
print(resultado)

# Operador Mayor o igual

resultado = d >= b
print(resultado)
"""

# Operadores Logicos

# Operador and
a = False
b = True
resultado = a and b
print(resultado)

# Operador or

resultado = a or b
print(resultado)

# Operador not

resultado = not a
print(resultado)