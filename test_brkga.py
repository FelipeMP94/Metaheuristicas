from M_brkga import BRKGA
from TSP_decoder import TSPDecoder
from TSP_instance import TSPInstance
import numpy as np 


if __name__ == "__main__":
    instance = TSPInstance(r"rd400.dat")
    max_instance = 15281
    decoder = TSPDecoder(instance)
    N = 10
    best_values = np.zeros(N)
    times = np.zeros(N)
    rpds = np.zeros(N)
    for i in np.arange(N):
        best,time_best = BRKGA(instance.num_nodes,decoder)
        best_values[i] = best
        times[i] = time_best
        rpds[i] = ((best-max_instance)*100)/max_instance    
    best_solution = best_values.min()
    best_time = times.min()

    mean_solution = best_values.mean()
    mean_time = times.mean()

    RDP = rpds.mean()
    print(f'Melhor: {best_solution} Média {mean_solution} Melhor tempo:{best_time:.2f} Média tempo:{mean_time} RDP:{RDP}')
