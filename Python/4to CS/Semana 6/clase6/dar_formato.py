# dar formato a un string
nombre = 'Leonela'
edad = 29
mensaje_con_formato = 'Mi nombre es %s y tengo  %d años '% (nombre,edad)
#Creamos una tupla
persona =('Leonela','reyes',5000.00)
mensaje_con_formato = 'Hola %s %s . Tu sueldo es %.2f' # %persona # Aqui le pasamos el objeto que es tupla
#print(mensaje_con_formato % persona)

nombre = 'Juan'
edad = 19
sueldo = 3000
#mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre,edad,sueldo)
#print(mensaje_con_formato)
mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre,edad,sueldo)
print(mensaje)


#mensaje = 'nombre {n} Edad {e} sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
# print(mensaje)

diccionario = {'nombre': 'ivan', 'edad': 35, 'sueldo': 8000.00}

mensaje = 'Nombre: {dic[nombre]} Edad: {dic[edad]} Sueldo: {dic[sueldo]:.2f}'.format(dic=diccionario)
print(mensaje)