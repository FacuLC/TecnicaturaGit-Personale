def bienvenida(nombre, genero):
   genero = genero.lower()
   if genero == 'hombre':
      return 'Hola '+nombre+', Bienvenido Craken'
   elif genero == 'mujer':
      return 'Hola '+nombre+', Bienvenida Reina'
   else:
      return 'ERROR AL INGRESAR EL LOS DATOS'
    
print(bienvenida('Facundo', 'HomBre'))
print(bienvenida('Erika', 'MuJer'))
print(bienvenida('Facundo', 'Hom'))