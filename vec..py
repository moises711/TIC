# Importo la librería pandas para trabajar con datos en Python
import pandas as pd

# Creo una serie de datos llamada "ventas" con los valores que quiero analizar
serie = pd.Series(data=[12, 20, 30, 40, 50], name="ventas")

# Imprimo la serie para ver cómo quedó en pantalla
print("serie:\n", serie)