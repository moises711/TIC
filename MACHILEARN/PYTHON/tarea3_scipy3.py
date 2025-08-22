# Ejercicio 3 SciPy: Optimización
from scipy.optimize import minimize
resultado = minimize(lambda x: (x-2)**2, x0=0)
print('Mínimo de (x-2)^2:', resultado.x[0])
