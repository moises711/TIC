# Ejercicio 3 PyTorch: matriz y suma por filas
import torch

matriz = torch.tensor([[1, 2], [3, 4]])
suma_filas = matriz.sum(dim=1)
print('Suma por filas:', suma_filas)
