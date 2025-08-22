# Ejercicio 2 Matplotlib: Diagrama de caja
import matplotlib.pyplot as plt
import numpy as np
datos = np.random.normal(0, 1, 100)
plt.boxplot(datos)
plt.title('Diagrama de caja')
plt.xlabel('Datos')
plt.show()
