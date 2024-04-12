from M_Grasp import linesearch
import numpy as np
from TSP_decoder import TSPDecoder
from TSP_instance import TSPInstance

if __name__ == "__main__":
    instance = TSPInstance(r"burma14.dat")
    decoder = TSPDecoder(instance)
    ind = np.random.rand(instance.num_nodes)
    fit = decoder.decode(ind)
    novo,novo_fit = linesearch(ind,0.95,0,decoder)
    print(f'Solução inicial: {ind} \nCusto inicial: {fit}\n')
    print(f'Solução Nova: {novo} \nCusto novo: {novo_fit}')
    print(decoder.decode(novo))
    print(decoder.decode(ind))