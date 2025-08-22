# Ejercicio 3 Numpy: Leer archivo CSV con Numpy
import numpy as np

# Suponiendo que el archivo tiene solo números en la segunda columna
try:
    datos = np.loadtxt('productos.csv', delimiter=',', skiprows=1, usecols=[1])
    print('Datos de la columna costo:', datos)
except Exception as e:
    print('Error al leer con Numpy:', e)
