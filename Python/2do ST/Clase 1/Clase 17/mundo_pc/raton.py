from dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipoEntrada):
        Raton.contador_ratones += 1  # Vamos sumando de a 1
        self._id_Raton = Raton.contador_ratones
        super().__init__(marca, tipoEntrada)

    def __str__(self):
        return f'Id: {self._id_Raton}, {super().__str__()}'


# Hacemos Pruebas

if __name__ == '__main__':
    raton1 = Raton('Usb', 'Reazer')
    print(raton1)