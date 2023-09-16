"""
The canonical example of a problem that can't be 
solved with a linear model is XOR.
"""
import numpy as np

from joelnet.train import train
from joelnet.nn import NeuralNet
from joelnet.layers import Linear, Tanh

inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

targets = np.array([
    [0],
    [1],
    [1],
    [0]
])

net = NeuralNet([
    Linear(input_size=2, output_size=2),
    # Tanh(),
    Linear(input_size=2, output_size=1)
])

train(net, inputs, targets)

for x, y in zip(inputs, targets):
    predicted = net.forward(x)
    print(x, predicted, y)