# Ejemplo de uso

## Objetivo

Ejecutar el programa y comprobar el resultado con diferentes valores de N.

## 1. Ejecutar el programa

```bash
python cuadrature.py
```

Salida obtenida durante la comprobación (las últimas cifras pueden variar):

```text
Valor de referencia: 317.3442466738264
Tolerancia absoluta: 1e-10
  N                Integral    Error absoluto
  1       134.0544199624634         1.833e+02
  2       306.8199344959197         1.052e+01
  3       317.2641517338290         8.009e-02
  4       317.3453903341579         1.144e-03
  5       317.3442267219694         1.995e-05
  6       317.3442468899962         2.162e-07
  7       317.3442466722262         1.600e-09
  8       317.3442466738354         9.038e-12
  9       317.3442466738262         1.705e-13
 10       317.3442466738264         0.000e+00
 11       317.3442466738263         5.684e-14
 12       317.3442466738265         1.137e-13
Primer N que cumple la tolerancia: 8
La tolerancia numérica no equivale a exactitud matemática.

```

El programa prueba todos los valores del 1 al 12 y conserva el primero que
cumple la tolerancia. `abs` calcula el valor absoluto de la diferencia.
`range(1, 13)` incluye el 1 y excluye el 13.

## 2. Usar las funciones desde Python

```python
from cuadrature import integrar, valor_referencia

resultado = integrar(8)
error = abs(resultado - valor_referencia())
print(f"Integral: {resultado:.10f}")
print(f"Cumple la tolerancia: {error < 1e-10}")
# Integral: 317.3442466738
# Cumple la tolerancia: True
```

`.10f` muestra diez cifras decimales. La comparación devuelve `True` si
el error es menor que la tolerancia. Al importar el módulo no se imprime la
tabla: el bloque `if __name__ == "__main__":` solo se ejecuta al llamar al script.

