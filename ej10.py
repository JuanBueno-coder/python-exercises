print("Dame un numero")

num=int(input())

if num<10:
    print("tiene una cifra")
elif num<100:
    print("tiene dos cifras")
elif num>99:
    print("tiene tres cifras o mas")