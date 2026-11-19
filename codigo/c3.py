# 1.  stock = {"serranito": 10, "pringá": 4}: añade una clave, modifica otra, borra una con del, usa stock.get("pavo", 0) y comprueba con in.
# 2.  Cuenta las palabras de "el que no tiene de inga tiene de mandinga, el que no" quitando la coma. Esperado: {'el': 2, 'que': 2, 'no': 2, 'tiene': 2, 'de': 2, 'inga': 1, 'mandinga': 1}. Pista: d[p] = d.get(p, 0) + 1.
# 3.  Convierte ventas = [("Serranito", 3.5, 25), ("Pringá", 2.8, 32), ("Espinacas", 3.0, 12), ("Solomillo", 4.2, 18)] en {nombre: (total, popularidad)} con Alta si cantidad > 25, Media si > 15 y Baja en otro caso. Esperado: {'Serranito': (87.5, 'Media'), 'Pringá': (89.6, 'Alta'), 'Espinacas': (36.0, 'Baja'), 'Solomillo': (75.6, 'Media')}. Fíjate en que 25 da Media y en que hace falta round.
# 4.  Recorre un diccionario de diccionarios: {1: {"nombre": "Ana", "mesa": 5}, 2: {"nombre": "Luis", "mesa": 3}} y muestra Mesa 5: Ana.

#1.
#----------------------------------------------------------------------------------#
stock = {"serranito": 10, "pringá": 4}
stock["aceitunas"] = 20 #añadir items diccionario
print(stock)

stock["serranito"] = 100
print(stock)
del stock["aceitunas"]
print(stock)
print(stock.get("pavo",0))
print("serranito" in stock)

#2.
#----------------------------------------------------------------------------------#
diccionario = {}
frase ="el que no tiene de inga tiene de mandinga, el que no"
# Quitamos la coma y separamos por espacios
palabras = frase.replace(",", "").split()

diccionario = {}
for p in palabras:
    diccionario[p] = diccionario.get(p, 0) + 1
print(diccionario)
#3.
#----------------------------------------------------------------------------------#
ventas = [("Serranito", 3.5, 25), ("Pringá", 2.8, 32), ("Espinacas", 3.0, 12), ("Solomillo", 4.2, 18)]
d = {}
for nombre, precio, cantidad in ventas:
    total =round(precio*cantidad, 2)
    if cantidad > 25:
        popularidad = "Alta"
    elif cantidad > 15:
        popularidad = "Media"
    else:
        popularidad = "Baja"
    d[nombre]=(total, popularidad)
print(d)

#4.
#----------------------------------------------------------------------------------#

d= {1: {"nombre": "Ana", "mesa": 5}, 2: {"nombre": "Luis", "mesa": 3}}

for k, v in d.items():
    print(f"Mesa {v['mesa']}: {v['nombre']}")
    








