


class Producto:
    def __init__(self, idProducto, nombre):
        self.__idProducto = idProducto
        self.__nombre = nombre
        self.__piezas = []

    
    @property
    def idProducto(self):
        return self.__idProducto
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def piezas(self):
        return self.__piezas

    def agregarPieza(self, oPieza):
        if oPieza in self.__piezas:
            return "Pieza repetida"
        else:
            self.__piezas.append(oPieza)
            return "Alta OK"
    
    def precioProducto(self):
        total =0 
        for pieza in self.__piezas:
            total += pieza.precio     
        return total

    def listadoPiezas(self):
        stringPiezas =""
        for pieza in self.__piezas:
            stringPiezas += str(pieza)+"\n"
        return stringPiezas
    
    def pesoProducto(self):
        total =0 
        for pieza in self.__piezas:
            total += pieza.peso    
        return total
    