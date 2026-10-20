class Producto:
    def __init__(self, idProducto, nombre, piezas):
        self.__idProducto = idProducto
        self.__nombre = nombre
        self.__piezas = piezas

    def agregarPieza(self, oPieza):
        print(Pieza)

    
class Pieza:
    def __init__(self, idPieza, peso, precio, urlFabricante):
        self.__idPieza = idPieza
        self.__peso = peso
        self.__precio = precio
        self.__urlFabricante = urlFabricante
    def __str__(self):
        return f"{self.__idPieza} {self.__peso} {self.__precio} {self.__urlFabricante}"
    @property
    def idPieza(self):
        return self.__idPieza

    @property
    def peso(self):
        return self.__peso
    @property
    def precio(self):
        return self.__precio
    @property
    def urlFabricante(self):
        return self.__urlFabricante
p = Pieza("P1", 50, 2.5, "Ejemplo")

print(p.peso)