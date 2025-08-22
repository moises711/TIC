# Ejercicio 3 TensorFlow: función de activación ReLU
import tensorflow as tf
x = tf.constant([-2.0, 0.0, 2.0])
relu = tf.nn.relu(x)
print('ReLU:', relu.numpy())
