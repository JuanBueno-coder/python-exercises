from veterinario.Mascota import Mascota

class Perro(Mascota):
    def __init__(self, idMascota, peso, altura):
        super().__init__(idMascota, peso)
        self.__altura =altura
    @property
    def altura(self):
        return self.__altura
    def __str__(self):
        return super().__str__() + f" {self.__altura}"
    