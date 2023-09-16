"""
We use an optimizer to adjust the parameters 
of our network based on the gradients 
computed during backpropagation.
"""
from joelnet.nn import NeuralNet    

class Optimizer:
    def step(self, net: NeuralNet) -> None:
        raise NotImplementedError
    
class SGD(Optimizer):
    """
    Stochastic gradient descent
    Stochastic because we use only a subset (a batch) of the data
    """
    def __init__(self, lr: float = 0.01) -> None:
        self.lr = lr
    
    def step(self, net: NeuralNet) -> None:
        for param, grad in net.params_and_grads():
            param -= self.lr * grad # gradient descent
