"""PLANTILLA POO (Ejercicio 1 del examen) - probada con Python 3.
Copia, renombra clases/atributos y adapta los textos de __str__ AL PIE DE LA LETRA."""


class Empleado:                                    # Java: public class Empleado {
    def __init__(self, nombre, salario_base):      # Java: constructor
        self.__nombre = nombre                     # __ = private
        self.__salario_base = salario_base

    # ---- getter + setter (Java: getNombre / setNombre) ----
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, valor):                 # setter CON VALIDACION
        if valor >= 0:                             # si no es valido, no cambia nada
            self.__salario_base = valor

    def calcular_salario(self, irpf=0):            # parametro con valor por defecto
        return self.__salario_base - self.__salario_base * irpf / 100

    def __str__(self):                             # Java: toString()
        return f"Nombre: {self.__nombre} - Salario base: {self.__salario_base}"


class Vendedor(Empleado):                          # Java: extends Empleado
    def __init__(self, nombre, salario_base, ventas_realizadas):
        super().__init__(nombre, salario_base)     # Java: super(nombre, salario_base)
        self.__ventas_realizadas = ventas_realizadas

    @property
    def ventas_realizadas(self):                   # SOLO LECTURA: sin @...setter
        return self.__ventas_realizadas.copy()     # "devuelve una copia"

    def agregar_venta(self, importe):
        self.__ventas_realizadas.append(importe)

    def calcular_salario(self, irpf=0):            # SOBRESCRIBE (override)
        # OJO: aqui self.__salario_base NO existe -> usar la propiedad self.salario_base
        return self.salario_base + sum(self.__ventas_realizadas) * 10 / 100

    def __str__(self):                             # reutiliza el __str__ del padre
        return (super().__str__() + f" - Ventas: {self.__ventas_realizadas}"
                f" - Salario total: {self.calcular_salario()}")


class Empresa:                                     # CLASE CONTENEDORA (lista de objetos)
    def __init__(self):
        self.__empleados = []

    @property
    def empleados(self):
        return self.__empleados

    def alta_empleado(self, oEmpleado):            # "siempre que no este repetido" (por nombre)
        for e in self.__empleados:
            if e.nombre == oEmpleado.nombre:
                return "Empleado repetido"
        self.__empleados.append(oEmpleado)
        return "Alta OK"

    def baja_empleado(self, nombre):
        for e in self.__empleados:
            if e.nombre == nombre:
                self.__empleados.remove(e)
                return "Empleado dado de baja"
        return "Empleado no localizado"

    def listado_vendedores(self):                  # filtrar por tipo con isinstance (Java: instanceof)
        texto = ""
        for e in self.__empleados:
            if isinstance(e, Vendedor):
                texto += str(e) + "\n"
        return texto

    def total_salarios(self):                      # version SIN bucles
        return sum(map(lambda e: e.calcular_salario(), self.__empleados))


def main():
    e1 = Empleado("Lola Mento", 1500)
    e2 = Empleado("Aitor Tilla", 1800)
    v1 = Vendedor("Elena Nito", 1200, [100, 150, 80])
    v2 = Vendedor("Paco Merte", 1100, [])
    for obj in (e1, e2, v1, v2):
        print(obj)                                 # print llama a __str__
    print(e1.calcular_salario(15))                 # 1275.0
    e1.salario_base = 2000                         # usa el SETTER (sin parentesis)
    e2.salario_base = -5                           # setter lo ignora
    v2.agregar_venta(300)
    v2.agregar_venta(200)
    copia = v1.ventas_realizadas
    copia.append(9999)                             # no afecta al objeto: era una copia
    print("--- Actualizados ---")
    for obj in (e1, e2, v1, v2):
        print(obj)
    emp = Empresa()
    print(emp.alta_empleado(v1), emp.alta_empleado(v1), emp.alta_empleado(e1))
    print(emp.listado_vendedores(), end="")
    print(emp.baja_empleado("Nadie"), emp.total_salarios())


if __name__ == "__main__":
    main()
