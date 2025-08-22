# Ejercicio 1 Keras: Red neuronal simple
from tensorflow import keras
import numpy as np
X = np.array([[0], [1], [2], [3], [4]])
y = np.array([0, 1, 4, 9, 16])
model = keras.Sequential([
    keras.layers.Dense(10, activation='relu', input_shape=(1,)),
    keras.layers.Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=100, verbose=0)
print('Predicción para x=5:', model.predict([[5]])[0][0])
