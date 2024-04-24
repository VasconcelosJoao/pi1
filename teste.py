import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_path(filename, d=10):
    df = pd.read_csv(filename)

    df['v_avg'] = (df['r1'] + df['r2']) / 2
    df['v_diff'] = df['r1'] - df['r2']

    df['theta'] = np.cumsum(df['v_diff'] / d)  

    df['x'] = np.cumsum(df['v_avg'] * np.cos(df['theta']))
    df['y'] = np.cumsum(df['v_avg'] * np.sin(df['theta']))

    plt.figure(figsize=(10,5))
    plt.plot(df['x'], df['y'])
    plt.axis('equal') 
    plt.grid(True) 
    plt.xlabel('Posição X (cm)')
    plt.ylabel('Posição Y (cm)')
    plt.title('Esboço do Percurso')

    plt.savefig('percurso.png')

plot_path('random_path.csv')

## rpm -> m/s = rpm*2*pi*r/60