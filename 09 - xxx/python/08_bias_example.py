import numpy as np
from random import random, shuffle


class MLP(object):
    """A Multilayer Perceptron class with bias.
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

        numWeights = len(layers)-1
        # create weights
        weights = []

        # create biases
        biases = []
        biasErrors = []
        for i in range(numWeights):
            n1 = layers[i]
            n2 = layers[i+1]

            w = np.random.rand(n1, n2) * 2 - 1
            weights.append(w)

            # create bias connection?
            if i < numWeights-1:
                w = np.random.rand(n2) * 2 - 1
                biases.append(w)
                e = np.zeros(n2)
                biasErrors.append(e)

        self.weights = weights
        self.biases = biases
        self.biasErrors = biasErrors

        # save activations/errors per layer
        activations = []
        errors = []
        numLayers = len(layers)
        for i in range(numLayers):
            n = layers[i]
            a = np.zeros(n)
            activations.append(a)
            errors.append(a[:])

        self.activations = activations
        self.errors = errors

        # save derivatives per layer
        derivatives = []
        for i in range(numLayers-1):
            n = layers[i+1]
            d = np.zeros(n)
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
        numLayers = len(self.weights)
        for i in range(numLayers):

            # get pointer to weights and biases
            ws = self.weights[i]

            # simply the dot product between previous activation and weights
            dotProduct = np.dot(activation, ws)

            # add the bias
            if i < numLayers-1:
                bs = self.biases[i]
                dotProduct += bs

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
        numLayers = len(self.derivatives)
        for i in reversed(range(numLayers)):

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
            # save the bias error
            if i < numLayers-1:
                self.biasErrors[i][:] = np.dot(delta, self.biases[i].T)

        return error

    def gradientDescent(self, learningRate=1):
        """Learns by descending the gradient

        Args:
            learningRate (float): How fast to learn.
        """
        # update the weights by stepping down the gradient
        numLayers = len(self.weights)
        for i in range(numLayers):
            weights = self.weights[i]
            activations = self.activations[i+1]
            derivatives = self.derivatives[i]
            weights -= np.dot(activations, derivatives) * learningRate
            # weights += derivatives * learningRate

            # update biases
            if i < numLayers-1:
                biases = self.biases[i]
                biasesErrors = self.biasErrors[i]
                biases -= biasesErrors * learningRate

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


def mse(target, output):
    """Mean Squared Error loss function

    Args:
        target (ndarray): The ground truth
        output (ndarray): The predicted values

    Returns:
        (float): Output
    """
    return np.average((target - output) ** 2, axis=0)


def train(mlp, items, targets, learningRate=0.1, epochs=50):
    lastError = 0

    # now enter the training loop
    for i in range(epochs):
        sumErrors = 0

        # iterate through all the training data
        for j, input in enumerate(items):
            target = targets[j]

            # activate the network!
            output = mlp.activate(input)

            # get the error derivative
            error = output - target

            # backpropogate this error
            mlp.backActivate(error)

            # keep track of the MSE for reporting later
            sumErrors += mse(target, output)

            # now perform gradient descent on the derivatives
            # (this will update the weights
            mlp.gradientDescent(learningRate)

        # Epoch complete, report the training error
        lastError = sumErrors / len(items)

        # uncomment this line if you want to "see the AI"
        # print(lastError)

    return lastError


if __name__ == "__main__":

    # create a dataset, this is a simple 1-x approximation
    Ns = [10, 100, 500]

    for N in Ns:
        items = [x/N for x in range(N)]
        error = 0

        # train 10 networks
        for i in range(10):
            shuffle(items)
            targets = [1-x for x in items]

            # create a Multilayer Perceptron with one hidden layer
            mlp = MLP(1, (3, ), 1)

            # train the network
            err = train(mlp, items, targets)

            # keep track of the error
            error += err

        # Finally, report the average error
        print("N={}\tAverage error: {}".format(N, error/10))

