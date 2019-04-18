import numpy as np


class MLP(object):
    """A Multilayer Perceptron class.
    """

    def __init__(self, numInputs=3, hiddenLayers=(3, 3), numOutputs=1):
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
        layers = [numInputs] + list(hiddenLayers) + [numOutputs]

        # create random connections for the layers
        weights = []
        for i in range(len(layers)-1):
            w = np.random.rand(layers[i], layers[i+1])
            weights.append(w)
        self.weights = weights

        # save activations/errors per layer
        activations = []
        errors = []
        for i in range(len(layers)):
            a = np.zeros(layers[i])
            e = a[:]
            activations.append(a)
            errors.append(e)
        self.activations = activations
        self.errors = errors

        # save derivatives per layer
        derivatives = []
        for i in range(len(layers) - 1):
            d = np.zeros(layers[i+1])
            derivatives.append(d)
        self.derivatives = derivatives

    def activate(self, input):
        """Computes activation of the network based on input signals.

        Args:
            input (list): Input signals

        Returns:
            output (list): Output values
        """

        # the input layer activation is just the input itself
        activation = input
        # save the activation for backpropogation
        self.activations[0][:] = activation

        # iterate through the network layers
        for i in range(len(self.weights)):
            # calculate dot product between previous activation and weights
            dotProduct = np.dot(activation, self.weights[i])

            # apply sigmoid activation function
            activation = self._sigmoid(dotProduct)

            # save the activation for backpropogation
            self.activations[i+1][:] = activation

        # return output layer activation
        return activation[0, :]

    def backActivate(self, error):
        """Backpropogates an error signal.

        Args:
            error (ndarray): The error to backprop.

        Returns:
            error (float): The final error of the input
        """

        # save the error
        self.errors[-1][:] = error

        # iterate backwards through the network layers
        for i in reversed(range(len(self.derivatives))):

            # get the last activation for the current layer
            activation = self.activations[i+1]

            # apply sigmoid derivative function
            delta = error * self._sigmoidPrime(activation)
            # save the derivative for gradient descent
            self.derivatives[i][:] = delta

            # backpropogate the next error
            error = np.dot(delta, self.weights[i].T)

            # save the error
            self.errors[i][:] = error

        return error

    def gradientDescent(self, learningRate=1):
        """Learns by descending the gradient

        Args:
            learningRate (float): How fast to learn.
        """
        # update the weights by stepping down the gradient
        for i in range(len(self.weights)):
            weights = self.weights[i]
            activations = self.activations[i+1]
            derivatives = self.derivatives[i]
            weights -= np.dot(activations, derivatives) * learningRate

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

    @staticmethod
    def _sigmoidPrime(x):
        return x * (1.0 - x)
