from TSP_instance import TSPInstance
from heuristica_construtiva import GreadyRandomTour
import numpy as np 
from TSP_decoder import TSPDecoder

if __name__ == "__main__":
    pop_size = 1000
    instance = TSPInstance(r'burma14.dat')
    decoder = TSPDecoder(instance)

    N = instance.num_nodes
    init_pop = np.random.rand(pop_size,N)
    init_fitness_random = np.zeros(pop_size)

    init_pop_gready = np.zeros((pop_size,N))
    init_fitness_gready = np.zeros(pop_size)
    
    
    #calculando fitness
    for i in np.arange(len(init_pop)):
        fit = decoder.decode(init_pop[i])
        init_fitness_random[i] = fit 
   
    for i in np.arange(len(init_pop_gready)):
        init_pop_gready[i] = GreadyRandomTour(instance)
        fit = decoder.decode(init_pop_gready[i])
        init_fitness_gready[i] = fit


    print(f'Maior: {np.max(init_fitness_random)}, Menor: {np.min(init_fitness_random)}, Média: {np.mean(init_fitness_random)}\n')
    print(f'Maior: {np.max(init_fitness_gready)}, Menor: {np.min(init_fitness_gready)}, Média: {np.mean(init_fitness_gready)}\n')
