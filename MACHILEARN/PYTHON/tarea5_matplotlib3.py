# Ejercicio 3 Matplotlib: Gráfico de dispersión
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 50)
y = 2 * x + np.random.normal(0, 2, 50)
plt.scatter(x, y, color='red')
plt.title('Gráfico de dispersión')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
