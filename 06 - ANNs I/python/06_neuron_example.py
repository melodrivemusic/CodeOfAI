import math


def sigmoid(x):
    """Sigmoid activation function

    Args:
        x (float): Value to be processed

    Returns:
        y (float): Output
    """
    y = 1.0 / (1 + math.exp(-x))
    return y


def activate(inputs, weights):
    """Computes activation of neuron based on input signals and connection
    weights. Output = f(x_1*w_1 + x_2*w_2 + ... + x_k*w_k), where 'f' is the
    sigmoid function.

    Args:
        inputs (list): Input signals
        weights (list): Connection weights

    Returns:
        output (float): Output value
    """

    s = 0

    # compute the sum of the product of the input signals and the weights
    # here we're using pythons "zip" function to iterate two lists together
    for x, w in zip(inputs, weights):
        s += x*w

    # process sum through sigmoid activation function
    return sigmoid(s)


if __name__ == "__main__":

    # value of neuron's input
    inputs = [0.3, 0.4, 0.5]

    # weights of connections between input and neuron
    weights = [0.4, 0.7, 0.2]

    # activate the neuron!
    output = activate(inputs, weights)

    print("Neuron activation: {}".format(output))
