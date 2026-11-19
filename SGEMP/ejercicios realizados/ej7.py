print("dame tu nota a ver si estas aprovado chaval")
nota =float(input())
if nota<5.0:
    print("Estas suspenso chaval")
elif nota<7:
    print("Estas aprovado chaval")
elif nota<9:
    print("Tienes un notable chaval")
elif nota<10:
    print("Tienes un sobresaliente chaval")
elif nota == 10:
    print("Tienes matricula")
else:
    print("Expresion no valida")
