"""
A NeuralNetwork is just a collection of layers.
It behaves a lot like a layer itself, although
we're not going to make it one.
"""
from typing import Sequence, Iterator, Tuple
from joelnet.tensor import Tensor
from joelnet.layers import Layer

class NeuralNet:
    def __init__(self, layers: Sequence[Layer]) -> None:
        self.layers = layers
    
    def forward(self, inputs: Tensor) -> Tensor:
        """
        Passes inputs through the layers in order.
        """
        for layer in self.layers:
            inputs = layer.forward(inputs)
        return inputs
    
    def backward(self, grad: Tensor) -> Tensor:
        """
        Passes gradients through the layers in reverse order.
        """
        for layer in reversed(self.layers):
            grad = layer.backward(grad)
        return grad
    
    def params_and_grads(self) -> Iterator[Tuple[Tensor, Tensor]]:
        """
        Extracts the parameters and gradients from each layer.
        """
        for layer in self.layers:
            for name, param in layer.params.items():
                grad = layer.grads[name]
                yield param, grad