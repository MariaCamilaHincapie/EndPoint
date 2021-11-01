from Tienda_de_Maquillaje.maquillaje import Labial
from Tienda_de_Maquillaje.inventario import Inventario
inventario = Inventario()

if __name__ == '__main__':
    marca = str(input('Ingrese la marca: '))
    color = str(input('Ingrese el color: '))

    labial = Labial(marca, color)

    inventario.agregar_Labial(labial)
    result = inventario.buscar(123, marca, color)
    print(list(result))
    inventario.agregar_Labial('BASE')
    print(inventario.labiales)
