#fuerza bruta
num1 =int(input("Dame un numerin  bb"))
num2 =int(input("Dame un numerin  bb"))
num3 =int(input("Dame un numerin  bb"))
num4 =int(input("Dame un numerin  bb"))
num5 =int(input("Dame un numerin  bb"))
num6 =int(input("Dame un numerin  bb"))


lista1 =[]  
lista2=[]

lista1.append(num1)
lista1.append(num2)
lista1.append(num3)

lista2.append(num4)
lista2.append(num5)
lista2.append(num6)
lista1.sort()
lista2.sort()
print(lista1)
print(lista2)
mi_tupla=(lista1,lista2)
print(mi_tupla)