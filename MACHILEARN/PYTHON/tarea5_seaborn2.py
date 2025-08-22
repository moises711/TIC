# Ejercicio 2 Seaborn: Diagrama de caja
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
datos = np.random.normal(0, 1, 100)
sns.boxplot(x=datos, color='lightgreen')
plt.title('Diagrama de caja con Seaborn')
plt.show()
