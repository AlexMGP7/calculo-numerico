def integracion_trapecio(func, a, b, n):
    """
    Implementación del método del trapecio para aproximar la integral definida de una función.

    Args:
    func (callable): La función para la cual aproximar la integral.
    a (float): Límite inferior del intervalo de integración.
    b (float): Límite superior del intervalo de integración.
    n (int): Número de subintervalos para dividir el intervalo [a, b].

    Returns:
    tuple: Una tupla que contiene el resultado de la aproximación de la integral y el error estimado.
    """
    delta_x = (b - a) / n
    integral_aprox = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        xi = a + i * delta_x
        integral_aprox += func(xi)
    integral_aprox *= delta_x
    # Para el método del trapecio, el error se estima como la diferencia entre la suma de las áreas
    # bajo la curva y la suma de las áreas de los trapecios.
    error = abs((b - a) * (func(a) + func(b)) / 2 - integral_aprox)
    return integral_aprox, error
