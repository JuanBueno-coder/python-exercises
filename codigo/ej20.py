num = 1
i= 1000
suma = 0

while num < i:
    if num%3 == 0 and num%7 == 0: 
        print(num)
        suma += num
    num+=1
print(suma)