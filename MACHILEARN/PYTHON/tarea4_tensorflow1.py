# Ejercicio 1 TensorFlow: suma de tensores
import tensorflow as tf
a = tf.constant([1, 2, 3])
b = tf.constant([4, 5, 6])
suma = tf.add(a, b)
print('Suma de tensores:', suma.numpy())
