# neural-network-from-scratch
## Define the Neural Network Class:

Create a class **NeuralNetwork** in network.py.
Define methods for initialization, forward pass, and backward pass.

## Implement Activation Functions in utils.py:
[_Sigmoid_](https://pytorch.org/docs/stable/generated/torch.nn.Sigmoid.html#torch.nn.Sigmoid)
[_ReLU_](https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html#relu)
[_Tanh_][link 1]
[_Softmax_][link 2]

## Implement Loss Functions in utils.py:
Mean Squared Error (MSE)
Cross-Entropy Loss
Implement the Forward Pass:

Define the forward pass method in your NeuralNetwork class.
Implement the Backward Pass (Backpropagation):

Define the backward pass method in your NeuralNetwork class.

## Training the Neural Network
Create a Training Loop in main.py:

Load and preprocess your dataset.
Initialize the neural network.
Implement the training loop.
Print training progress.
Evaluate the Neural Network:

Implement an evaluation method to test the network on a validation dataset.

[link 1]: https://pytorch.org/docs/stable/generated/torch.nn.Tanh.html#tanh
[link 2]: https://pytorch.org/docs/stable/generated/torch.nn.Softmax.html#softmax