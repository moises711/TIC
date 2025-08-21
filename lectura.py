# Importo la librería pandas para poder trabajar con datos en tablas
import pandas as pd

# Leo el archivo 'productos.csv' y lo guardo en un DataFrame llamado df
df = pd.read_csv('productos.csv')

# Imprimo el DataFrame para ver el contenido del archivo CSV
print(df)
