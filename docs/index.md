# Tarea 2: Cuadratura gaussiana, documentación de código y Git

**Orlando Ismael Benavides Renault — C11025**

## Objetivo

Calcular numéricamente la integral

$$I=\int_1^3 [x^6-x^2\sin(2x)]\,dx$$

utilizando cuadratura de Gauss-Legendre. Los puntos y pesos se calculan en [-1, 1] y se transforman al intervalo de integración.

## Organización

- [Método numérico](explanation.md): puntos, pesos, cambio de intervalo y precisión.
- [Ejemplo de uso](tutorials.md): ejecución del programa y resultados.
- [Referencia de funciones](reference.md): documentación automática de los docstrings.

El módulo `cuadrature.py` implementa el método numérico.
La función trigonométrica se evalúa en radianes.

## Resultado

Obtengo aproximadamente **317.3442466738264**.
Defino una tolerancia absoluta de **10⁻¹⁰**; el primer valor que la cumple
al probar N = 1, 2, ..., 12 es **N = 8**. Esta tolerancia es una elección
explícita para la comprobación, no un dato proporcionado por el enunciado.
