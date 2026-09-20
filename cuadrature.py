"""Calcular la integral de x**6 - x**2*sin(2*x) con Gauss-Legendre.

Implementación de cuadratura de Gauss-Legendre en un intervalo general.
"""

import numpy as np


def gaussxw(N):
    """Obtener los puntos y pesos en el intervalo [-1, 1].

    Examples:
        >>> x, w = gaussxw(2)
        >>> np.allclose(x, [-1 / np.sqrt(3), 1 / np.sqrt(3)])
        True
        >>> np.allclose(w, [1, 1])
        True

    Args:
        N (int): Cantidad positiva de puntos de muestreo.

    Returns:
        tuple: Arreglos de NumPy (x, w) con los puntos y pesos.

    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w


def gaussxwab(a, b, x, w):
    """Escalar los puntos y pesos de [-1, 1] al intervalo [a, b].

    Examples:
        >>> x, w = gaussxw(2)
        >>> xp, wp = gaussxwab(1, 3, x, w)
        >>> np.allclose(xp, x + 2)
        True
        >>> np.allclose(wp, w)
        True

    Args:
        a (float): Límite inferior de integración.
        b (float): Límite superior de integración.
        x (numpy.ndarray): Puntos de muestreo en [-1, 1].
        w (numpy.ndarray): Pesos correspondientes a esos puntos.

    Returns:
        tuple: Arreglos (xp, wp) de puntos y pesos transformados.

    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w


def funcion(x):
    """Evaluar la función x**6 - x**2*sin(2*x).

    Examples:
        >>> float(funcion(0.0))
        0.0

    Args:
        x (float or numpy.ndarray): Valor o arreglo de valores; ángulos en radianes.

    Returns:
        float or numpy.ndarray: Valor de la función en cada punto.

    """
    return x**6 - x**2 * np.sin(2 * x)


def integrar(N, a=1.0, b=3.0):
    """Aproximar la integral mediante N puntos de Gauss-Legendre.

    Examples:
        >>> round(integrar(8), 8)
        317.34424667

    Args:
        N (int): Cantidad positiva de puntos de muestreo.
        a (float): Límite inferior; por defecto 1.0.
        b (float): Límite superior; por defecto 3.0.

    Returns:
        float: Aproximación numérica de la integral de funcion.

    """
    x, w = gaussxw(N)
    xp, wp = gaussxwab(a, b, x, w)
    return float(np.sum(wp * funcion(xp)))


def primitiva(x):
    """Evaluar una primitiva para comprobar la integración numérica.

    Examples:
        >>> float(primitiva(0.0))
        -0.25

    Args:
        x (float or numpy.ndarray): Valor o arreglo de valores.

    Returns:
        float or numpy.ndarray: Valor de una primitiva de funcion.

    """
    return x**7 / 7 + (x**2 / 2 - 1 / 4) * np.cos(2 * x) - x * np.sin(2 * x) / 2


def valor_referencia(a=1.0, b=3.0):
    """Calcular F(b)-F(a) como referencia analítica evaluada en punto flotante.

    Examples:
        >>> round(valor_referencia(), 8)
        317.34424667

    Args:
        a (float): Límite inferior; por defecto 1.0.
        b (float): Límite superior; por defecto 3.0.

    Returns:
        float: Valor de referencia con la precisión de la computadora.

    """
    return float(primitiva(b) - primitiva(a))


if __name__ == "__main__":
    referencia = valor_referencia()
    tolerancia = 1e-10
    primer_N = None
    print(f"Valor de referencia: {referencia:.13f}")
    print(f"Tolerancia absoluta: {tolerancia:.0e}")
    print(f"{'N':>3} {'Integral':>23} {'Error absoluto':>17}")
    for N in range(1, 13):
        resultado = integrar(N)
        error = abs(resultado - referencia)
        print(f"{N:3d} {resultado:23.13f} {error:17.3e}")
        if primer_N is None and error < tolerancia:
            primer_N = N
    print(f"Primer N que cumple la tolerancia: {primer_N}")
    print("La tolerancia numérica no equivale a exactitud matemática.")
