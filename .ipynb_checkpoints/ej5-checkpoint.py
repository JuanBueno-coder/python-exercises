print("Introduce el año y yo te dire si es bisiesto")

num_usuario = int(input())

if num_usuario % 4== 0 and num_usuario<100:
    print("El año es bisiesto")
elif(num_usuario %100==0 and num_usuario%400==0):
    print("El año  es bisiesto")
else:
    print("El año no es bisiesto")