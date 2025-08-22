# Ejercicio 1 Matplotlib: Histograma
import matplotlib.pyplot as plt
import numpy as np
datos = np.random.normal(0, 1, 1000)
plt.hist(datos, bins=30, color='skyblue', edgecolor='black')
plt.title('Histograma')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()
