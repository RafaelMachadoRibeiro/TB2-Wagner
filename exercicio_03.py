import numpy as np

array = np.arange(51)

pares = array[array % 2 == 0]

multiplos_de_5 = array[array % 5 == 0]

print("Elementos pares:", pares)
print("Múltiplos de 5:", multiplos_de_5)