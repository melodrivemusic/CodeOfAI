# We can use the numpy library to make the maths a little easier.
# Install it with pip if you haven't already!
import numpy as np


class MLP(object):
    """A Multilayer Perceptron class.
    """

    def __init__(self, numInputs=3, numHidden=3, numOutputs=1):
        """Constructor for the MLP. Takes the number of inputs,
            number of neurons in the hidden layer, and number of outputs

        Args:
            numInputs (int): Number of inputs
            numHidden (int): Number of neurons in the hidden layer
            numOutputs (int): Number of outputs
        """

        self.numInputs = numInputs
        self.numHidden = numHidden
        self.numOutputs = numOutputs

        # randomise weights within the network
        # np.random.rand produces a NxM array of floats
        self.weights = (
            np.random.rand(numInputs, numHidden),
            np.random.rand(numHidden, numOutputs)
        )

    def activate(self, inputs):
        """Computes activation of the network based on input signals.

        Args:
            inputs (list): Input signals

        Returns:
            output (list): Output values
        """
        # calculate dot product between input layer and hidden layer
        dotProduct1 = np.dot(inputs, self.weights[0])

        # apply sigmoid activation function
        hiddenActivation = self._sigmoid(dotProduct1)

        # calculate dot product between hidden layer and 2nd layer of weights
        dotProduct2 = np.dot(hiddenActivation, self.weights[1])

        # apply sigmoid activation function
        return self._sigmoid(dotProduct2)

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

