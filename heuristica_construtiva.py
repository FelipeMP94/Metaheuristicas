import numpy as np


def GreadyRandomTour(instance):
    inicial = np.random.randint(0,high=instance.num_nodes)
    tour  = np.full(instance.num_nodes,-1)
    n_can = 4
    for i in range(len(tour)):
        if i ==0:
            tour[i] = inicial
        else:
            candidates = np.zeros(instance.num_nodes)
            for j in range(len(candidates)):
                if  np.any(tour==j):
                    candidates[j] = np.inf
                else:
                    candidates[j] = instance.distance(int(tour[i-1]),int(j))
            order = np.argsort(candidates)
            if instance.num_nodes - len(tour) >= n_can:
                prox = np.random.randint(0,high=n_can)
                tour[i] = order[prox]
            elif instance.num_nodes - len(tour)!=0:
                prox = np.random.randint(0,high=instance.num_nodes - len(tour))
                tour[i] = order[prox]
            elif instance.num_nodes - len(tour) ==0:
                tour[i] = order[0]

    vec = np.zeros(instance.num_nodes,dtype=float)
    aux = 0
    for i in range(len(tour)):
        aux += np.random.randint(1,high=10) 
        vec[tour[i]] = float(aux) 

    aux += np.random.randint(1,high=10)
    for i in range(len(vec)):
        vec[i] = vec[i]/float(aux) 
    
    return vec 