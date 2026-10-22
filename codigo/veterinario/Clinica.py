from veterinario.Gato import Gato
from veterinario.Perro import Perro

class Clinica:
    def __init__(self):
        self.__mascotas = []

    @property
    def mascotas(self):
        return self.__mascotas

    def altaMascota(self, oMascota):
        if oMascota in self.__mascotas:
            return "Mascota repetida"
        else:
            self.__mascotas.append(oMascota)
            return "Alta OK"

    def bajaMascota(self,idMascota):
        for mascota in self.__mascotas:
            if idMascota == mascota.idMascota:
                self.__mascotas.remove(mascota)
                return "Mascota dada de baja"
        return "Mascota no localizada"

    def pesoMaximoGato(self):
        maximo = 0
        for mascota in self.__mascotas:
            if isinstance(mascota, Gato)and maximo< mascota.peso:
                maximo = mascota.peso
        return maximo