# Escriba un programa que calcule y muestre por pantalla la descomposición en factores de un
# número introducido por el usuario. 

num =int(input("Dame un numerin  bb"))

factores = []
divisor = 2

while num>1:
    while num % divisor ==0:
        factores.append(divisor)
        num//=divisor
    divisor +=1
print(factores)
