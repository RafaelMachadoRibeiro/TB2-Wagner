import numpy as np

matriz = np.arange(1, 10).reshape(3, 3)

media_linhas = np.mean(matriz, axis=1, keepdims=True)

matriz_centralizada = matriz - media_linhas

print("Matriz original:")
print(matriz)
print("\nMédia de cada linha:")
print(media_linhas)
print("\nMatriz após subtração das médias das linhas:")
print(matriz_centralizada)