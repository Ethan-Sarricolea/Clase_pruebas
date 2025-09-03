## Problema:

El problema del triángulo es uno de los ejemplos de mayor uso durante el aprendizaje de Pruebas de software.

Descripción del problema:
El programa acepta 3 enteros como entradas: a, b, y c. Estos serán los lados de un triángulo. Los enteros a, b, y c deben satisfacer las siguientes condiciones:

- c1: 1 <= a <= 200
- c2: 1 <= b <= 200
- c3: 1 <= c <= 200 
- c4: a < b + c
- c5: b < a + c
- c6: c < a + b

La salida del programa es el tipo de triángulo que es determinados por sus tres lados:
- Equilátero
- Isósceles.
- Escaleno.
- No es un Triángulo.

Si una entrada falla con las condiciones c1, c2 o c3, el programa muestra el mensaje "El valor? no está dentro del rango permitido".

Si los valores de a, b, y c satisfacen las condiciones c4, c5 y c6; se muestra uno de los siguientes mensajes

- Si todos los lados son iguales, se muestra "Equilátero".
- Si exactamente dos son iguales, se muestra "Isósceles".
- Si todos los lados son diferentes, se muestra "Escaleno".

Si alguna de las condiciones c4, c5 o c6, no se cumple, se muestra el mensaje "No es un Triángulo".

```py
# Problema del triangulo
"""
Descripcion: Programa de 3 entradas con diveras condiciones para identificar triangulo
Autor: Sarricolea Cortés Ethan Yahel
"""

def clearData(a, b, c):
  try: 
    for valor in (a, b, c):
        if (valor <= 0 or valor >= 200):
            raise ValueError(f"El valor {valor} no esta dentro del rango permitido")
    return True
  except ValueError as e:
    print(e)
    return False

def triangleType(a, b, c):
  total = a + b + c
  try:
    for side in (a, b, c):
      if (side > total-side):
        raise ValueError(f"No es un triangulo")
    if a == b == c:
      print("Equilatero")
    elif a == b or b == c or a == c:
      print("Isosceles")
    else:
      print("Escaleno")
  except ValueError as e:
    print(e)

def main():
  # Aceptar tres entradas
  a = int(input()) #
  b = int(input())
  c = int(input())

  if clearData(a, b, c):
    triangleType(a, b, c)

if __name__ == "__main__":
  main()
```
