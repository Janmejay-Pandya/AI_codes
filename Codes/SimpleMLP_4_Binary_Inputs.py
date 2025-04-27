"""Implement a simple Multi-Layer Perceptron with 4 binary inputs, one
hidden layer and two binary outputs. Display the final weight matrices, bias
values and the number of steps. Note that random values are assigned to
weight matrices and bias in each step."""

import numpy as np

# Binary step activation function
def binary_step(x):
    return np.where(x >= 0, 1, 0)

# Forward pass
def forward_pass(x, w1, b1, w2, b2):
    hidden = binary_step(np.dot(x, w1) + b1)
    output = binary_step(np.dot(hidden, w2) + b2)
    return output, hidden

if __name__ == "__main__":
    # Sample input
    x = np.array([1, 0, 1, 0])

    # Randomly initialized weights and biases
    w1 = np.random.randn(4, 5)  # 4 inputs → 5 hidden neurons
    b1 = np.random.randn(5)

    w2 = np.random.randn(5, 2)  # 5 hidden neurons → 2 output neurons
    b2 = np.random.randn(2)

    # Forward pass
    output, hidden = forward_pass(x, w1, b1, w2, b2)

    # Display results
    print("Input:", x)
    print("Hidden Layer Output:", hidden)
    print("Final Output:", output)
