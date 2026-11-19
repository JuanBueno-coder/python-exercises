

from fabrica.Pieza import Pieza


class PiezaPlastico(Pieza):
    def __init__(self, idPieza, peso, precio, urlFabricante, resistencia):
        super().__init__(idPieza, peso, precio, urlFabricante)
        self.__resistencia =resistencia
    @property
    def resistencia(self):
        return self.__resistencia
    def __str__(self):
        return super().__str__() + f" {self.__resistencia}"
    