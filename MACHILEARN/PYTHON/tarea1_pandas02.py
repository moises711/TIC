# Ejercicio 2 Pandas: Leer archivo CSV y analizar datos
import pandas as pd

df = pd.read_csv('productos.csv')
print('Lectura de CSV:\n', df)
print('Costo promedio:', df['costo'].mean())
