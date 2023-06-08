class Rectangulo:
    def __init__(self, Altura, Base):
        self.Altura = Altura
        self.Base = Base

    def calculo(self):
        return self.Base * self.Altura

print('Ingrese la Medida de la base y la altura de 3 Rectangulos')
Base = float(input('\nDigite la Base del Primer Rectangulo -> '))
Altura = float(input('Digite la Altura del Primer Rectangulo -> '))
regtangulo1 = Rectangulo(Base, Altura)
print(f'El Area del Primer Regtangulo es -> {regtangulo1.calculo()}')

Base2 = float(input('\nDigite la Base del Segundo Rectangulo -> '))
Altura2 = float(input('Digite la Altura del Segundo Rectangulo -> '))
regtangulo2 = Rectangulo(Base2, Altura2)
print(f'El Area del Primer Regtangulo es -> {regtangulo2.calculo()}')

Base3 = float(input('\nDigite la Base del Tercer Rectangulo -> '))
Altura3 = float(input('Digite la Altura del Segundo Rectangulo -> '))
regtangulo3 = Rectangulo(Base3, Altura3)
print(f'El Area del Primer Regtangulo es -> {regtangulo3.calculo()}')
