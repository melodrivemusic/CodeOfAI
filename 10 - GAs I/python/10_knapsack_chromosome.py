import random


class Item:
    value = 0
    weight = 0

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return "Item(value={}, weight={})".format(self.value, self.weight)


def getRandomItem(min=1, max=30):
    return Item(
        random.randrange(min, max),
        random.randrange(min, max)
    )


def getPhenotype(chromosome, items):
    return [v for i, v in enumerate(items) if chromosome[i] == 1]


if __name__ == "__main__":
    # the number of possible items to put in the knapsack
    numItems = 10

    # the items themselves
    # this will generate a random set of items, from 1-30 in value and weight
    items = [getRandomItem() for x in range(numItems)]

    # A potential solution to the knapsack problem as a binary chromosome
    # A list for every potential item, 1 = it's in the bag 0 = it isn't
    # Here I'll just create a random one
    chromosome = [1 if random.random() > 0.5 else 0 for x in range(numItems)]
    print("Chromosome:")
    print(chromosome)

    phenotype = getPhenotype(chromosome, items)
    print("Phenotype ({} items):".format(len(phenotype)))
    print(phenotype)
