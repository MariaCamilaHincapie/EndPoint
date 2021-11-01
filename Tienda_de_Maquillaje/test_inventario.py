from Tienda_de_Maquillaje.maquillaje import Labial
from Tienda_de_Maquillaje.inventario import Inventario

def test_buscar():
    marcas = ['Avon', 'Nivea']
    colores = ['Rojo', 'Rosa', 'Crema']

    inventario = Inventario()
    for marca in marcas:
        for color in colores:
            inventario.agregar_Labial(
                Labial(marca, color)
            )
    assert True

if __name__ == '__main__':
    test_buscar()
