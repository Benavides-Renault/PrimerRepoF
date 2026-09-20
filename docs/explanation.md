# Explicación del método numérico

## 1. Objetivo

Aproximo una integral mediante una suma de valores de la función multiplicados por pesos:

$$\int_a^b f(x)\,dx\approx\sum_{k=1}^{N}w'_k f(x'_k).$$

`N` indica la cantidad de puntos de muestreo. Los puntos no tienen que estar
igualmente separados. Los pesos indican cuánto aporta cada evaluación a la suma.

## 2. Puntos y pesos de Legendre

En el intervalo original [-1, 1], los puntos son las raíces del polinomio de Legendre de grado N:

$$P_N(x_k)=0,\qquad w_k=\frac{2}{(1-x_k^2)[P'_N(x_k)]^2}.$$

Calculo los puntos y pesos mediante:

```python
x, w = np.polynomial.legendre.leggauss(N)
```

1. `np.polynomial.legendre` contiene herramientas para polinomios de Legendre.
2. `leggauss(N)` devuelve los N puntos y sus N pesos.
3. `x, w` guarda ambos arreglos por separado.
4. Mi función `gaussxw(N)` devuelve esos arreglos mediante `return x, w`.

## 3. Escalar el intervalo

Los puntos anteriores pertenecen a [-1, 1], pero necesito integrar en [1, 3]. Uso:

$$x'_k=\frac{b-a}{2}x_k+\frac{b+a}{2},\qquad w'_k=\frac{b-a}{2}w_k.$$

Para a = 1 y b = 3, resulta:

$$x'_k=x_k+2,\qquad w'_k=w_k.$$

Los pesos quedan iguales en este caso porque ambos intervalos tienen longitud 2.
La función `gaussxwab(a, b, x, w)` mantiene la fórmula general para otros intervalos.

## 4. Evaluar la suma

```python
x, w = gaussxw(N)
xp, wp = gaussxwab(1, 3, x, w)
resultado = np.sum(wp * funcion(xp))
```

1. Obtengo puntos y pesos en [-1, 1].
2. Transformo ambos al intervalo del problema.
3. `funcion(xp)` evalúa todos los puntos de manera vectorial.
4. `wp * funcion(xp)` multiplica cada valor por su peso.
5. `np.sum` suma todas las contribuciones.

En Python uso `**` para elevar a una potencia. `np.sin(2*x)` calcula el seno
en radianes. No necesito un ciclo para evaluar cada punto por separado.
El ciclo del programa principal se utiliza para comparar diferentes valores de N.

## 5. Comprobación analítica

Para comparar necesito una referencia independiente de la cuadratura.
Integro el término x⁶ directamente y el término x² sen(2x) por partes dos veces:

$$\int x^2\sin(2x)\,dx=-\frac{x^2}{2}\cos(2x)
+\frac{x}{2}\sin(2x)+\frac14\cos(2x).$$

Por tanto, una primitiva de la función completa es:

$$F(x)=\frac{x^7}{7}+\left(\frac{x^2}{2}-\frac14\right)\cos(2x)
-\frac{x}{2}\sin(2x).$$

La integral exacta se puede expresar como:

$$I=\frac{2186}{7}+\frac{17}{4}\cos(6)-\frac14\cos(2)
-\frac32\sin(6)+\frac12\sin(2).$$

Al evaluar esa expresión en la computadora obtengo aproximadamente
317.3442466738264. Esa representación decimal tiene errores de redondeo.

## 6. ¿Con cuál N se alcanza el resultado exacto?

La regla de N puntos integra exactamente polinomios de grado hasta 2N−1
(en aritmética exacta). Para x⁶ bastaría N = 4, pues 2(4)−1 = 7.
Sin embargo, la función completa incluye un seno y no es un polinomio.
Por eso no puedo concluir que N = 4 resuelva exactamente toda la integral.

Defino el error absoluto y la condición de aceptación:

$$E_N=|I_N-I_{\mathrm{ref}}|,\qquad E_N<10^{-10}.$$

No existe una garantía de exactitud matemática para esta función por la regla
polinómica. Respondo en términos de precisión numérica: **N = 8 es el primer N
probado que cumple la tolerancia elegida**. Con N = 9 el error ya es del orden
de 10⁻¹³; las últimas cifras dependen del redondeo de punto flotante.
Aumentar N no garantiza que esas últimas cifras mejoren de manera monótona.

## 7. Pruebas

| N | Integral aproximada | Error absoluto |
|---:|---:|---:|
| 1 | 134.0544199624634 | 1.833e+02 |
| 2 | 306.8199344959197 | 1.052e+01 |
| 3 | 317.2641517338290 | 8.009e-02 |
| 4 | 317.3453903341579 | 1.144e-03 |
| 5 | 317.3442267219694 | 1.995e-05 |
| 6 | 317.3442468899962 | 2.162e-07 |
| 7 | 317.3442466722262 | 1.600e-09 |
| 8 | 317.3442466738354 | 9.038e-12 |
| 9 | 317.3442466738262 | 1.705e-13 |
| 10 | 317.3442466738264 | 0.000e+00 |
| 11 | 317.3442466738263 | 5.684e-14 |
| 12 | 317.3442466738265 | 1.137e-13 |

## Material de referencia

- Notebook suministrado: `GaussianCuadratureAndFitting(1).ipynb`, sección Cuadratura Gaussiana.
- Mark Newman, *Computational Physics*, capítulo 5 y apéndice C, citados en el notebook.
