import numpy as np


class MLP(object):
    """A Multilayer Perceptron class.
    """

    def __init__(self, numInputs=3, hiddenLayers=[3, 3], numOutputs=1):
        """Constructor for the MLP. Takes the number of inputs,
            a variable number of hidden layers, and number of outputs

        Args:
            numInputs (int): Number of inputs
            hiddenLayers (list): A list of ints for the hidden layers
            numOutputs (int): Number of outputs
        """

        self.numInputs = numInputs
        self.hiddenLayers = hiddenLayers
        self.numOutputs = numOutputs

        # create a generic representation of the layers
        layers = [numInputs] + hiddenLayers + [numOutputs]

        # create random connections for the layers
        weights = []
        for i in range(len(layers)-1):
            w = np.random.rand(layers[i], layers[i+1])
            weights.append(w)
        self.weights = weights

    def activate(self, inputs):
        """Computes activation of the network based on input signals.

        Args:
            inputs (list): Input signals

        Returns:
            output (list): Output values
        """

        # the input layer activation is just the input itself
        activation = inputs

        # iterate through the network layers
        for i in range(len(self.weights)):
            # calculate dot product between previous activation and weights
            dotProduct = np.dot(activation, self.weights[i])

            # apply sigmoid activation function
            activation = self._sigmoid(dotProduct)

        # return output layer activation
        return activation

    @staticmethod
    def _sigmoid(x):
        """Sigmoid activation function

        Args:
            x (float): Value to be processed

        Returns:
            y (float): Output
        """
        y = 1.0 / (1 + np.exp(-x))
        return y


if __name__ == "__main__":
    # create a Multilayer Perceptron
    mlp = MLP()

    # set random values for network's input
    inputs = np.random.rand(mlp.numInputs)

    # activate the network!
    output = mlp.activate(inputs)

    print("Network activation: {}".format(output))

