class Producto:
    pass

class Pan_sin_Gluten(Producto):

    def __init__(self, nombre = 'Pan sin Gluten', precio = 1000,
                 numProdcuto = 1, *args, **kargs):
        self.nombre = nombre
        self.precio = precio
        self.numProducto = numProdcuto

    def __str__(self):
        return f"{self.numProducto}--{self.nombre}--{self.precio}"

    def __repr__(self):
        return 'Soy un pan'





