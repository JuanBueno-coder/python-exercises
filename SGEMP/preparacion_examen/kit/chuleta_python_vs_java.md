# Chuleta Python vs Java (examen SGEMP)

| Qué | Java | Python |
| --- | --- | --- |
| Bloques | `{ }` y `;` | `:` + 4 espacios de sangría, sin `;` |
| Variables | `int n = 5;` | `n = 5` |
| Leer teclado | `sc.nextInt()` | `int(input("Texto: "))` (input da `str`) |
| Imprimir | `System.out.println("a" + n)` | `print(f"a {n}")` · `print(a, b, end="")` |
| Decimales | `String.format("%.2f", x)` | `f"{x:.2f}"` · `round(x, 2)` |
| Lógicos | `&& \|\| !` · `null` · `true` | `and or not` · `None` · `True` |
| if | `else if` | `elif` · ternario `"A" if c else "B"` |
| for clásico | `for (int i=0; i<n; i++)` | `for i in range(n):` · `range(1, n+1)` · `range(7, 51, 7)` |
| for-each | `for (T x : lista)` | `for x in lista:` · con índice `for i, x in enumerate(lista):` |
| División | `7/2 = 3` (int) | `7/2 = 3.5` · `7//2 = 3` · `7%2 = 1` · `2**3 = 8` |
| switch | `switch` | `match op:` `case 1:` `case _:` |
| Excepciones | `try {} catch (E e) {}` | `try:` `except ValueError:` |
| ArrayList | `list.add(x)` · `list.size()` · `list.get(0)` | `l.append(x)` · `len(l)` · `l[0]` · `l[-1]` (último) |
| Más lista | `remove` · `contains` · `sort` | `l.remove(x)` · `x in l` · `l.sort()` · `sorted(l, key=..., reverse=True)` |
| Slicing | `subList` | `l[:3]` · `l[-2:]` · `l[::-1]` (invertida) · `l.copy()` |
| Tupla | (no hay) | `t = ("Ana", 3)` · un elemento: `(5,)` · inmutable · `nombre, n = t` |
| HashMap | `put` · `get` · `containsKey` | `d[k] = v` · `d[k]` · `d.get(k, 0)` · `k in d` · `del d[k]` |
| Recorrer mapa | `entrySet()` | `for k, v in d.items():` · `d.keys()` · `d.values()` |
| String | `split` · `trim` · `equals` | `s.split(",")` · `s.strip()` · `==` · `s.lower()` · `s.replace(a, b)` · `s[0]` |
| Unir textos | `String.join(",", l)` | `",".join(l)` (todo `str`) · `str(n)` para concatenar números |
| Método | `public int f(int a)` | `def f(a, b=0):` `return x, y` (devuelve tupla) |
| Main | `public static void main` | `def main():` + `if __name__ == "__main__":` `main()` |

## Ficheros
```python
with open("f.csv", "r", encoding="utf-8") as f:   # "w" machaca, "a" añade
    lineas = f.readlines()
for linea in lineas[1:]:                          # salta cabecera
    if linea.strip():                             # salta líneas vacías
        c = linea.strip().split(",")              # strip ANTES de split
        id_, nombre, n = int(c[0]), c[1], float(c[2])
f.write(f"{a},{b}\n")                             # el \n lo pones tú
```

## POO
```python
class Hija(Padre):                    # extends
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.__c = c                  # privado
    @property
    def c(self): return self.__c      # getter (sin setter = solo lectura)
    @c.setter
    def c(self, v): self.__c = v      # setter -> se usa obj.c = 5
    def __str__(self): return super().__str__() + f" - C: {self.__c}"
# en la hija, el privado del padre se lee con self.propiedad, NUNCA self.__privado
# isinstance(obj, Clase) = instanceof
```

## Funcional (sin for/while; comprensiones sí)
```python
from functools import reduce
list(map(lambda x: x * 2, l))                     # transformar
list(filter(lambda x: x > 0, l))                  # filtrar
reduce(lambda a, b: a + b, l, 0)                  # acumular (0 = valor inicial)
reduce(lambda a, b: a if a[1] > b[1] else b, d.items())   # máximo "a lo profe"
max(d.items(), key=lambda it: it[1][0])[0]        # clave con mayor valor[0]
sorted(l, key=lambda t: t[1], reverse=True)       # ordenar por campo
[k for k, v in d.items() if v[2] == "Alta"]       # comprensión de lista
{k: v[0] for k, v in d.items()}                   # comprensión de diccionario
sum(map(lambda v: v[1], d.values())) / len(d)     # media
tuple(...) / list(...)                            # map/filter se gastan: conviértelos
def gen(d):                                       # generador
    for k in d: yield k
```

## BBDD (pymysql)
```python
import pymysql
conn = pymysql.connect(host="db", user="root", password="test", database="examen")
cur = conn.cursor()
cur.execute("INSERT INTO t VALUES (%s, %s)", (a, b));  conn.commit()
cur.execute("SELECT a, b FROM t WHERE f = %s", (x,));  filas = cur.fetchall()
cur.rowcount            # filas afectadas por UPDATE/DELETE
except pymysql.err.IntegrityError:   # clave repetida
float(decimal) · str(fecha)          # DECIMAL y DATE no llegan como float/str
conn.close()
```
