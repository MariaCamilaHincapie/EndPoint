import os
from Tienda_de_Mascotas.Dominio.mascota import Perro
from Tienda_de_Mascotas.Dominio.listaMascotas import ListaMascotas
from Tienda_de_Mascotas.Infraestructura.PersistenciaPerro import PersistenciaPerro

import random

lista = ListaMascotas()

if __name__== '__main__':

    saver = PersistenciaPerro()
    saver.connect()

    razas = ['Beagle', 'Labrador', 'Criollo']
    precios = [1000, 2000, 3000]
    colores = ['Castaño', 'Negro', 'Blanco', 'Mono', 'Bicolor', 'Tricolor']
    raza = random.choice(razas)
    color = random.choice(colores)
    precio = random.choice(precios)

    p = Perro(raza, color, precio)
    PersistenciaPerro.save(p)
    PersistenciaPerro.save_json(p)
    lista = ListaMascotas()
    lista_json = ListaMascotas()
    for file in os.listdir("./Files"):
        if '.per' in file:
            lista.agregar_perro(PersistenciaPerro.load(file))
        if '.json' in file:
            lista_json.agregar_perro(PersistenciaPerro.load_json(file))

    for p in lista.perros:
        saver.guardar_perro(p)
        PersistenciaPerro.save(p)
        PersistenciaPerro.save_json(p)
