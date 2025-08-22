# Ejercicio 2 TensorFlow: multiplicación de matrices
import tensorflow as tf
matriz1 = tf.constant([[1, 2], [3, 4]])
matriz2 = tf.constant([[2, 0], [1, 2]])
producto = tf.matmul(matriz1, matriz2)
print('Producto de matrices:', producto.numpy())
