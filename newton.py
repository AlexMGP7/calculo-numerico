import sympy as sp

def newton_raphson_sympy(func, x0, tol=1e-6, max_iter=100):
    """
    Implementación del método de Newton-Raphson para encontrar raíces de una función simbólica.

    Args:
    func (sympy.Expr): La función simbólica para la cual encontrar la raíz.
    x0 (float): Aproximación inicial.
    tol (float): Tolerancia para el criterio de convergencia.
    max_iter (int): Número máximo de iteraciones permitidas.

    Returns:
    float or None: La aproximación de la raíz, o None si no converge.
    """
    x = sp.symbols('x')
    f = sp.lambdify(x, func)

    df = sp.diff(func, x)
    f_prime = sp.lambdify(x, df)

    x_n = x0
    for _ in range(max_iter):
        f_x_n = f(x_n)
        if abs(f_x_n) < tol:
            return x_n
        f_prime_x_n = f_prime(x_n)
        if f_prime_x_n == 0:
            return None  # La derivada es cero, no se puede continuar
        x_n = x_n - f_x_n / f_prime_x_n
    return None  # No se alcanzó la convergencia en el número máximo de iteraciones
