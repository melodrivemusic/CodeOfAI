import numpy as np

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
    """Trains an MLP with its gradientDescent method

    Args:
        mlp (MLP): The MLP
        items (array): The training input
        targets (array): The training target
        learningRate (float): The learning rate passed to gradient descent
        epochs (int): How many training epochs to run

    Returns:
        (float): The final error
    """
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
