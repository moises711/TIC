# Ejercicio 3 Seaborn: Gráfico de dispersión
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 50)
y = 2 * x + np.random.normal(0, 2, 50)
sns.scatterplot(x=x, y=y, color='red')
plt.title('Gráfico de dispersión con Seaborn')
plt.show()
