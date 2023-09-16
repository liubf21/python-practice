"""
Here's a function that can train a neural net
"""

from joelnet.tensor import Tensor
from joelnet.nn import NeuralNet
from joelnet.loss import Loss, MSE
from joelnet.optim import Optimizer, SGD
from joelnet.data import DataIterator, BatchIterator

def train(net: NeuralNet,
            inputs: Tensor,
            targets: Tensor,
            num_epochs: int = 5000,
            iterator: DataIterator = BatchIterator(),
            loss: Loss = MSE(),
            optimizer: Optimizer = SGD()) -> None:
        for epoch in range(num_epochs):
            epoch_loss = 0.0
            for batch in iterator(inputs, targets):
                predicted = net.forward(batch.inputs) # get predictions from the network
                epoch_loss += loss.loss(predicted, batch.targets)
                grad = loss.grad(predicted, batch.targets) # get the gradient of the loss
                net.backward(grad) # pass gradients back into the network, updating gradients of weights
                optimizer.step(net) # take a step with the optimizer
            
            if epoch % 100 == 0:
                print(epoch, epoch_loss)
