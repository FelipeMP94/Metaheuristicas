import numpy as np
class TSPDecoder():
    """
    Simple Traveling Salesman Problem decoder. It creates a permutation of
    nodes induced by the chromosome and computes the cost of the tour.
    """

    def __init__(self, instance):
        self.instance = instance

    ###########################################################################

    def decode(self, chromosome) -> float:
        """
        Given a chromossome, builds a tour.

        Note that in this example, ``rewrite`` has not been used.
        """
        indices = np.argsort(chromosome)

       

        cost = self.instance.distance(indices[0], indices[-1])
        for i in range(len(indices) - 1):
            cost += self.instance.distance(indices[i],
                                           indices[i + 1])
        return cost