num_positivos = 0
num_negativos = 0
suma_pos = 0
suma_neg = 0

for x in range(10):
    target = int(input("¿Me das un numerin bb? "))

    if target >= 0:
        num_positivos += 1
        suma_pos += target
    else:
        num_negativos += 1
        suma_neg += target

print("Suma números positivos:", suma_pos)

if num_positivos == 0:
    print("No hay números positivos")

if num_negativos == 0:
    print("No hay números negativos")
else:
    media = suma_neg / num_negativos
    
    print("Media números negativos:", media)