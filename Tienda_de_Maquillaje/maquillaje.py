class Maquillaje:
    pass

class Labial(Maquillaje):

    def __init__(self, marca, color):
        self.serial = 123
        self.marca = marca
        self.color = color

    def __str__(self):
        return f"{self.serial}--{self.marca}--{self.color}"

    def __repr__(self):
        return 'Soy un labial'

    def buscar(self, serial):
        return None
