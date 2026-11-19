from functools import reduce


def analizar_rendimiento_tapas_lambda(dic_estadisticas):
  if not dic_estadisticas:
    return [], 0.0, None

  # Filtrar tapas con popularidad "Alta" (índice 2)
  tapas_alta_popularidad = list(
      filter(
          lambda tapa: tapa[1][2] == "Alta", dic_estadisticas.items()
      )
  )

  # Promedio del segundo valor / IVA (índice 1)
  iva = sum(
      map(lambda tapa: tapa[1][1], dic_estadisticas.items())
  ) / len(dic_estadisticas)

  # Tapa con mayor recaudación (índice 0)
  mayor_recaudacion = reduce(
      lambda tapa1, tapa2: tapa1 if tapa1[1][0] > tapa2[1][0] else tapa2,
      dic_estadisticas.items(),
  )

  return (tapas_alta_popularidad, iva, mayor_recaudacion)