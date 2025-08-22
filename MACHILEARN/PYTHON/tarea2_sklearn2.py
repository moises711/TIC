# Ejercicio 2 Scikit-learn: Clasificación con árbol de decisión
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
datos = load_iris()
x = datos.data
y = datos.target
modelo = DecisionTreeClassifier()
modelo.fit(x, y)
test_flower = [[5.1, 3.5, 1.4, 0.2]]
prediccion = modelo.predict(test_flower)
print('Predicción:', datos.target_names[prediccion[0]])
