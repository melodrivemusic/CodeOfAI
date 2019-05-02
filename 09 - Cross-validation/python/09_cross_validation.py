import numpy as np
from random import shuffle
from ml.mlp import MLP


def mse(target, output):
    """Mean Squared Error loss function

    Args:
        target (ndarray): The ground truth
        output (ndarray): The predicted values

    Returns:
        (float): Output
    """
    return np.average((target - output) ** 2, axis=0)


def splitData(x, y, testRatio=0.2):
    """
    Randomly splits testing a training data into train / test chunks
    :param x: The training items
    :param y: The target items
    :param testRatio: The test/train ratio
    :return: tuple of trainX, trainY, testX, testY
    """
    N = len(x)

    # make sure we have an equal number of training examples...
    assert N == len(y)
    # ...and that we have a percentage for the test size
    assert 0 < testRatio < 1

    # calculate how many items in the test set
    nTest = int(testRatio * N)

    # get the data indexes
    idxs = np.arange(N)
    # shuffle them
    shuffle(idxs)

    # split the data
    testIdxs = idxs[:nTest]
    trainIdxs = idxs[nTest:]

    # return the data split
    return x[trainIdxs], y[trainIdxs], x[testIdxs], y[testIdxs]


def crossValidationTrain(mlp, items, targets, testItems, testTargets, learningRate=0.1, epochs=50):
    """Trains an MLP with its gradientDescent method and using cross-validation

    Args:
        mlp (MLP): The MLP
        items (array): The training input
        targets (array): The training target
        testItems (array): The test input
        testTargets (array): The test target
        learningRate (float): The learning rate passed to gradient descent
        epochs (int): How many training epochs to run

    Returns:
        (float): The final error
    """
    lastError = 0
    lastTestError = 1000

    # now enter the training loop
    for i in range(epochs):
        sumErrors = 0

        # train on the training data
        for j, input in enumerate(items):
            target = targets[j]

            output = mlp.activate(input)
            error = output - target
            mlp.backActivate(error)
            sumErrors += mse(target, output)
            mlp.gradientDescent(learningRate)

        # test on the test data
        sumTestErrors = 0
        for j, input in enumerate(testItems):
            target = testTargets[j]

            output = mlp.activate(input)
            sumTestErrors += mse(target, output)

        # Epoch complete, report the training and test error
        lastError = sumErrors / len(items)
        testError = sumTestErrors / len(testItems)

        print("Epoch {}\ttrainErr {:.6f}\ttestErr {:.6f}".format(i, lastError, testError))

        if testError > lastTestError:
            print("Training stopped after {} epochs".format(i+1))
            break

        lastTestError = testError

    return lastError, lastTestError

if __name__ == "__main__":
    # create a dataset, this is a toy one for illustration purposes
    N = 100
    items = np.random.random(N)
    targets = np.array([(1-x)**3 for x in items])

    trainX, trainY, testX, testY = splitData(items, targets)

    print("Data size: {}".format(len(items)))
    print("Train size: {}".format(len(trainX)))
    print("Test size: {}".format(len(testX)))

    mlp = MLP(1, (3, 2), 1)

    # train the network
    err, testErr = crossValidationTrain(mlp, trainX, trainY, testX, testY)
    print("Final trainErr {:.6f}\ttestErr {:.6f}".format(err, testErr))





