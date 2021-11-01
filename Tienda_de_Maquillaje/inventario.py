from Tienda_de_Maquillaje.maquillaje import Labial

class Inventario():

    def __init__(self):
        self.labiales = []

    def agregar_Labial(self, labial):
        if type(labial) == Labial:
            self.labiales.append(labial)
            
    def buscar(self, serial, marca, color):
        for l in self.labiales:
            if l.serial == serial and l.marca == marca and l.color == color:
                yield l
