import numpy as np

notas = np.array([
    [7.5, 8.0, 6.5, 9.0],  # Aluno 1
    [8.5, 7.0, 9.0, 6.0],  # Aluno 2
    [6.0, 7.5, 8.0, 7.0],  # Aluno 3
    [9.0, 8.5, 7.5, 8.0],  # Aluno 4
    [7.0, 6.5, 8.5, 9.0]   # Aluno 5
])

media_alunos = np.mean(notas, axis=1)

media_provas = np.mean(notas, axis=0)

print("Médias dos alunos:", media_alunos)
print("Médias das provas:", media_provas)