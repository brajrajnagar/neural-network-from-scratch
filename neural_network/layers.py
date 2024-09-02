# layers.py

import numpy as np

class DenseLayer:
    def __init__(self, input_size, output_size):
        """
        Initialize the layer with random weights and biases.
        
        Parameters:
        input_size (int): Number of input features.
        output_size (int): Number of output neurons.
        """
        self.weights = np.random.randn(input_size, output_size) * 0.01
        self.biases = np.zeros((1, output_size))

    def forward(self, inputs):
        """
        Perform the forward pass through the layer.
        
        Parameters:
        inputs (ndarray): Input data (batch_size, input_size).
        
        Returns:
        ndarray: Output data after applying the linear transformation.
        """
        self.inputs = inputs
        return np.dot(inputs, self.weights) + self.biases

    def backward(self, dvalues, learning_rate):
        """
        Perform the backward pass and update the weights and biases.
        
        Parameters:
        dvalues (ndarray): Gradient of the loss with respect to the output of this layer.
        learning_rate (float): Learning rate for updating the parameters.
        """
        # Gradient with respect to weights and biases
        self.dweights = np.dot(self.inputs.T, dvalues)
        self.dbiases = np.sum(dvalues, axis=0, keepdims=True)
        
        # Gradient with respect to input data (to pass to the previous layer)
        self.dinputs = np.dot(dvalues, self.weights.T)
        
        # Update weights and biases
        self.weights -= learning_rate * self.dweights
        self.biases -= learning_rate * self.dbiases

