"""PLANTILLA EJERCICIO 2: input -> lista de tuplas -> diccionario -> funcional SIN bucles -> fichero.
Probada con Python 3. En el apartado funcional: NI UN for/while (las comprensiones si valen)."""
from functools import reduce                       # reduce SIEMPRE hay que importarlo


# a) Pedir datos -> lista de tuplas
def entrada_datos():
    lista = []
    for i in range(3):                             # aqui SI se pueden usar bucles
        nombre = input(f"Nombre del equipo {i + 1}: ")
        favor = int(input("Puntos a favor: "))     # input devuelve str -> int()/float()
        contra = int(input("Puntos en contra: "))
        partidos = int(input("Partidos jugados: "))
        lista.append((nombre, favor, contra, partidos))   # doble parentesis = tupla
    print(lista)
    return lista


# b) Lista de tuplas -> diccionario {clave: (tupla de resultados)}
def calculo_estadisticas(lista_datos):
    d = {}
    for nombre, favor, contra, partidos in lista_datos:   # desempaquetado
        diferencia = favor - contra
        tasa = round(diferencia / partidos, 2)
        nivel = "Alta" if diferencia > 100 else "Media" if diferencia > 0 else "Baja"
        d[nombre] = (diferencia, tasa, nivel)
    return d


# c) FUNCIONAL: d.items() da tuplas (clave, valor) -> it[0] = clave, it[1] = valor
def extremos(d):
    mayor = reduce(lambda a, b: a if a[1][0] > b[1][0] else b, d.items())   # estilo del profe
    menor = min(d.items(), key=lambda it: it[1][0])                        # alternativa corta
    return [mayor[0], menor[0]]


def analizar(d):
    # 1. filtrar + transformar + ordenar
    altos = sorted([(k, v[0]) for k, v in d.items() if v[2] == "Alta"],
                   key=lambda t: t[1], reverse=True)
    # 2. media sin bucles
    media_tasa = round(sum(map(lambda v: v[1], d.values())) / len(d), 2)
    # 3. el maximo por un campo
    top = max(d.items(), key=lambda it: it[1][0])[0]
    # extra: filter + map -> tupla
    positivos = tuple(map(lambda it: it[0], filter(lambda it: it[1][0] > 0, d.items())))
    # extra: diccionario por comprension
    solo_dif = {k: v[0] for k, v in d.items()}
    return (altos, media_tasa, top, positivos, solo_dif)


# d) Guardar diccionario en CSV
def guardar_datos(d, fichero="baloncesto.csv"):
    with open(fichero, "w", encoding="utf-8") as f:     # se cierra solo
        for k, v in d.items():
            f.write(f"{k},{v[0]},{v[1]}\n")


# e) main
def main():
    # lista = entrada_datos()                           # en el examen, esta
    lista = [("Triana Heat", 780, 648, 10), ("ElCerro Bulls", 870, 710, 10),
             ("Bami Nuggets", 580, 950, 10)]           # datos fijos para probar rapido
    d = calculo_estadisticas(lista)
    print(d)
    print(extremos(d))
    print(analizar(d))
    guardar_datos(d)


if __name__ == "__main__":
    main()
