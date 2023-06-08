class Cubo:
    def __init__(self, Ancho, Alto, Profundidad):
        self.Ancho = Ancho
        self.Alto = Alto
        self.Profundidad = Profundidad

    def calculo(self):
        return self.Ancho * self.Alto * self.Profundidad

print('Ingrese los Valores para Determinar el Volumen del Cubo')

Ancho = int(input('Digite el Ancho del Cubo -> '))
Alto = int(input('Digite la Altura del Cubo -> '))
Profundidad = int(input('Digite la Profundidad del Cubo -> '))

formula = Cubo(Ancho, Alto, Profundidad)
print(f'El volumen del Cubo es de -> {formula.calculo()}')