import numpy as np

array = np.random.randint(0, 11, size=30)

valores_unicos, frequencias = np.unique(array, return_counts=True)

print("Array de números aleatórios:")
print(array)
print("\nValores únicos:")
print(valores_unicos)
print("\nFrequência de cada valor:")
print(frequencias)