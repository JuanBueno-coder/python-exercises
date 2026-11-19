# 1.  Pide nombre y edad con input y muestra Juan tendrá 30 años en 2036 usando un f-string. Ojo: input siempre devuelve texto.
# 2.  Muestra en una sola línea los múltiplos de 7 entre 1 y 50, separados por espacios. Pista: range(7, 51, 7) y print(x, end=" ").
# 3.  Pide números hasta que el usuario escriba x y muestra la suma. El while con centinela es igual que en Java, pero sin llaves ni paréntesis.


#1.
#----------------------------------------------------------------------------------#
nombre=input("Dame el nombre \n")
edad=int(input("Dame tu edad "))

texto =f"{nombre} tendrá {edad+10} años en 2036"
print(texto)


#2.
#----------------------------------------------------------------------------------#
for x in range(7, 51, 7):
    print(x, end=" ")



#3.
#----------------------------------------------------------------------------------#
var=input("Dame un número, cuando quieras parar escribe x \n")
acumulador = 0
while var!="x":
    acumulador +=int(var)
    var=input("Dame un número, cuando quieras parar escribe x \n")
salida= f"pulsaste x hemos acumulado :{acumulador}"

print(salida)