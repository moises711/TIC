# Ejemplo 1 PyTorch: suma de tensores
import torch

# Creo dos tensores
x = torch.tensor([1, 2, 3, 4])
y = torch.tensor([5, 6, 7, 8])

# Sumo los tensores
total = x + y
print('Suma de tensores:', total)
