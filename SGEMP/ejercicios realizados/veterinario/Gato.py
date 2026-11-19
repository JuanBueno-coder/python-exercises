from veterinario.Mascota import Mascota

class Gato(Mascota):
    def __init__(self, idMascota, peso, raza):
        super().__init__(idMascota, peso)
        self.__raza =raza
    @property
    def raza(self):
        return self.__raza
    def __str__(self):
        return super().__str__() + f" {self.__raza}"
    