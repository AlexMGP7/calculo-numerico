def biseccion(f, a, b, epsilon):
    """Encuentra una raíz aproximada de la función f en el intervalo [a, b] con un error máximo de epsilon.

    Args:
      f: Una función que toma un número real y devuelve un número real.
      a: El límite izquierdo del intervalo.
      b: El límite derecho del intervalo.
      epsilon: El error máximo permitido.

    Returns:
      Una raíz aproximada de la función f en el intervalo [a, b] con un error máximo de epsilon.
    """

    while abs(b - a) > epsilon:
        # Calcula el punto medio del intervalo
        c = (a + b) / 2

        # Si f(a) * f(c) es menor que 0, entonces la raíz está en el intervalo (a, c)
        if f(a) * f(c) < 0:
            b = c

        # Si f(a) * f(c) es mayor que 0, entonces la raíz está en el intervalo (c, b)
        else:
            a = c
    
    return c
