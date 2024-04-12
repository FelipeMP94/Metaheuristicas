import numpy as np

def linesearch(choromossome,h,i,decoder):
    bestZ = choromossome
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
    print(f'RK: {rk}')
    for j in range(q):
        print(f'{choromossome[i]}  {rk[j]}')
        choromossome[i] = rk[j]
        fit = decoder.decode(choromossome)
        if fit < bestF:
            bestZ = choromossome
            bestF = fit
    return bestZ,bestF