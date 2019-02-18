from probability import sample

if __name__ == "__main__":
    # the initial distribution - to decide what happens first
    initialDistribution = {
        "A": 1,
        "E": 1
    }

    # the transition matrix - to decide what happens next
    transitionMatrix = {
        "A":  {
            "A": 0.6,
            "E": 0.4
        },
        "E": {
            "A": 0.7,
            "E": 0.3
        }
    }

    # first, we decide the initial state
    sequence = sample(initialDistribution)

    # then, we'll decide the next 10 states...
    for x in range(10):
        # find the probabilities for the next state
        state = sequence[-1]
        nextDistr = transitionMatrix[state]

        # then decide the outcome
        sequence += sample(nextDistr)

    print("Output sequence: {}".format(sequence))

