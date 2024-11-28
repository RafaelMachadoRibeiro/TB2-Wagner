import numpy as np

matriz = np.random.rand(3, 3)

determinante = np.linalg.det(matriz)

if determinante != 0:
    inversa = np.linalg.inv(matriz)
else:
    inversa = None

print("Matriz aleatória 3x3:")
print(matriz)
print("\nDeterminante da matriz:")
print(determinante)
if inversa is not None:
    print("\nInversa da matriz:")
    print(inversa)
else:
    print("\nA matriz não é inversível (determinante é zero).")
