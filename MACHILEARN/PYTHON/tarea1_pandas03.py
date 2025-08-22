# Ejercicio 3 Pandas: Filtrar y modificar datos
import pandas as pd

df = pd.read_csv('productos.csv')
filtrados = df[df['costo'] > 30]
print('Productos con costo mayor a 30:\n', filtrados)
df.loc[df['producto'] == 'radio', 'costo'] = 100
print('DataFrame con radio modificado:\n', df)
