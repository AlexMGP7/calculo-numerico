# import sympy as sp
# import numpy as np

import pytest

from biseccion import biseccion
#from newton_raphson import newton_raphson


#-------------------------------------------------------------------------------------------


import pytest

def test_biseccion_funcion_con_una_raiz_simple():
    """Prueba que la función de bisección encuentra correctamente la raíz de una función con una raíz simple."""

    def f(x):
        return x**2 - 2

    a = 0
    b = 2
    epsilon = 0.0001

    # La raíz de la función f es x = 1.4142141342163086.

    raiz_esperada = 1.414
    raiz_calculada = biseccion(f, a, b, epsilon)

    assert round(raiz_calculada, 3) == raiz_esperada

#-------------------------------------------------------------------------------------------

