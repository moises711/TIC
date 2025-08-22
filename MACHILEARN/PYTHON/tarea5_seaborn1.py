# Ejercicio 1 Seaborn: Histograma
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
datos = np.random.normal(0, 1, 1000)
sns.histplot(datos, bins=30, kde=True, color='skyblue')
plt.title('Histograma con Seaborn')
plt.show()
