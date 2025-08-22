from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Cargo el dataset de iris
datos = load_iris()
x = datos.data
y = datos.target  # Clases de las flores

# Creo y entreno el modelo de árbol de decisión
modelo = DecisionTreeClassifier()
modelo.fit(x, y)

# Defino una flor de prueba con sus características
test_flower = [[5.1, 3.5, 1.4, 0.2]]

# Realizo la predicción
prediccion = modelo.predict(test_flower)
print("Predicción :", datos.target_names[prediccion[0]])