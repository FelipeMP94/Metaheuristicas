import numpy as np
import nltk

class PMED_instance:
    def __init__(self,path):
        self.inf = 9999999
        self.path = path
        self.parameters = np.array([],dtype=int)
        arq = open(self.path)
        self.data = arq.readlines()
        extract_params = nltk.word_tokenize(self.data.pop(0))
        for e in extract_params:
            self.parameters =  np.append(self.parameters,int(e))

        self.dist = np.array([[self.inf]*self.parameters[0]]*self.parameters[0])
        for i in np.arange(self.parameters[0]):
            self.dist[i][i] = 0

        for i in np.arange(len(self.data)):
            tolkens = nltk.word_tokenize(self.data[i])
            self.dist[int(tolkens[0])-1][int(tolkens[1])-1] = int(tolkens[2])
            self.dist[int(tolkens[1])-1][int(tolkens[0])-1] = int(tolkens[2])


        for k in np.arange(self.parameters[0]):
            for i in np.arange(self.parameters[0]):
                for j in np.arange(self.parameters[0]):
                    if self.dist[i][k]+self.dist[k][j] <self.dist[i][j]:
                        self.dist[i][j] = self.dist[i][k]+self.dist[k][j]

