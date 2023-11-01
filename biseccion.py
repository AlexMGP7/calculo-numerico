import numpy as np

def bisection_method(f, a, b, tol):
  """
  Resuelve la ecuación f(x) = 0 usando el método de bisección.

  Parámetros:
    f: La función a resolver.
    a: El límite inferior del intervalo.
    b: El límite superior del intervalo.
    tol: El margen de error.

  Devuelve:
    La raíz de la ecuación, o None si no se encuentra una raíz.
  """

  while True:
    c = (a + b) / 2
    if np.abs(f(c)) < tol:
      return c
    if f(a) * f(c) > 0:
      a = c
    else:
      b = c

def main():
  # Aproxima f(x) = e^x - 3x^2 en [0, 1] hasta que err < 0.04

  f = lambda x: np.exp(x) - 3 * x ** 2
  a = 0
  b = 1
  tol = 0.04

  root = bisection_method(f, a, b, tol)
  print(f"La raíz de la ecuación es {root:.4f}")

if __name__ == "__main__":
  main()
