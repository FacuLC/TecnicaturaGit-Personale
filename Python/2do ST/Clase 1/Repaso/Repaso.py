""""
# Ejercicio (Como Estuvo tu dia, Calificalo)
dia = int (input('Como estuvo su Dia?\nDenos una Calificacion del 1 al 10:\n'));
print(f'Mi Dia Estuvo de: {dia}');

# Ejercicio (Proporcione los datos para el siguiente libro)
titulo = input('\nProporcine el Titulo del Libro: ');
autor = input('Proporcione el Autor del Libro: ');

print(f'\nEl Titulo del Libro es: ({titulo}) y fue escripo por: ({autor})');
print('El autor del libor es: '+titulo+' y fue escrito por: '+autor);
"""

"""
# en las lista podes poder modificar los elementos
lista = ['Leo', 'Renzo', True, 1.78]

lista[1] = 'Santiago'
print(lista)

# en las tuplas no podemos modificar los elemntos
tupla = ('Leo', 'Renzo', True, 1.78)
# tupla[2] = 'Javier'
#print(tupla[2])

# Conjunto (set), (no se accede  a elementos por indice, no almacena elementos duplicados)

conjunto = {'Leo', 'Renzo', True, 1.78}
# print(conjunto[2]) -> No se puede acceder al elemento

# Creamos un Diccionario
diccionario = {
    'nombre':'Facundo Cano',
    'apellido':'Cano',
    'altura': 1.78,
    'telefono':'124424214'
}
print(diccionario['nombre'])
"""

"""
ingreso_mensual = 100000

if ingreso_mensual > 10000:
    print('Estas bine en cualquier parte del mundo')
elif ingreso_mensual > 1000:
    print('Etas bien en latino america')
else:
    print('Sos Pobre')
"""

cadena1 = 'Hola soy Facundo';


#convierte a mayusculas
mayusc = cadena1.upper()
print(mayusc)


#convierte a minusculas
minusc = cadena1.lower()
print(minusc)


#primera letra en mayuscula
primer_Mayus = cadena1.capitalize()
print(primer_Mayus)


# bucamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find('Hola')
print(busqueda_find)


#buscamos cuantas veces se repite algun valor
contra_Coincidencias = cadena1.count('a')
print(contra_Coincidencias)


#Contamos cuantos carcteres tiene una cadena
contra_Caracteres = len(cadena1)
print(contra_Caracteres)


#Verificamos con que inicia la cadena
inica_Con = cadena1.startswith('H')
print(inica_Con)


#Verificamos con que termina la cadena
termina_Con = cadena1.endswith('o')
print(termina_Con)


#remplaza un pedazo de la cadena por otra
remplaza_por = cadena1.replace('la soy', 'uoooo me presento soy')
print(remplaza_por)


#separar cadenas con la cadena que le pasemos
cadena_Sparada = cadena1.split(',')
print(cadena_Sparada[1])

