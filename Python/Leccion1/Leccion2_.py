"""
numero = int(input("Digite un numero: "))
cuenta = numero % 2==0
print(f"El residuo de la divicion es: {numero % 2}")
if cuenta:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es inpar")
"""
"""
# Ejercicio numero 2

numero1 = int(input("Digite su edad: "))
if numero1 >= 18:
    print(f"Usted tiene {numero1} es mayor de edad ")
else:
    print(f"Usted tiene {numero1} es menor de edad ")
"""

"""
# Ejercicio numero 4

numero3 = int(input("Digite un numero: "))
cuenta = numero3 >= 0 and numero3 <= 5
if cuenta:
    print(f"El numero {numero3} esta dentro de el rango.")
else:
    print(f"El numero {numero3} no esta dentro de el rango.")
"""

"""
# Ejercicio Numero 5

edad = int(input("Digite su edad: "))

if 20 <= edad <= 30:
    print(f"Usted tiene {edad} años y esta en un rango de edad entre 20 a 30 años")
else:
    print(f"Usted tiene {edad} años y no esta en un rango de edad de entre 20 a 30 años")

"""

"""
# Ejercicio Numero 6

numero4 = int(input("Digite un Numero: "))
numero5 = int(input("Digite un segundo Numero: "))

if numero4 > numero5:
    print(f"El numero mayor es: {numero4}")
    print(f"El numero menor es: {numero5}")
else:
    print(f"El numero mayor es: {numero5}")
    print(f"El numero menor es: {numero4}")
"""

# Ejercicio Numero 7

print("Ingrese los siguientes datos de el libro: ")

nombreL = input("Escriba un nombre para el libro: ")
Id = input("Ingrese un ID para el libro: ")
Precio = int(input("Ingrese el precio de el libro: "))
print(" ")
print("Titulo:",nombreL)
print("ID de el libro:",Id)
print("El precio:",Precio)
print(" ")
if Precio >= 500:
    print("El valor de el libro es de 500$ o mas, el envio sera gratis")
else:
    print("El valor de el libro no supera los 500$, el envio costara 300$")