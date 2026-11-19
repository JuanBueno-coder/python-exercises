# Datos: notas = [7, 4.5, 9, 3, 6, 8.5]

# 1.  Muestra la media, la máxima y la mínima sin bucles (sum, len, max, min). Esperado: 6.333333333333333 9 3.

# 2.  Lista de aprobados con comprensión: [7, 9, 6, 8.5]. Ordenada de mayor a menor: [9, 8.5, 7, 6, 4.5, 3].

# 3.  Slicing: las 3 primeras [7, 4.5, 9], las 2 últimas [6, 8.5] e invertida [8.5, 6, 3, 9, 4.5, 7].

# 4.  Función leer_productos() que pida 3 productos (nombre, precio, unidades) y devuelva una lista de tuplas: [('Pan', 1.2, 3), …]. Recorre luego la lista desempaquetando: for nombre, precio, uds in lista:.

# 5.  Crea una tupla de un solo elemento y comprueba con type() que lo es. Pista: lleva coma.

#1.
#----------------------------------------------------------------------------------#
notas = [7, 4.5, 9, 3, 6, 8.5]
suma = sum(notas)
items = len(notas)#items cuenta desde 1<--
maxima = max(notas)
minima = min(notas)
media = suma/items

salida= f"La media de notas es:{media}, la maxima es {maxima}, y la minima es {minima}"

print(salida)

#2.
#----------------------------------------------------------------------------------#



aprobados = [nota for nota in notas if nota >= 5]
print("Aprobados:", aprobados)
ordenadas = sorted(notas, reverse=True)
print("Ordenadas de mayor a menor:", ordenadas)




#3.
#----------------------------------------------------------------------------------#
# 3.  Slicing: las 3 primeras [7, 4.5, 9], las 2 últimas [6, 8.5] e invertida [8.5, 6, 3, 9, 4.5, 7].
notas = [7, 4.5, 9, 3, 6, 8.5]

corte1 =notas[:3]
corte2 = notas[-2:]
notasInvertidas = notas[::-1]
print(corte1)
print(corte2)
print(notasInvertidas)

#4.
#----------------------------------------------------------------------------------#

# 4.  Función leer_productos() que pida 3 productos (nombre, precio, unidades) y devuelva una lista de tuplas: [('Pan', 1.2, 3), …]. Recorre luego la lista desempaquetando: for nombre, precio, uds in lista:.

def leer_productos():
    listadetuplas =[]
    for i in range(3):
        nombre = input("Dame el nombre \n")
        precio = float(input("Dame el precio \n"))
        unidades = int(input("Dame el unidades \n"))
        listadetuplas.append((nombre, precio, unidades))
    

    return listadetuplas
lista=leer_productos()

for nombre, precio, unidades in lista:
    print(f"{nombre}: {precio:.2f} € x {unidades} unidades = {precio * unidades:.2f} €")

#----------------------------------------------------------------------------------#

# 5.  Crea una tupla de un solo elemento y comprueba con type() que lo es. Pista: lleva coma.

tupla_un_elemento = (5,)
print(type(tupla_un_elemento))







