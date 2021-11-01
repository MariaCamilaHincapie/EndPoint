import uuid
import pickle


class Mascota:
    pass

class Perro(Mascota):

    def __init__(self, raza, color, precio):
        self.codigo = uuid.uuid4()
        self.raza = raza
        self.color = color
        self.precio = precio

    def __str__(self):
        return f"{self.codigo}--{self.raza}--{self.color}"

    def __repr__(self):
        return str(self.codigo)

    def cumple(self, especificacion):
        dict_perro = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_perro or dict_perro[k] != especificacion.get_value(k):
                return False
        return True

    @classmethod
    def save(cls, perro):
        binary_open = open(str(perro.codigo) + '.per', mode='wb')
        pickle.dump(perro, binary_open)
        binary_open.close()