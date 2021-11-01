from Panaderia_Vegana.producto import Pan_sin_Gluten
from Panaderia_Vegana.almacen import Almacen
almacen = Almacen()

if __name__== '__main__':
    nombre = str(input('Pan de Gluten'))
    numProducto = int(input('numProducto'))


    pan_sin_gluten = Pan_sin_Gluten(nombre , 1000, 1)

    almacen.agregarPan_sin_Gluten(pan_sin_gluten)
    result= almacen.buscar(numProducto, nombre)
    print(list(result))
    almacen.agregarPan_sin_Gluten('Pan de Arroz')
    print(almacen.productos)
