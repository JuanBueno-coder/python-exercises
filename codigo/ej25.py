vector_t1 =[1.0, 2.0, 3.0]
vector_t2 =[4.0, 5.0, 6.0]
# ------------------suma ------------------------
suma = 0
for num in vector_t1:
    suma += num
print(suma)

# ------------------PRODUCTO ESCALAR------------------------

acumulador= 0

for i in range(len(vector_t1)):
    acumulador += vector_t1[i]*vector_t2[i]
print (acumulador)

# ------------------MAXIMO y MINIMO------------------------

print(f"Minimo del vector_t1  {min(vector_t1)}")
print(f"Maximo del vector_t1  {max(vector_t1)}")

# ------------------INVERTIR LISTA------------------------

#CREANDO UNA NUEVA
lista_invertida = vector_t1[::-1]
print(f"Lista_invertida  {lista_invertida}")

# ------------------SUMA DE ELEMENTOS K EN MATRIZ NXN ------------------------
suma = 0
M = [
    [1.5, 2.0, 3.5],  # Fila 0
    [4.0, 5.5, 6.0],  # Fila 1
    [7.5, 8.0, 9.5]   # Fila 2
]
for j in range (2):
    suma +=M[2][j]

print(suma)

#esto suma la SEGUNDA fila 

# ------------------BUSCADOR ------------------------

def buscador(num_busc, array):
    for i in range(len(array)):
        if num_busc ==array[i]:
            return True, i
        
print(buscador(5.0, vector_t2))
#--------------COMPROBAR ORDENADO--------------------
if vector_t1.sort:
    print("esta ordenado")
else:
    print("No esta ordenado")

#--------------BUSCAR UN VALOR EN UNA MATRIZ(9) --------------------
k = [
    [1.5, 2.0, 3.5],  # Fila 0
    [4.0, 5.5, 6.0],  # Fila 1
    [7.5, 8.0, 9.5]   # Fila 2
]
exito= False
p = -1
q = -1
busco = 1.5
for i in range(len(k)):
    for j in range(len(k[i])):
        if busco ==k[i][j]:
            p = i 
            q = j
            exito = True
            break
    if exito:
        break
if not exito:
    print("No se ha encontrado")
else:
    print(f"Se ha encontrado en {p} , {q}")
#--------------CREAR UNA MATRIZ TRANSPUESTA (10) --------------------
n = int(input("Introduce el tamaño de la matriz NxN: "))

m = []

# Leer la matriz
for i in range(n):
    fila = []
    for j in range(n):
        valor = float(input(f"Introduce m[{i}][{j}]: "))
        fila.append(valor)
    m.append(fila)

# Calcular la traspuesta respecto a la diagonal principal
for i in range(n):
    for j in range(i + 1, n):
        m[i][j], m[j][i] = m[j][i], m[i][j]

# Mostrar la matriz traspuesta
print("Matriz traspuesta:")
for fila in m:
    print(fila)