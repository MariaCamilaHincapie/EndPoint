import pickle
import jsonpickle
import sqlite3
from Tienda_de_Mascotas.Dominio.mascota import Perro
class PersistenciaPerro():

    def connect(self):
        self.con = sqlite3.connect("tienda_de_mascotas_huellitas.sqlite")
        self.__crear_tabla()

    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE PERRO(codigo text primary key,"\
                    "raza text, color text, precio float)"
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_perro(self, perro : Perro):
        cursor = self.con.cursor()
        query = "insert into PERRO(codigo," \
                "raza, color, precio)  values(" \
                f" ?,?,?,?)"
        cursor.execute(query,(str(perro.codigo),perro.raza,perro.color,
                              perro.precio))
        self.con.commit()


    @classmethod
    def save(cls, perro):
        binary_open = open("Files/" + str(perro.codigo) + '.per', mode='wb')
        pickle.dump(perro, binary_open)
        binary_open.close()

    @classmethod
    def load(cls, file_name):
        binary_open = open("Files/" + file_name, mode='rb')
        perro = pickle.load(binary_open)
        binary_open.close()
        return perro

    @classmethod
    def save_json(cls, perro):
        text_open = open("Files/" + str(perro.codigo) + '.json', mode='w')
        json_per = jsonpickle.encode(perro)
        text_open.write(json_per)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("Files/" + file_name, mode='r')
        json_per = text_open.readline()
        perro = jsonpickle.decode(json_per)
        text_open.close()
        return perro


