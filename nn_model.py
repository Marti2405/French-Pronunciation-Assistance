import numpy as np
import os 
from locations import *
from create_nn_input_fv import create_nn_input_fv as inp


#-----------------PATH for importing the weights--------------------
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
loc1 = os.path.join(__location__, 'Weights_Neural_Network\\w1.npy')
loc2 = os.path.join(__location__, 'Weights_Neural_Network\\w2.npy')
#-------------------------------------------------------------------



#--------Neural Network object-----------

class Neural_Network(object):
    def __init__(self):
        self.inputSize = 1000
        self.outputSize = 1
        self.hiddenSize = 500
        self.w1 = np.load(loc1) 
        self.w2 = np.load(loc2)

    def forward(self,X):

        self.l1 = np.dot(X, self.w1)
        self.al1 = self.sigmoid(self.l1)
        self.o = np.dot(self.al1,self.w2)
        output = self.sigmoid(self.o)
        return output

    def backward(self,X,y,o):
        self.o_error = y - o
        self.o_delta = self.o_error * self.sigmoid_prime(self.sigmoid(o))
        self.z2_error = self.o_delta.dot(self.w2.T)
        self.z2_delta = self.z2_error * self.sigmoid_prime(self.al1)
        self.w1 += X.T.dot(self.z2_delta)
        self.w2 += self.al1.T.dot(self.o_delta)
    
    def sigmoid(self,s):
        return 1/(1+np.exp(-s))

    def sigmoid_prime(self,s):
        return s*(1-s)
    
    def train(self,X,y,n): 
        for _ in range(n):    
            o2 = self.forward(X)
            self.backward(X,y,o2)
    
    def save_weights(self):
        np.save(loc1, self.w1)
        np.save(loc2, self.w2)

    
X = np.array(([inp(fft1)]),dtype=float)
X = np.append(X,[inp(v3)],axis=0)
X = np.append(X,[inp(fem1)],axis=0)
X = np.append(X,[inp(v2)],axis=0)
X = np.append(X,[inp(f2)],axis=0)
X = np.append(X,[inp(vem1)],axis=0)
X = np.append(X,[inp(f3)],axis=0)
X = np.append(X,[inp(vvt1)],axis=0)
X = np.append(X,[inp(f1)],axis=0)
X = np.append(X,[inp(v1)],axis=0)
Y = np.array(([1],[0],[1],[0],[1],[0],[1],[0],[1],[0]),dtype=float) # f=1 , v=0

AI1 = Neural_Network()
#AI1.train(X,Y,20000)
#AI1.save_weights()

def lettre(c):
    if c>0.5:
        return "C'est un f!"
    elif c<0.5:
        return "C'est un v!"
    else:
        return "Je suis pas sur de la lettre..."


def prediction(nom):
    pred = AI1.forward(inp(audio(nom)))
    print(f"Prediction pour le fichier {nom} : ",lettre(pred) , " , Valeur : " , np.round(pred[0] ,4)*100 ,"%")

for i in fichiers:
    prediction(i)










        

