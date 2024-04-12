import numpy as np
import time


def CrossOver(elit_size,pop_size,rhoe,pop,N):
    elit_parent = np.random.randint(0,high=elit_size)
    non_elit_parent = np.random.randint(elit_size,high=pop_size)
    new_chromossome = np.zeros(N)
    for i in np.arange(N):
        if np.random.rand() < rhoe:
            new_chromossome[i] = pop[elit_parent][i]
        else:
             new_chromossome[i] = pop[non_elit_parent][i]
    return new_chromossome

def BRKGA(N,decoder):
    pop_size = 1000
    pe = 0.2
    pm = 0.25
    rhoe = 0.7
    limit_wo_improvment = 50
    #inicializando população
    init_pop = np.random.rand(pop_size,N)
    init_fitness = np.zeros(pop_size)
    
    #calculando fitness
    start_time = time.time()
    for i in np.arange(len(init_pop)):
        fit = decoder.decode(init_pop[i])
        init_fitness[i] = fit 
        
    sorted_fit_indices = np.argsort(init_fitness)
    sorted_fit = np.sort(init_fitness)
    sorted_pop = np.zeros((pop_size,N))
    
    for i in np.arange(len(sorted_fit_indices)):
        sorted_pop[i] = init_pop[sorted_fit_indices[i]] 
        
    best_fit = sorted_fit[0]
    
    num_generation = 0 
    generation_wo_improvement = 0
    
    evolve = True
    
    pop_atual = sorted_pop
    pop_atual_fit = sorted_fit
    while(evolve):
        num_generation += 1
        new_pop =  np.zeros((pop_size,N))
        new_pop_fit = np.zeros(pop_size)
        
        #Gerando nova população 
        for i in np.arange(int(pop_size*pe)):
            new_pop[i] = pop_atual[i]
        
        for i in range(int(pop_size*pe), int(pop_size-pop_size*pm)):
            new_pop[i] = CrossOver(int(pop_size*pe),pop_size,rhoe,pop_atual,N)
        
        for i in range(pop_size-int(pop_size*pe)-int(pop_size*pm),pop_size):
            new_pop[i] = np.random.rand(N)
        
        #Fitness da nova população    
        new_pop_fit[0:int(pop_size*pe)] = pop_atual_fit[0:int(pop_size*pe)]
        for i in range(int(pop_size*pe),pop_size):
            new_pop_fit[i] = decoder.decode(new_pop[i])
            
        #Ordenando nova população
        sorted_indices = np.argsort(new_pop_fit)
        sorted_new_pop =  np.zeros((pop_size,N))
        sorted_new_pop_fit = np.zeros(pop_size)
        for i in np.arange(len(sorted_indices)):
            sorted_new_pop[i] = new_pop[sorted_indices[i]]
            sorted_new_pop_fit[i] = new_pop_fit[sorted_indices[i]]
        
        pop_atual = sorted_new_pop
        pop_atual_fit = sorted_new_pop_fit
        if best_fit > pop_atual_fit[0]:
            best_fit = pop_atual_fit[0]
            generation_wo_improvement = 0
            time_to_find_best = time.time() - start_time
        else:
            generation_wo_improvement+=1
        
        if generation_wo_improvement == limit_wo_improvment:
            break

    return best_fit, time_to_find_best