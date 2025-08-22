# Ejercicio 3 Keras: Funciones de activación
from tensorflow import keras
import tensorflow as tf
x = tf.constant([-2.0, 0.0, 2.0])
print('ReLU:', keras.activations.relu(x).numpy())
print('Sigmoid:', keras.activations.sigmoid(x).numpy())
print('Tanh:', keras.activations.tanh(x).numpy())
