"""Implement a simple Multi-Layer Perceptron with N binary inputs, two
hidden layers and one binary output. Display the final weight matrices, bias
values and the number of steps. Note that random values are assigned to
weight matrices and bias in each step. """

import numpy as np

# Activation function (binary step function)
def binary_step(x):
    return np.where(x >= 0, 1, 0)

# Forward pass through the network
def forward_pass(x, weights1, bias1, weights2, bias2, weights3, bias3):
    hidden1 = binary_step(np.dot(x, weights1) + bias1)
    hidden2 = binary_step(np.dot(hidden1, weights2) + bias2)
    output = binary_step(np.dot(hidden2, weights3) + bias3)
    return output, hidden1, hidden2


x = np.array([1, 0])  # Example input vector
# Randomly initialized weights and biases
weights1 = np.random.randn(2, 4)   # input layer -> first hidden layer
bias1 = np.random.randn(4)
weights2 = np.random.randn(4, 3)   # first hidden layer -> second hidden layer
bias2 = np.random.randn(3)
weights3 = np.random.randn(3, 1)   # second hidden layer -> output layer
bias3 = np.random.randn(1)
# Perform forward pass
output, hidden1, hidden2 = forward_pass(x, weights1, bias1, weights2, bias2, weights3, bias3)
# Show results
print("Input:", x)
print("Hidden Layer 1 Output:", hidden1)
print("Hidden Layer 2 Output:", hidden2)
print("Final Output:", output)
