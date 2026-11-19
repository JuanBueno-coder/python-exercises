"""PLANTILLA FICHEROS DE TEXTO / CSV - probada con Python 3.
Regla de oro al leer: strip() -> split(sep) -> convertir tipos -> saltar cabecera y lineas vacias."""


# 1) CSV -> diccionario de diccionarios (examen 2025: reservas.csv)
def cargar_csv_dict(fichero="reservas.csv"):
    d = {}
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    for linea in lineas[1:]:                     # [1:] salta la cabecera
        linea = linea.strip()                    # quita \n y espacios
        if linea == "":                          # linea vacia al final -> fuera
            continue
        campos = linea.split(",")                # OJO: separador ; si el fichero usa ;
        d[int(campos[0])] = {
            "nombre": campos[1],
            "telefono": campos[2],               # telefono se queda como texto
            "fecha": campos[3],
            "personas": int(campos[4]),
            "mesa": int(campos[5]),
        }
    return d


# 2) CSV -> lista de tuplas
def cargar_csv_tuplas(fichero, sep=","):
    lista = []
    with open(fichero, encoding="utf-8") as f:
        next(f)                                  # otra forma de saltar la cabecera
        for linea in f:                          # recorrer el fichero linea a linea
            if linea.strip():
                c = linea.strip().split(sep)
                lista.append((int(c[0]), c[1], float(c[2])))
    return lista


# 3) Escribir (w = machaca, a = anade al final)
def guardar(d, fichero="salida.csv"):
    with open(fichero, "w", encoding="utf-8") as f:
        for k, v in d.items():
            f.write(f"{k},{v['nombre']},{v['personas']}\n")   # el \n lo pones tu


# 4) Fichero de numeros separados por ; en varias lineas (Boletin 46)
def estadisticas_numeros(fichero):
    numeros = []
    with open(fichero, encoding="utf-8") as f:
        for linea in f:
            if linea.strip():
                numeros += [float(x) for x in linea.strip().split(";")]
    return max(numeros), min(numeros), sum(numeros), sum(numeros) / len(numeros)


# 5) Contar palabras de un texto (Boletin 36 y 44)
def contar_palabras(texto):
    for signo in ".,:;!?¡¿":
        texto = texto.replace(signo, "")
    d = {}
    for p in texto.lower().split():              # split() sin argumento: por espacios
        d[p] = d.get(p, 0) + 1                   # get con valor por defecto
    return d


def main():
    reservas = cargar_csv_dict("../../Examen Python -14-11-2025/reservas.csv")
    print(reservas[1])
    guardar(reservas, "prueba_salida.csv")
    with open("prueba_numeros.txt", "w") as f:
        f.write("1.25;2.75;0.001;21\n3.45;4.52;12;-3.834\n7.1;-5.2;4.32;8.27\n")
    print(estadisticas_numeros("prueba_numeros.txt"))
    print(contar_palabras("De la mesa, de la silla. ¡De la casa!"))


if __name__ == "__main__":
    main()
