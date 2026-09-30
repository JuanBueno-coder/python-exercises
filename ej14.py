#generar la constante de pi
target =int(input("¿Cuantos terminos bb?"))

variabletemp=1

for i in range(1, target + 1):
    variabletemp *= (2 * i) / (2 * i - 1)
    variabletemp *= (2 * i) / (2 * i + 1)
print(2*variabletemp)