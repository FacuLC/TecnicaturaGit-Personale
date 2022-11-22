class Aritmetica:
    """
    El nombre de este tipode comentario es : DocString
    esto es documentacion de la calse en phyton
    Vamos a hacer es esta calse algunas operaciones de : suma, resta, multiplicacion y mas
    """

    def __init__(self, numeroA, numeroB):
        self.numeroA = numeroA
        self.numeroB = numeroB

    # Metodo para sumar
    def sumar(self):
        return self.numeroA + self.numeroB

    # Metodo para restar
    def resta(self):
        return self.numeroA - self.numeroB

    # Metodo para multiplicacion
    def multi(self):
        return self.numeroA * self.numeroB

    # Metodo para dividir
    def dividir(self):
        return self.numeroA / self.numeroB

# Metodo Suma
aritmetica1 = Aritmetica(7, 9)  # Le pasamos los argumentos para los operadores
print(f'La suma de los numeros es: {aritmetica1.sumar()}')

# Metodo Resta
aritmetica1 = Aritmetica(9, 6)
print(f'La resta de los numeros es: {aritmetica1.resta()}')

# Metodo Multi.
aritmetica1 = Aritmetica(3, 4)
print(f'La multiplicacion de los numeros es: {aritmetica1.multi()}')

# Metodo Dividir
aritmetica1 = Aritmetica(10, 2)
print(f'La divicion de los numeros es : {aritmetica1.dividir():.2f}')