from random import shuffle
from ml.mlp import MLP
from ml.train import train


if __name__ == "__main__":

    # create a dataset, this is a simple 1-x approximation
    N = 100
    items = [x/N for x in range(N)]
    shuffle(items)
    targets = [1-x for x in items]

    learningRates = [0.1, 0.3, 1.0, 3.0]

    for lr in learningRates:
        error = 0

        # train 10 networks
        for i in range(10):

            # create a Multilayer Perceptron with one hidden layer
            mlp = MLP(1, (3, ), 1)

            # train the network
            err = train(mlp, items, targets, lr)

            # keep track of the error
            error += err

        # Finally, report the average error
        print("{}\t{:.6f}".format(lr, error/10))

