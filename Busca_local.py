import numpy as np


def hNeighborhood(chromossome, h):
    x = chromossome.copy()
    n = len(x.vec)
    z = np.zeros(n)
    norm = 0.0
    
    for i in range(n):
        if np.random.rand() <= 0.5:
            z[i] = np.random.randint(1, np.ceil((1.0 - x[i]) / h) + 1)
        else:
            z[i] = -1 * np.random.randint(1, np.ceil((x[i]) / h) + 1)
        norm += (z[i] * h) ** 2
    
    norm = np.sqrt(norm)
    if norm == 0:
        norm = 0.0001
    
    for i in range(n):
        x[i] += (1.0 / norm) * h * z[i] * h
        if x[i] < 0 or x[i] >= 1.0:
            x[i] += (1.0 / norm) * h * -1 * z[i] * h
    
    return x

def GridSearch(x, h,decoder):
    numGridPoints = int(np.floor(len(x.vec) * (1.0 / h)))
    numExaminedPoints = 0
    # Definir a melhor solução encontrada como a solução atual x
    xBest = x.copy()
    xBest_fit = decoder.decode(x)
    while numExaminedPoints <= numGridPoints:
        numExaminedPoints += 1
        # Criar uma solução vizinha no h-Neighborhood
        y = hNeighborhood(xBest, h)
        # Decoder
        y_fit = decoder.decode(y)
        if y_fit < xBest_fit:
            xBest = y
            xBest_fit = y_fit
            numExaminedPoints = 0
    # Retornar a melhor solução
    return xBest