from math import sqrt
val_a=int(input("valor a"))
val_b=int(input("valor a"))
val_c=int(input("valor a"))

discriminante =val_b*val_b-4*val_a*val_c
if discriminante<0:
    print ("no hay solucion")
else:
    sol1 =(-val_b + sqrt(discriminante))/(2*val_a)
    sol2 =(-val_b - sqrt(discriminante))/(2*val_a)
    if sol1==sol2:
        print(sol1)
    else:
        print(sol1)
        print(sol2)
