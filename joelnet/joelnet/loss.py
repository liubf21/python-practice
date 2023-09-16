"""
A loss function measures how good our predictions are,
we can use this to adjust the parameters of our network.
"""
import numpy as np
from joelnet.tensor import Tensor

class Loss:
    def loss(self, predicted: Tensor, actual: Tensor) -> float:
        """Calculates the degree by which the prediction missed the actual"""
        raise NotImplementedError
    
    def grad(self, predicted: Tensor, actual: Tensor) -> Tensor:
        """Calculates how to change the prediction to reduce the loss"""
        raise NotImplementedError
    
class MSE(Loss):
    """
    MSE is mean squared error, although we actually
    return the total squared error
    """
    def loss(self, predicted: Tensor, actual: Tensor) -> float:
        # predicted and actual are same shape
        return np.sum((predicted - actual)**2)
    
    def grad(self, predicted: Tensor, actual: Tensor) -> Tensor:
        return 2 * (predicted - actual)
    
class MAE(Loss):
    """
    MAE is mean absolute error
    """
    def loss(self, predicted: Tensor, actual: Tensor) -> float:
        return np.sum(np.abs(predicted - actual))
    
    def grad(self, predicted: Tensor, actual: Tensor) -> Tensor:
        return np.sign(predicted - actual)
    
class CrossEntropy(Loss):
    """
    Cross entropy loss is used for classification.
    The correct class should have probability 1, and the incorrect classes
    should have probability 0.
    """
    def loss(self, predicted: Tensor, actual: Tensor) -> float:
        # Apply softmax to get probabilities from logits
        softmax = np.exp(predicted) / np.exp(predicted).sum(axis=1, keepdims=True)
        # Clip values to avoid log(0) error
        softmax = np.clip(softmax, 1e-7, 1 - 1e-7)
        # Actual is one-hot encoded, so multiply by softmax to get the log probability of the correct class
        log_likelihood = -np.log(np.sum(softmax * actual, axis=1))
        return np.sum(log_likelihood)
    
    def grad(self, predicted: Tensor, actual: Tensor) -> Tensor:
        softmax = np.exp(predicted) / np.exp(predicted).sum(axis=1, keepdims=True)
        return softmax - actual