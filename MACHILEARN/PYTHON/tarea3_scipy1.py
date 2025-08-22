# Ejercicio 1 SciPy: Cálculo de la media con scipy.stats
from scipy import stats
datos = [1, 2, 3, 4, 5]
media = stats.tmean(datos)
print('Media con SciPy:', media)
