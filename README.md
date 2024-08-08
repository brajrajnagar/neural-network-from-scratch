# neural-network-from-scratch
![Neural Network](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*N8UXaiUKWurFLdmEhEHiWg.jpeg)

## Define the Neural Network Class:

Create a class **NeuralNetwork** in network.py.<br />
Define methods for initialization, forward pass, and backward pass.<br />

## Implement Activation Functions in utils.py:
[_Sigmoid_](https://pytorch.org/docs/stable/generated/torch.nn.Sigmoid.html#torch.nn.Sigmoid) <br />
[_ReLU_](https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html#relu) <br />
[_Tanh_][link 1] <br />
[_Softmax_][link 2] <br />

## Implement Loss Functions in utils.py:
Mean Squared Error (MSE) <br />
Cross-Entropy Loss <br />

## Implement the Forward Pass:

Define the forward pass method in your NeuralNetwork class. <br />

## Implement the Backward Pass (Backpropagation):

Define the backward pass method in your NeuralNetwork class. <br />

## Training the Neural Network
Create a Training Loop in main.py: <br />

Load and preprocess your dataset. <br />
Initialize the neural network. <br />
Implement the training loop. <br />
Print training progress. <br />

## Evaluate the Neural Network: 

Implement an evaluation method to test the network on a validation dataset. <br />

[link 1]: https://pytorch.org/docs/stable/generated/torch.nn.Tanh.html#tanh
[link 2]: https://pytorch.org/docs/stable/generated/torch.nn.Softmax.html#softmax