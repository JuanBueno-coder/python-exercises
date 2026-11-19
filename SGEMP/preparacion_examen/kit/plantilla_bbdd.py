"""PLANTILLA BASE DE DATOS MySQL con pymysql (como el GitHub del profe).
Datos de conexion del entorno Docker de clase: host 'db', usuario 'root', clave 'test'.
Comprueba ANTES del examen que 'import pymysql' funciona: en el examen no hay internet para instalarlo."""
import pymysql

HOST, USUARIO, CLAVE, BD = "db", "root", "test", "examen"     # cambia BD segun el ejercicio


def get_connection():
    return pymysql.connect(host=HOST, user=USUARIO, password=CLAVE,
                           database=BD, port=3306)


# INSERT: %s como hueco SIEMPRE (nunca + ni f-strings en el SQL) y commit()
def insertar_reservas_bbdd(reservas):              # reservas = {id: {...}} del CSV
    conn = get_connection()
    cursor = conn.cursor()
    sql = ("INSERT INTO reserva (id, nombre_cliente, telefono, fecha_reserva, "
           "numero_personas, numero_mesa) VALUES (%s, %s, %s, %s, %s, %s)")
    insertadas = 0
    for id_r, r in reservas.items():
        try:
            cursor.execute(sql, (id_r, r["nombre"], r["telefono"], r["fecha"],
                                 r["personas"], r["mesa"]))
            insertadas += 1
        except pymysql.err.IntegrityError:         # clave primaria repetida -> seguimos
            print(f"La reserva {id_r} ya existia")
    conn.commit()                                  # SIN commit NO se guarda nada
    conn.close()
    return insertadas


# SELECT con parametro + salida "amigable" + totales
def mostrar_reservas_fecha(fecha):
    fecha = fecha.strip()                          # trampa del ' 2025-11-14'
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_cliente, telefono, numero_personas, numero_mesa "
                   "FROM reserva WHERE fecha_reserva = %s", (fecha,))   # (x,) tupla de 1
    filas = cursor.fetchall()                      # lista de tuplas
    conn.close()
    print(f"RESERVAS PARA {fecha}:")
    print("========================")
    total_personas = 0
    for nombre, tel, personas, mesa in filas:
        print(f"Mesa {mesa}: {nombre} ({personas} personas) - Tel: {tel}")
        total_personas += personas
    print(f"\nTotal: {len(filas)} reservas, {total_personas} personas\n")


# UPDATE / DELETE: rowcount = filas afectadas
def sumar_personas(id_reserva, cantidad):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE reserva SET numero_personas = numero_personas + %s "
                   "WHERE id = %s", (cantidad, id_reserva))
    afectadas = cursor.rowcount                    # 0 -> ese id no existe
    conn.commit()
    conn.close()
    return afectadas


def borrar_reservas_fecha(fecha):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reserva WHERE fecha_reserva = %s", (fecha,))
    borradas = cursor.rowcount
    conn.commit()
    conn.close()
    return borradas


# GROUP BY + BBDD -> diccionario (Decimal -> float, date -> str)
def personas_por_fecha():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT fecha_reserva, COUNT(*), SUM(numero_personas) "
                   "FROM reserva GROUP BY fecha_reserva ORDER BY fecha_reserva")
    d = {}
    for fecha, num, personas in cursor:            # el cursor tambien se puede recorrer
        d[str(fecha)] = (num, int(personas))       # SUM devuelve Decimal -> int()/float()
    conn.close()
    return d


# executemany: inserta una lista de tuplas de golpe
def insertar_lista(lista_tuplas):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO reserva VALUES (%s, %s, %s, %s, %s, %s)", lista_tuplas)
    conn.commit()
    conn.close()


def main():
    reservas = {1: {"nombre": "Ana García", "telefono": "611223344", "fecha": "2025-03-15",
                    "personas": 4, "mesa": 5},
                2: {"nombre": "Luis Martínez", "telefono": "622334455", "fecha": "2025-03-15",
                    "personas": 2, "mesa": 3}}
    print("Insertadas:", insertar_reservas_bbdd(reservas))
    print("Insertadas:", insertar_reservas_bbdd(reservas))      # 2a vez: 0, sin romper
    mostrar_reservas_fecha(" 2025-03-15")
    print("Actualizadas:", sumar_personas(1, 2), "| inexistente:", sumar_personas(999, 2))
    print(personas_por_fecha())
    print("Borradas:", borrar_reservas_fecha("2025-03-17"))


if __name__ == "__main__":
    main()
