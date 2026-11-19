class Mascota:
    def __init__(self, idMascota, peso):
        self.__idMascota = idMascota
        self.__peso = peso
    def __str__(self):
        return f"{self.__idMascota} {self.__peso}"
    @property
    def idMascota(self):
        return self.__idMascota
    @property
    def peso(self):
        return self.__peso
        