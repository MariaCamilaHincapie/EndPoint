from Tienda_de_Mascotas.Dominio.especificacionPerro import EspecificacionPerro
from Tienda_de_Mascotas.Dominio.mascota import Perro


class ListaMascotas():

    def __init__(self):
        self.perros = []

    def agregar_perro(self, perro):
        if type(perro) == Perro:
            espec = EspecificacionPerro()
            espec.agregar_parametro('codigo', perro.codigo)
            if len(list(self.buscar(espec))) == 0:
                self.perros.append(perro)
            else:
                raise Exception('Perro repetido')

    def buscar(self, raza):
        for p in self.perros:
            if p.raza == raza:
                yield p

    def buscar(self, especificacion):
        for p in self.perros:
            if p.cumple(especificacion):
                yield p
