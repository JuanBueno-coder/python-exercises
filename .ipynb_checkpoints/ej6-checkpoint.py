print("dame tres numerines y veras que te los ordeno tela de bien")

num1=int(input())

numero_mayor = num1
numero_menor = num1

num2 = int(input())

if num2>num1:
    numero_mayor = num2
else:
    numero_menor = num2

num3 = int(input())

if num3>num1 and num3> num2:
    numero_mayor =num3
elif num3<num1 and num3< num2:
    numero_menor = num3
print("El numero mayor es " +str(numero_mayor) +" y el numero menor " +str(numero_menor))