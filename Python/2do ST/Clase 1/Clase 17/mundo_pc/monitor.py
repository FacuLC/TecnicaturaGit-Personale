


class Monitor:

    contador_monitor = 0

    def __init__(self, marca, tamaño):
        Monitor.contador_monitor += 1
        self._id_monitor = Monitor.contador_monitor
        self._marca = marca
        self._tamaño = tamaño

    def __str__(self):
        return f"ID: {self._id_monitor}, Marca: {self._marca}, Tamaño de Monitor: {self._tamaño} Pulgadas"
    

if __name__ == "__main__":
    monitor1 = Monitor("LG", "17")
    print(monitor1)