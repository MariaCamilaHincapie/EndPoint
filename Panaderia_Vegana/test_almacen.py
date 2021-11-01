from Panaderia_Vegana.almacen import Almacen
from Panaderia_Vegana.producto import Pan_sin_Gluten

def test_buscar():
    almacen = Almacen()
    almacen.agregarPan_sin_Gluten(Pan_sin_Gluten('Pan de Gluten' , 1000, 1))
    assert True

if __name__ == '__main__':
    test_buscar()
