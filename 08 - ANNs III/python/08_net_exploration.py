from random import shuffle
from ml.mlp import MLP
from ml.train import train


def getNumParameters(numInputs=1, hiddenLayers=(3,), numOutputs=1):
    """Calculates the number of trainable parameters in an MLP

    Args:
        numInputs (int): Number of inputs
        hiddenLayers (list): A list of ints for the hidden layers
        numOutputs (int): Number of outputs

    Returns:
        (int): The number of parameters
    """
    # input to first hidden layer
    numParams = numInputs * hl[0]

    # hidden layer connections
    numLayers = len(hiddenLayers)
    if numLayers > 1:
        for i in range(numLayers-1):
            numParams += hiddenLayers[i]*hiddenLayers[i+1]

    # last hidden layer to output
    numParams += hl[-1] * numOutputs
    return numParams


if __name__ == "__main__":

    # create a dataset, this is a simple 1-x approximation
    N = 100
    items = [x/N for x in range(N)]
    shuffle(items)
    targets = [1-x for x in items]

    hiddenLayers = [(1, ), (3, ), (3, 2), (9, 6), (32, 16)]

    for hl in hiddenLayers:
        error = 0

        # train 10 networks
        for i in range(10):

            # create a Multilayer Perceptron
            mlp = MLP(1, hl, 1)

            # train the network
            err = train(mlp, items, targets)

            # keep track of the error
            error += err

        # calculate the number of parameters
        numParams = getNumParameters(hiddenLayers=hl)

        # Finally, report the average error
        print("{}\t{}\t{:.6f}".format(hl, numParams, error/10))

