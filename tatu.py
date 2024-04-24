import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Gerar velocidades aleatórias para as rodas
np.random.seed(0)  # Para reprodutibilidade
r1 = np.random.randint(1, 5, size=100).astype(float)
r2 = np.random.randint(1, 5, size=100).astype(float)

# Ajustar as velocidades para garantir que a soma total das diferenças de velocidade seja zero
r1[-1] -= np.sum(r1 - r2)

# Ajustar as velocidades para garantir que a soma total das velocidades médias seja um múltiplo de 2π
r1 += 2 * np.pi - np.sum(r1 + r2) / 2 % (2 * np.pi)

# Criar um DataFrame com as velocidades das rodas e o tempo
df = pd.DataFrame({
    'r1': r1,
    'r2': r2,
    't': list(range(100))
})

# Salvar o DataFrame como um arquivo CSV
df.to_csv('random_path.csv', index=False)