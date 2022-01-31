from cmath import exp
import numpy as np
from create_nn_input import Matvvt1

class Neural_Network(object):
    def __init__(self):
        self.inputSize = 40000
        self.outputSize = 2
        self.hidden1Size = 20000
        self.hidden2Size = 20000

        self.w1 = np.random.randn(self.inputSize,self.hidden1Size) #Mat(40000,80000)
        self.w2 = np.random.randn(self.hidden1Size,self.hidden2Size) #Mat(80000,80000)
        self.w3 = np.random.randn(self.hidden2Size,self.outputSize) #Mat(80000,2)

    def forward(self,X):

        self.l1 = np.dot(X, self.w1)
        self.al1 = self.sigmoid(self.l1)

        self.l2 = np.dot(self.al1,self.w2)
        self.al2 = self.sigmoid(self.l2)

        self.o = np.dot(self.al2,self.w3)
        ao = self.sigmoid(self.o)

        return ao
    
    def sigmoid(self,s):
        return 1/(1+exp(-s))

    def sigmoid_prime(self,s):
        return self.sigmoid(s)*(1-self.sigmoid(s))

NN1 = Neural_Network()

print(NN1.forward(Matvvt1))


        

