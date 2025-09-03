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
  a = int(input())
  b = int(input())
  c = int(input())

  if clearData(a, b, c):
    triangleType(a, b, c)

if __name__ == "__main__":
  main()
