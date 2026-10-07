DIAS_VALIDOS = ["lunes", "martes", "miércoles", "jueves", "viernes"]

guardias = {}

while len(guardias) < 5:
    nombre = input("Nombre del trabajador: ").lower()

    dia = input("Día de guardia (lunes a viernes): ").lower()

    if nombre in guardias:
    
        print("Echa el freno Madaleno ese trabajador ya está registrado. Entrada ignorada.")
    
    elif dia not in DIAS_VALIDOS:
        print("Día no válido.¿No seras tu un explotador? Entrada ignorada.")
    
    elif dia in guardias.values():
    
        print("Ese día ya está asignado.¿Te sobra gente o qué? Entrada ignorada.")
    
    else:
        guardias[nombre] = dia

print(guardias)