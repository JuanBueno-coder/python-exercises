from fabrica.Pieza import Pieza

class PiezaMetalica(Pieza):
    def __init__(self, idPieza, peso, precio, urlFabricante, metal):
        super().__init__(idPieza, peso, precio, urlFabricante)
        self.__metal =metal
    @property
    def metal(self):
        return self.__metal
    def __str__(self):
        return super().__str__() + f" {self.__metal}"
    