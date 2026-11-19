# De un operario se conoce su sueldo y los años de antigüedad. Escriba un programa que lea los
# datos de un trabajador, en concreto su sueldo actual y su antigüedad. A partir de estos datos el
# programa deberá calcular el nuevo sueldo que le corresponde según los siguientes criterios:

# a) Si el sueldo es inferior a 1500 y su antigüedad es igual o superior a 10 años, otorgarle
# un aumento del 20 %, mostrar el sueldo a pagar.

# b) Si el sueldo es inferior a 1500 pero su antigüedad es menor a 10 años, otorgarle un
# aumento de 5 %.

# c) Si el sueldo es mayor o igual a 1500 mostrar el sueldo en la página sin cambios

print("Bienvenido al programa de nominas automaticas")

print("Dime tu sueldo actual")
sueldo_actual =int(input())

print("Dime tu antiguedad en años")
antiguedad = int(input())

if sueldo_actual<1500 and antiguedad>=10:
    sueldo_nuevo =sueldo_actual*1.20

elif sueldo_actual<1500 and antiguedad<10:
    sueldo_nuevo =sueldo_actual*1.05

elif sueldo_actual>=1500:
    sueldo_nuevo = sueldo_actual
print(f"Tu sueldo nuevo es {sueldo_nuevo}")