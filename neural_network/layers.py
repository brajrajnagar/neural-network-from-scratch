import numpy as np

class DenseLayer:
    def __init__(self, input_size, output_size) -> None:
        self.weights = np.random.randn(input_size, output_size)*0.01
        self.biases = np.zeros(1, output_size)

    def forward(self, input):
        self.input = input
        return np.dot(self.input, self.weights) + self.biases
    
    def backward(self, dvalues, learning_rate):
        # Gradient with respect to weights and biases
        self.dweights = np.dot(self.inputs.T, dvalues)
        self.dbiases = np.sum(dvalues, axis=0, keepdims=True)
        
        # Gradient with respect to input data (to pass to the previous layer)
        self.dinputs = np.dot(dvalues, self.weights.T)
        
        # Update weights and biases
        self.weights -= learning_rate * self.dweights
        self.biases -= learning_rate * self.dbiases