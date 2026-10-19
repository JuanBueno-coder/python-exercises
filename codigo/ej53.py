class Producto:
    idProducto = "0000000"

    nombre = "Pieza"

    piezas = listpiezas


    

    def __init__(self, idProducto, nombre, piezas):
        self._idProducto = idProducto
        self._nombre = nombre
        self._piezas = piezas

    def agregarPieza(self, Pieza):
        print(Pieza)

    def precioProducto(self, precio float):
