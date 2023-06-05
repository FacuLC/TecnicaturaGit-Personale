# falto el profe y los pibes van a dar la calse

# pedir nombre y edad de los compañeros

def obtener_compañero(cantidad):
    compañeros = []
    for i in range(7):
        nombre = input('ingrese el nombre del compañero: ')
        edad = int(input('ingrese la edad del compañero: '))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])#(sort() es para ordenar)
    asistente = compañeros[0],[0]
    profesor = compañeros[-1]
    return asistente,profesor

asistente,profesor = obtener_compañero(5)

print(f'El profesor es: {profesor} y su asistente es: {asistente}')