# Ejercicio 2 Pandas: Filtrar datos
import pandas as pd
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
filtrado = df[df['A'] > 1]
print('Filtrado:\n', filtrado)
