n = 3

m = []

# Leer la matriz
for i in range(n):
    fila = []
    for j in range(n):
        valor = float(input(f"Introduce m[{i}][{j}]: "))
        fila.append(valor)
    m.append(fila)

# Mostrar matriz
for fila in m:
    for valor in fila:
        print(valor, end="\t")  # Imprime elementos separados por tabulación
    print()