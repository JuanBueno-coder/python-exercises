from fabrica.Producto import Producto
from fabrica.PiezaMetalica import PiezaMetalica
from fabrica.PiezaPlastico import PiezaPlastico


palaExcabadora = PiezaPlastico("3728d",324, 32.32, "juanbueno.com", 100)
excabadora = Producto(123123, "excabadora")
medidorAire = PiezaMetalica("239832d", 42421, 3213, "maria.com", "adamantio")
print(excabadora.agregarPieza(palaExcabadora))
print(excabadora.agregarPieza(medidorAire))
print(excabadora.listadoPiezas())
print(excabadora.precioProducto())
print(excabadora.pesoProducto())
print(excabadora.agregarPieza(palaExcabadora))