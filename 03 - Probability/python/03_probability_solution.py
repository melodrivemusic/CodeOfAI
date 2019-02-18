import random
from collections import OrderedDict


def normaliseSum(*args):
    """Returns a list of all the arguments, so that they add up to 1

    Args:
        *args: A variable number of arguments

    Returns:
        (list): list of all the arguments that all add up to 1
    """

    # convert the arguments to a list, so we can operate on it
    args = list(args)

    # calculate the sum of the list
    s = sum(args)

    # this if statement is important, because dividing by 0 is bad!
    if s != 0:
        # return a list on numbers divided by the sum
        return [float(x) / s for x in args]

    # return a list of 0s if the sum is 0
    return [0.0 for x in args]


def normaliseDict(distDict):
    """Returns a new dictionary where the values all add up to 1

    Args:
        distDict (dict): A probability distribution

    Returns:
        norm (dict): a new dictionary where the values all add up to 1
    """

    # get the keys from the disctionary
    keys = list(distDict.keys())

    # normalise the values from the dictionary
    norm = normaliseSum(*distDict.values())

    # create a normalised disctionary
    normalised = {}

    # iterate through the keys and values
    i = 0
    for key in keys:
        normalised[key] = norm[i]
        i += 1

    return normalised


def getCumulativeDistr(distr):
    """Returns an OrderedDictionary where the values add up the cumulative sum

    Args:
        distr (dict): A probability distribution

    Returns:
        norm (dict): a new dictionary where the values add up the cumulative sum
    """

    # first, make sure we have a normalised distribution
    distr = normaliseDict(distr)

    # create an OrderedDict
    cumulative = OrderedDict()

    # iterate through the distribution, adding up the probabilities as we go
    sum = 0
    for key in distr:
        sum += distr[key]
        cumulative[key] = sum

    # make sure the final key is a dead cert
    distr[key] = 1

    return cumulative


def sample(distr):
    """Picks a random value from a probability distribution

    Args:
        distr (dict): A probability distribution

    Returns:
        key (str): the chosen dict key
    """

    # make sure the distribution is a normalised cumulative distr
    distr = getCumulativeDistr(distr)

    # pick a random number between 0 and 1
    r = random.random()

    # iterate through the distribution
    for key in distr:
        # return the key that matches the random choice
        if r < distr[key]:
            return key

    # return the last key if all else fails
    return key


if __name__ == "__main__":

    print("=== Fair dice ===")

    fairDice = {
        "1": 1,
        "2": 1,
        "3": 1,
        "4": 1,
        "5": 1,
        "6": 1
    }

    results = {}
    for x in range(10):
        result = sample(fairDice)
        i = results.get(result, 0)
        results[result] = i + 1
    print("Throw results: {}".format(results))

    print("=== Loaded dice ===")

    loadedDice = {
        "1": 10,
        "2": 1,
        "3": 1,
        "4": 1,
        "5": 1,
        "6": 1
    }

    results = {}
    for x in range(10):
        result = sample(loadedDice)
        i = results.get(result, 0)
        results[result] = i + 1
    print("Throw results: {}".format(results))
