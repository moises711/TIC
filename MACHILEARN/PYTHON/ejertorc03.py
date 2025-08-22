# Ejemplo 3 PyTorch: matriz y suma por filas
import torch

# Creo una matriz
matriz = torch.tensor([[1, 2], [3, 4]])

# Sumo los valores por filas
suma_filas = matriz.sum(dim=1)
print('Suma por filas:', suma_filas)
