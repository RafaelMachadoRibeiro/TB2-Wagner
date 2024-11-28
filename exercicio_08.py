import numpy as np

matriz = np.random.rand(3, 3)

autovalores, autovetores = np.linalg.eig(matriz)

print("Matriz aleatória 3x3:")
print(matriz)
print("\nAutovalores:")
print(autovalores)
print("\nAutovetores:")
print(autovetores)
