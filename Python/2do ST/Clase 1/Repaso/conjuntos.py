#Creando un conjunto con set()
conjunto = set(['dato1', 'dato2']);

#Metiendo un Conjunto dentro de otro conjunto, utilizamos la funcion (frozenset) que nos permite unir conjuntos
conjunto1 = frozenset({'dato1', 'dato2'})
conjunto2 = {conjunto1,'dato3'}
print(conjunto2);

#Teoria de conjunto
conjunto1 = {1, 2, 3, 7}
conjunto2 = {1, 3, 7}

#como saber si es un sub-conjunto, utilizamos la funcion (.issubset) o (' <= ')
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= (conjunto1)

#como saber si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 >= conjunto1

#verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)#(Es True cuando son completamente destintos sino es False)

print(resultado)