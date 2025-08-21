# Importo la librería pandas para manejar datos en forma de tablas
import pandas as pd

# Defino un diccionario con los productos y sus costos
data  = {
    'producto':['tele','radio','silla'],
    'costo':[20,40,52]
}

# Creo un DataFrame a partir del diccionario para organizar los datos
df = pd.DataFrame(data)

# Imprimo el DataFrame para ver los productos y sus costos
print('producto:\n', df)