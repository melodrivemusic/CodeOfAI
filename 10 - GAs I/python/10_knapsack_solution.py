from random import randrange, random


class Item:
    """
    The Item class represents one item in our knapsack
    """
    value = 0
    weight = 0

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return "Item(value={}, weight={})".format(self.value, self.weight)


def getRandomItem(min=1, max=30):
    """
    Returns an Item with random weight and value
    :param min: The minimum weight/value
    :param max: The maximum weight/value
    :return: Item
    """
    return Item(
        randrange(min, max),
        randrange(min, max)
    )


def getPhenotype(chromosome, items):
    """
    Given a chromosome, returns a list of items in the bag
    :param chromosome:
    :param items:
    :return: list
    """
    return [v for i, v in enumerate(items) if chromosome[i] == 1]


def fitness(chromosome, items, capacity):
    """
    Calculates a fitness score for a single chromosome
    :param chromosome:
    :param items:
    :param capacity:
    :return: float
    """
    phenotype = getPhenotype(chromosome, items)

    # sum up the weight
    weight = sum([i.weight for i in phenotype])

    if weight > capacity:
        # the knapsack is over capacity, return 0 fitness
        return 0

    # return a fitness based on the value of the items in the knapsack
    value = sum([i.value for i in phenotype])
    return value


if __name__ == "__main__":
    # the number of possible items to put in the knapsack
    numItems = 25

    # the items themselves
    # this will generate a random set of items, from 1-30 in value and weight
    items = [getRandomItem() for x in range(numItems)]

    # the target capacity
    capacity = 10 * numItems

    print("Number of items:", numItems)
    print("Capacity: ", capacity)

    # A potential solution to the knapsack problem as a binary chromosome
    # A list for every potential item, 1 = it's in the bag 0 = it isn't
    # Here I'll just create a random one
    chromosome = [1 if random() > 0.5 else 0 for x in range(numItems)]
    print("Chromosome:")
    print(chromosome)

    # 1) Can you take some code from the bruteForceKnapsack function,
    #         and create a fitness function to evaluate a single chromosome?
    score = fitness(chromosome, items, capacity)
    print("Fitness: ", score)
