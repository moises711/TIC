# Ejercicio 2 SciPy: Integración numérica
from scipy import integrate
resultado, error = integrate.quad(lambda x: x**2, 0, 1)
print('Integral de x^2 de 0 a 1:', resultado)
