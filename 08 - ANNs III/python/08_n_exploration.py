from random import shuffle
from ml.mlp import MLP
from ml.train import train


if __name__ == "__main__":

    # create a dataset, this is a simple 1-x approximation
    Ns = [10, 100, 500, 1000]

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
        print("N={}:\t{:.6f}".format(N, error/10))

