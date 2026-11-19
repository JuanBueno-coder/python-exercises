print("Dame 2 numeritos y veras la magia que puedo hacer con ellos")
a = int(input())
print("Primer número introducido buen chico falta el segundo")
b = int(input())
print("Ahora viene lo guapo decidir que quieres hacer: \n " \
"1: sumar los dos numerines\n" \
"2: restar los dos numerines \n" \
"3: multiplicar los dos números \n" \
"4: dividir los dos  números")
opcion =int(input())
match opcion:
    case 1:
        print("Has seleccionado sumar")
        print("El resultado es "+str(a+b))
    case 2:
        print("Has seleccionado restar")
        print("El resultado es "+str(a-b))
    case 3:
        print("Has seleccionado multiplicar")
        print("El resultado es "+str(a*b))
    case 4:
        print("Has seleccionado dividir")
        print("El resultado es "+str(a/b))
    case _:
        print("Valor no valido adios")