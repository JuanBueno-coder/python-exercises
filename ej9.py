print("dame el numero de mes y te digo cuantos dias tiene va")
num_mes = int(input())
if num_mes%2 ==0 and num_mes !=2:
    print("este mes tiene 31 dias")
elif num_mes%2 !=0:
    print("este mes tiene 30 dias")
else:
    print("Este mes tiene 28 dias")