
VOCALES = set("aeiou")

total_vocales = 0
total_no_vocales = 0

entrada = input("¿Me das una letra bb?")




while entrada!= " ":
    print("es una letra ")

    if entrada in VOCALES:
        print ("Es vocal")
        total_vocales +=1
    else:
        print ("Es no vocal")
        total_no_vocales +=1
    entrada = input("¿Me das una letra bb?")

print("total vocales = " .total_vocales)

print("total no vocales = " .total_no_vocales)