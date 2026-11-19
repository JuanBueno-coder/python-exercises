from functools import reduce

def leer_ventas_tapas():
    lista_de_tuplas = []
    for _ in range(4):
        nombre_tapa = input("Dame la tapa: \n")
        precio_unitario = float(input(f"Dame el precio de la tapa {nombre_tapa}: "))
        cantidad_vendida = int(input(f"Dame la cantidad vendida de {nombre_tapa}: "))
        lista_de_tuplas.append((nombre_tapa, precio_unitario, cantidad_vendida))
    return lista_de_tuplas


def calcular_estadisticas_tapas(lista_ventas):
    d = {}
    for tapa in lista_ventas:
        nombre = tapa[0]
        precio = tapa[1]
        cantidad = tapa[2]
        
        total_venta = precio * cantidad
        iva = total_venta * 0.1
        
        if cantidad > 25:
            popularidad = 'Alta'
        elif cantidad > 15:
            popularidad = 'Media'
        else:
            popularidad = 'Baja'
            
        d[nombre] = (total_venta, iva, popularidad)
        
    return d  

ventas = leer_ventas_tapas()
# Llamamos a la función usando la variable 'ventas'
diccionario_tapas = calcular_estadisticas_tapas(ventas)

print(diccionario_tapas)


def analizar_rendimiento_tapas(dic_estadisticas):
  if not dic_estadisticas:
    return [], 0.0, None

  # 1. Filtrar tapas con popularidad "Alta" (índice 2)
  def comprobar_tapa_alta(item_diccionario):
    return item_diccionario[1][2] == "Alta"

  tapas_alta_popularidad = list(
      filter(comprobar_tapa_alta, dic_estadisticas.items())
  )

  # 2. Calcular promedio del segundo valor (índice 1)
  def extraer_segundo_valor(item):
    return item[1][1]

  iva = sum(map(extraer_segundo_valor, dic_estadisticas.items())) / len(
      dic_estadisticas
  )
    def obtener_mayor_recaudacion(tapa1, tapa2):
  # tapa1 y tapa2 son tuplas (nombre_tapa, (recaudacion, iva, popularidad))
  # Comparamos el índice 0 de los datos (la recaudación)
      if tapa1[1][0] > tapa2[1][0]:
        return tapa1
      return tapa2

  # 3. Obtener el ítem con mayor recaudación (índice 0) usando el parámetro de la función
  mayor_recaudacion = reduce(
      lambda tapa1, tapa2: tapa1 if tapa1[1][0] > tapa2[1][0] else tapa2,
      dic_estadisticas.items(),
  )

  return (tapas_alta_popularidad, iva, mayor_recaudacion)


diccionario = {
    "Serranito": (87.5, 8.75, "Alta"),
    "Solomillo al whisky": (75.6, 7.56, "Media"),
    "Montadito de pringá": (89.6, 8.96, "Alta"),
    "Espinacas con garbanzos": (63.0, 6.3, "Media"),
}


resultado = analizar_rendimiento_tapas(diccionario)

print("Tapas alta popularidad:", resultado[0])
print("Promedio IVA:", resultado[1])
print("Mayor recaudación:", resultado[2])
diccionario = {'Serranito': (87.5, 8.75, 'Alta'),'Solomillo al whisky': (75.6, 7.56, 'Media'), 'Montadito de pringá': (89.6, 8.96, 'Alta'), 'Espinacas con garbanzos': (63.0, 6.3, 'Media') }
    