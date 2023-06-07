class MiClase:

    # Este atributo de clase dara a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia):#La variable instancia otorga diferentes valores
        self.variable_instancia = variable_instancia

print(MiClase.variable_clase)

miClase1 = MiClase('Es es una variable de Intancia')

print(miClase1.variable_instancia)

print(miClase1.variable_clase)

miClase2 = MiClase('Esta es otra prueba de variable de instancia')

print(miClase2.variable_instancia)
print(miClase2.variable_clase)