# Ejemplo 2 PyTorch: multiplicación de tensores
import torch

# Creo dos tensores
x = torch.tensor([2, 4, 6])
y = torch.tensor([3, 5, 7])

# Multiplico los tensores
producto = x * y
print('Multiplicación de tensores:', producto)
