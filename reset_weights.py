import numpy as np
import os 

# Fonction to reset random weights 
def reset_weigths():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    loc = os.path.join(__location__, 'Weights_Neural_Network\\w1.npy')
    w = np.random.randn(1000,500)
    np.save(loc,w)
    w = np.random.randn(500,1)
    loc = os.path.join(__location__, 'Weights_Neural_Network\\w2.npy')
    np.save(loc,w)

reset_weigths()