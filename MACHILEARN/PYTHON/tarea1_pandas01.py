# Ejercicio 1 Pandas: Crear y manipular DataFrame
import pandas as pd

data = {'producto': ['tele', 'radio', 'silla'], 'costo': [20, 40, 52]}
df = pd.DataFrame(data)
print('DataFrame original:\n', df)
df['costo'] = df['costo'] * 2
print('DataFrame con costos duplicados:\n', df)
