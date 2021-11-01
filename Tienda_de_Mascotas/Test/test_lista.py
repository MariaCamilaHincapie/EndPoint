from Tienda_de_Mascotas.Dominio.listaMascotas import ListaMascotas
from Tienda_de_Mascotas.Dominio.mascota import Perro
from Tienda_de_Mascotas.Dominio.especificacionPerro import EspecificacionPerro
import random


def test_buscar():
    razas = ['Beagle', 'Labrador', 'Criollo']
    colores = ['Blanco', 'Negro', 'Rubio', 'Bicolor', 'Tricolor']
    precios = [1000, 2000, 3000]

    lista = ListaMascotas()
    for raza in razas:
        for color in colores:
            for precio in precios:
                lista.agregar_perro(Perro(raza, precio))
    especificacion = EspecificacionPerro()
    especificacion.agregar_parametro('raza', 'Beagle')
    for perro in lista.buscar(especificacion):
        assert perro is not None
    assert len(list(lista.buscar(especificacion))) > 0


def test_fuzzing_buscar():
    razas = ['Beagle', 'Labrador', 'Criollo']
    colores = ['Castaño', 'Negro', 'Blanco', 'Mono', 'Bicolor', 'Tricolor']
    precios = [1000, 2000, 3000]
    cantidad_perros = random.randint(10, 100)
    lista = ListaMascotas()
    especificaciones = []
    for i in range(cantidad_perros):
        raza = random.choice(razas)
        color = random.choice(colores)
        precio = random.choice(precios)
        especificacion = EspecificacionPerro()
        especificacion.agregar_parametro('raza', raza)
        especificacion.agregar_parametro('color', color)
        especificacion.agregar_parametro('precio', precio)
        especificaciones.append(especificacion)

        p = Perro(raza, color, precio)
        lista.agregar_perro(p)
    cantida_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantida_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(lista.buscar(esp))) > 0
        print('encontradas: ')
        print(list(lista.buscar(esp)))
    esp_fake = EspecificacionPerro()
    esp_fake.agregar_parametro('color_ojos', 'azules')
    print(lista.perros)
    assert len(list(lista.buscar(esp_fake))) == 0
    p = Perro(raza, color, precio)
    lista.agregar_perro(p)
    try:
        lista.agregar_perro(p)
        assert False
    except Exception as ex:
        assert ex


if __name__ == '__main__':
    test_fuzzing_buscar()
