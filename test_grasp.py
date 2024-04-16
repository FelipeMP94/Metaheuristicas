from M_Grasp import linesearch,ConstrutiveGreedyRandomized,GRASP
import numpy as np
from TSP_decoder import TSPDecoder
from TSP_instance import TSPInstance
import time

if __name__ == "__main__":
    instance = TSPInstance(r"rd400.dat")
    decoder = TSPDecoder(instance)
    lb = 15281
    N =10
    melhor_sol = np.zeros(N)
    tempo_sol = np.zeros(N)
    rpds = np.zeros(N)
    
    for i in range(N):
        ind = np.random.rand(instance.num_nodes)
        fit = decoder.decode(ind)
        t_inicial = time.time()
        s,s_fit = GRASP(1,decoder)
        tempo = time.time() - t_inicial
        tempo_sol[i]= tempo 
        melhor_sol[i]= s_fit
        rpd = ((s_fit-lb)*100)/lb
        rpds[i] = rpd

    print(f'Melhor solução: {melhor_sol.min()}\n')
    print(f'Média solução: {melhor_sol.mean()}\n')
    print(f'Melhor tempo: {tempo_sol.min():.2f}\n')
    print(f'Média tempo: {tempo_sol.mean():.2f}\n')
    print(f'RPDs: {rpds.mean()}')