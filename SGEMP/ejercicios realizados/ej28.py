vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
lista = []

# 1. Lectura de datos
palabra = input("Dame una palabra, escribe 'fin' cuando no quieras introducir más: ")

while palabra.lower() != "fin":
    if palabra:  # Evita guardar cadenas vacías
        lista.append(palabra)
    palabra = input("Dame una palabra, escribe 'fin' cuando no quieras introducir más: ")

# 2. Mostrar la lista de palabras introducidas
print("\nLista completa de palabras introducidas:")
print(lista)

lista_vocales = []
lista_consonantes = []

# 3. Clasificación y eliminación de duplicados
for palabra in lista:
    primera_letra = palabra[0]
    
    if primera_letra in vocales:
        if palabra not in lista_vocales:
            lista_vocales.append(palabra)
    elif primera_letra.isalpha():  # Asegura que comience por consonante
        if palabra not in lista_consonantes:
            lista_consonantes.append(palabra)


tupla_consonantes = tuple(lista_consonantes)

print("\nPalabras que empiezan por vocal (sin duplicados):")
print(lista_vocales)

print("\nTupla de palabras que empiezan por consonante (sin duplicados):")
print(tupla_consonantes)
