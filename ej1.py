import random
import sys
numeroaleatorio = random.randrange(10);
print ("Hola chaval vamos a adivinar un número del 1 al 10, va que tu eres tela de listo");

print("Vale esta primera vez no te doy pistas que si no es muy facil, va dime un numerin y pulsa enter")
for i in range(3):
    try:
        numerointento =int(input())
        if numeroaleatorio == numerointento:
            print("dios eres como super inteligente, guapo y listo")
            sys.exit()
        elif numeroaleatorio > numerointento:
            print("mira al menos ya sabemos que hay dos cosas pequeñas el numero que has dicho y... bueno tu intentalo otra vez")
        elif numeroaleatorio < numerointento:
            print("Piensas en cosas grandes, piensa en cosas mas chicas")
    except ValueError:
        print("Eso no era un numero genio")
print("nada no lo adivinaste que malo eres")
sys.exit()