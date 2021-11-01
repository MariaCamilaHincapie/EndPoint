from Panaderia_Vegana.producto import Pan_sin_Gluten

class Almacen():

    def __init__(self):
        self.productos = []

    def agregarPan_sin_Gluten(self, pan):
        if type(pan) == Pan_sin_Gluten:
            self.productos.append(pan)

    def buscar(self, nombre):
        for p in self.productos:
            if p.nombre == nombre:
                yield p

    def buscar(self, numProducto, nombre):
        for p in self.productos:
            if p.numProducto == numProducto and p.nombre == nombre:
                yield p
