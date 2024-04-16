import numpy as np

def hNeighborhood(chromossome, h):
    x = chromossome.copy()
    n = len(x)
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
    numGridPoints = int(np.floor(len(x) * (1.0 / h)))
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
    return xBest,xBest_fit






def linesearch(ind,h,i,decoder):
    choromossome = ind.copy()
    bestZ = choromossome.copy()
    bestF = np.inf
    rk = []
    tau = 0
    rk.append(choromossome[i]+tau*h)
    for j in range(0,int(1.0/h)+1,2):
        tau+=1
        if(choromossome[i]+tau*h>=0) and (choromossome[i]+tau*h<1):
            rk.append(choromossome[i]+tau*h)
        if(choromossome[i]+(-1*tau)*h>=0) and (choromossome[i]+(-1*tau)*h<1):
            rk.append(choromossome[i]+(-1*tau)*h)

    q = min(int(np.ceil(np.log2(1.0/h))) + 1, len(rk))
    np.random.shuffle(rk)
    for j in range(q):
        choromossome[i] = rk[j]
        fit = decoder.decode(choromossome)
        if fit < bestF:
            bestZ = choromossome.copy()
            bestF = fit
    return bestZ[i],bestF


def ConstrutiveGreedyRandomized(chromossome, h, alpha, decoder, beta_min=0.5, beta_max=0.8):
    s = chromossome.copy()
    n = len(s)
    intensity = np.random.uniform(beta_min, beta_max)
    unfixed = np.arange(n)  # Armazena as random-keys ainda não fixadas

    for _ in range(int(n * intensity)):
        np.random.shuffle(unfixed)
        k_max = min(int(len(unfixed) * 0.5), 2)  # Número máximo de random-keys a serem pesquisadas
        chosen_rk = unfixed[:k_max]

        # Line search
        z = np.zeros(n)
        g = np.full(n, np.inf)
        for k in chosen_rk:
            s_aux = s.copy()  # Copia da solução corrente
            z[k],g[k] = linesearch(s_aux, h, k, decoder)

        # Atualização dos valores mínimos e máximos de g
        g_min = np.min(g)
        g_max = np.max(g[g != np.inf])

        # Construção da RCL (Restricted Candidate List)
        threshold = g_min + alpha * (g_max - g_min)
        rcl = np.where(g <= threshold)[0]

        if len(rcl) > 0:
            k_current = np.random.choice(rcl)
            s[k_current] = z[k_current]
            unfixed = unfixed[unfixed != k_current]

    return s

def GRASP(control,decoder):
    # Parâmetros GRASP
    s =  np.random.rand(decoder.instance.num_nodes)  # solução
    s_fit = decoder.decode(s)
    sCurrent = s.copy()  # solução atual
    sBest = s.copy()  # melhor solução do C-GRASP
    sBest_fit = s_fit
    sigma = 0.2  # taxa de greedy
    h = 0.12500  # densidade da grade
    hs = 0.12500  # densidade inicial da grade
    he = 0.00098  # densidade final da grade
    ls = 1  # método de busca local
    improv = 0 

    # Número de pontos na grade e pontos examinados
    numGridPoints = int(np.floor(len(s) * (1.0 / h)))
    numExaminedPoints = 0

    # Tempo computacional do processo de busca
    currentTime = 0

     # Controle offline
    if control == 0:
        sigma = 0.2
        ls = 1

    iter = 0  # iterador de iteração
      # Executar o processo de busca até o critério de parada (maxTime)
    while True:
        h = hs
        while h >= he:
            iter += 1
            improv +=1
            numExaminedPoints += 1

            # Controle offline
            if control == 0:
                sigma = np.random.uniform(0.1, 0.9)

            # Construir uma solução GRASP
            s = ConstrutiveGreedyRandomized(s, h, sigma,decoder)
            s_fit = decoder.decode(s)

            # Aplicar busca local na solução atual
            if ls == 1:
                s,s_fit = GridSearch(s, h,decoder)
            elif ls == 2:
                pass
                #s = NelderMeadSearch(sBest, sCurrent, s, h)
            elif ls == 3:
                pass
                #RVND(s)

            # Atualizar a melhor solução encontrada pelo GRASP
            if s_fit < sBest_fit:
                sBest = s.copy()
                sBest_fit = s_fit
                improv = 0


            # Tornar a grade mais densa
            else:
                h = h / 2

            # Critério de parada
            if improv >= 50:
                break


        # Terminar o processo de busca
        if improv >= 50:
            break
    return sBest,s_fit
