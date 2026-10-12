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