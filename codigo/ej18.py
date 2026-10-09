n =int(input("Dame un numerin  bb"))
if n <= 1:
    print(False)
else:
    primo = True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            primo = False
            break
    print(primo)