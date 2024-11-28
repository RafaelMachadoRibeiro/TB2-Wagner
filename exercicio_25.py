import numpy as np

matriz = np.random.randint(1, 11, size=(4, 3))

soma_total = np.sum(matriz)

produto_linhas = np.prod(matriz, axis=1)

print("Matriz 4x3 com números aleatórios:")
print(matriz)
print("\nSoma de todos os elementos:")
print(soma_total)
print("\nProduto dos elementos em cada linha:")
print(produto_linhas)