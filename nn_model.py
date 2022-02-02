import numpy as np


test_input = [
    np.array([0,1]),np.array([1,0]),np.array([1,1]),np.array([0,0])
]

test_output = [1,1,0,0]

class Neural_Network(object):
    def __init__(self):
        self.inputSize = 2
        self.outputSize = 1
        self.hiddenSize = 3
        #self.hidden2Size = 20000

        self.w1 = np.random.randn(self.inputSize,self.hiddenSize) #Mat(40000,80000)
        self.w2 = np.random.randn(self.hiddenSize,self.outputSize) #Mat(80000,80000)
        #self.w3 = np.random.randn(self.hidden2Size,self.outputSize) #Mat(80000,2)

    def forward(self,X):

        self.l1 = np.dot(X, self.w1)
        self.al1 = self.sigmoid(self.l1)

        self.o = np.dot(self.al1,self.w2)

        output = self.sigmoid(self.o)

        return output

        #self.l2 = np.dot(self.al1,self.w2)
        #self.al2 = self.sigmoid(self.l2)

        #self.o = np.dot(self.al2,self.w3)
        #ao = self.sigmoid(self.o)

        #return ao
    
    def sigmoid(self,s):
        return 1/(1+np.exp(-s))

    def sigmoid_prime(self,s):
        return self.sigmoid(s)*(1-self.sigmoid(s))

    def train (self, input , expected_output , step):
        output = self.forward(input)
        cost = (abs(expected_output - output)**2)/2



NN1 = Neural_Network()

print(NN1.forward(test_input[0]))


        

