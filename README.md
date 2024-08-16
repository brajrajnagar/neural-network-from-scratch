# neural-network-from-scratch
![Neural Network](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*N8UXaiUKWurFLdmEhEHiWg.jpeg)

>_God Bias:When an algorithm or neural network inherits flaws of it's human creator.― Clyde DeSouza, Maya_
## Define the Neural Network Class:

Create a class **NeuralNetwork** in network.py.<br />
Define methods for initialization, forward pass, and backward pass.<br />

## Implement Activation Functions in utils.py:
* [_Sigmoid_](https://pytorch.org/docs/stable/generated/torch.nn.Sigmoid.html#torch.nn.Sigmoid) <br />
    * nn.Sigmoid()
* [_ReLU_](https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html#relu) <br />
    * nn.ReLU()
* [_Tanh_][link 1] <br />
    * nn.Tanh()
* [_Softmax_][link 2] <br />
    * nn.Softmax(dim=1)

## Implement Loss Functions in utils.py:
1. Mean Squared Error (MSE) <br />
2. Cross-Entropy Loss <br />

## Implement the Forward Pass:

Define the forward pass method in your NeuralNetwork class. <br />

## Implement the Backward Pass (Backpropagation):

Define the backward pass method in your NeuralNetwork class. <br />

## Training the Neural Network
Create a Training Loop in main.py: <br />

Load and preprocess your dataset.  
Initialize the neural network.  
Implement the training loop.  
Print training progress.

## Evaluate the Neural Network: 

Implement an evaluation method to test the network on a validation dataset. <br />

[link 1]: https://pytorch.org/docs/stable/generated/torch.nn.Tanh.html#tanh
[link 2]: https://pytorch.org/docs/stable/generated/torch.nn.Softmax.html#softmax