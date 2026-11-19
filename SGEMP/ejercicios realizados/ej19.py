mayores_edad = 0
menores_edad = 0

for x in range(10):
  target =int(input("¿Me das tu edad bb?"))
  if target>=18:
    mayores_edad +=1
  else:
    menores_edad +=1
print("menores de edad: ". menores_edad)

print("mayores de edad: ". mayores_edad)
