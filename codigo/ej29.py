print("hola")
lista_temporal =[]
for i in range(5):
    valor =int(input(f"Dame el dato {i+1} "))
    lista_temporal.append(valor)

mi_tupla = tuple(lista_temporal)#<------aqui creo tupla con valores del array una tupla no se puede modificar
print(mi_tupla)
lista_final= []
for j in mi_tupla:
    if j%2 ==0:
        tupla_par = (j, "par")
        lista_final.append(tupla_par)
    else:
        tupla_impar =(j, "impar")
        lista_final.append(tupla_impar)

print(lista_final)