# Ejercicio 1 Scikit-learn: Regresión lineal
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

modelo = LinearRegression()
modelo.fit(X, y)

prediccion = modelo.predict([[6]])
print('Predicción para X=6:', prediccion[0])
