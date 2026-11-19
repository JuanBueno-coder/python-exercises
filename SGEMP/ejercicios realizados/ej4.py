print("voy a formatearte la fecha \n dame el dia en numeros")

numero_dia=input()

print("Ahora dame el mes en numeros tambien")

numero_mes = int(input())

print("ahora dame el año en numeros tambien porfa")
numero_year = input()

match numero_mes:
    case 1: 
        print(numero_dia+" de Enero de "+numero_year)
    case 2: 
        print(numero_dia+" de Febrero de "+numero_year)
    case 3: 
        print(numero_dia+" de Marzo de "+numero_year)
    case 4: 
        print(numero_dia+" de Abril de "+numero_year)
    case 5: 
        print(numero_dia+" de Mayo de "+numero_year)
    case 6: 
        print(numero_dia+" de Junio de "+numero_year)
    case 7: 
        print(numero_dia+" de Julio de "+numero_year)
    case 8: 
        print(numero_dia+" de Agosto de "+numero_year)
    case 9: 
        print(numero_dia+" de Septiembre de "+numero_year)
    case 10: 
        print(numero_dia+" de Octubre de "+numero_year)
    case 11: 
        print(numero_dia+" de Noviembre de "+numero_year)
    case 12: 
        print(numero_dia+" de Diciembre de "+numero_year)
    case _:
        print("mes no valido")