from dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):

    contador_teclado = 0

    def __init__(self, marca, tipoEntrada):
        Teclado.contador_teclado += 1
        self._id_teclado = Teclado.contador_teclado
        super().__init__(marca, tipoEntrada)

    def __str__(self):
        return f'Id: {self._id_teclado}, {super().__str__()}'
    

if __name__ == '__main__':
    teclado1 = Teclado('Noga', 'Usb')
    print(teclado1)