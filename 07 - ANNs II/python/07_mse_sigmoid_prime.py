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


def sigmoidPrime(x):
    return x * (1.0 - x)


if __name__ == "__main__":
    y = sigmoid(0.5)
    print(y)
    x = sigmoidPrime(y)
    print(x)