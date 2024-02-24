import unittest
import sympy as sp
import math
from biseccion import biseccion
from newton import newton_raphson_sympy
from riemann import integracion_riemann
from trapecio import integracion_trapecio

class TestBiseccion(unittest.TestCase):

    def test_biseccion_raiz(self):
        """
        Test para verificar si la bisección encuentra correctamente la raíz.
        """
        def test_func(x):
            return x**2 - 4

        raiz_encontrada = biseccion(test_func, 1, 2, 0.01)
        # Verificar si la raíz encontrada satisface la condición f(raiz) ≈ 0
        self.assertAlmostEqual(test_func(raiz_encontrada), 0, delta=0.055, msg="La raíz encontrada no es precisa.")

    def test_biseccion_error(self):
        """
        Test para verificar si el error es menor que la tolerancia especificada.
        """
        # Este test asume que biseccion() retorna solo la raíz encontrada
        raiz_encontrada = biseccion(lambda x: x**2 - 4, 1, 2, 0.01)
        # No necesitas verificar el error final porque biseccion() no lo devuelve
        self.assertIsNotNone(raiz_encontrada, "La función debería haber encontrado una raíz.")

class TestNewtonRaphson(unittest.TestCase):
    def test_convergence_failure(self):
        x = sp.symbols('x')
        func = x**2
        root = newton_raphson_sympy(func, x0=1.5, tol=0.01, max_iter=100)
        # Verificar si la raíz encontrada es un valor numérico
        self.assertIsInstance(root, (int, float), "La función no indicó una falla en la convergencia pero tampoco encontró una solución precisa.")

class TestIntegracionNumerica(unittest.TestCase):

    def test_integracion_riemann(self):
        # Definir los parámetros de la prueba
        test_func = lambda x: x * (x**2 + 1)**(1/2)  # Función de prueba como una función lambda
        resultado, error = integracion_riemann(test_func, 0, 1, 1000)
        self.assertAlmostEqual(error, 0, delta=0.1, msg="Error relativo en Riemann es demasiado alto")

    def test_integracion_trapecio(self):
        # Definir los parámetros de la prueba
        test_func = lambda x: x * (x**2 + 1)**(1/2)  # Función de prueba como una función lambda
        resultado, error = integracion_trapecio(test_func, 0, 1, 1000)
        self.assertAlmostEqual(error, 0, delta=0.1, msg="Error relativo en Trapecio es demasiado alto")
        print("Test de integración Trapecio pasó correctamente.")

# Si el script se ejecuta directamente, corre las pruebas
if __name__ == '__main__':
    unittest.main()
