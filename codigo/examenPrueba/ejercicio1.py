class Empleado:
    def __init__(self, nombre, salario_base):
        self.__nombre = nombre
        self.__salario_base = salario_base
    #getters
    @property
    def nombre(self):
        return self.__nombre
    @property
    def salario_base(self):
        return self.__salario_base
    #setter
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre= nombre
    @salario_base.setter
    def salario_base(self, salario_base):
        self.__salario_base= salario_base
        
    def calcular_salario(irpf):
        salario_base-irpf
        salario_neto = self.salario_base-(self.salario_base*irpf/100)
        return salario_neto
        
    def __str__(self):
        return f"Nombre: {self.__nombre} - Salario base: {self.__salario_base}"
        

class Vendedor(Empleado):
    def __init__(self,nombre, salario_base ,ventas_realizadas):
        super().__init__(nombre, salario_base)
        self.__ventas_realizadas =ventas_realizadas
    #getter
    @property
    def ventas_realizadas(self):
        return self.__ventas_realizadas
    def calcular_salario(self):
        total_ventas= sum(self.ventas_realizadas)
        salario_neto = self.salario_base +total_ventas*0.1
        return salario_neto
    
    def __str__(self):
        return f"{super().__str__()}  - Ventas: {self.__ventas_realizadas} - Salario total: {self.calcular_salario()}"
    def agregar_venta(self, importe):
        self.__ventas_realizadas.append(importe)
    

## MAIN  ##

esclavo = Empleado( "Alejandro", 50)
esclavo2 = Empleado( "Gabriel_Vigo", 25) 

vendedor = Vendedor("benRu", 23, [232,2323,323])
vendedor2 = Vendedor("Maria", 464587, [232,2323,323])

print(esclavo)
print(esclavo2)
                    
print(vendedor)
print(vendedor2)
vendedor.nombre = "Deivid"
vendedor2.agregar_venta(4555)
print(vendedor2)






















        

    