import random


class Item:
    value = 0
    weight = 0

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return "Item(value={}, weight={})".format(self.value, self.weight)

    @classmethod
    def random(cls, min=1, max=30):
        return Item(
            random.randrange(min, max),
            random.randrange(min, max)
        )


def getPhenotype(chromosome, items):
    return [v for i, v in enumerate(items) if chromosome[i] == 1]


def fitness(chromosome, items, capacity):
    phenotype = getPhenotype(chromosome, items)
    weight = sum([i.weight for i in phenotype])
    if weight > capacity:
        return 0
    value = sum([i.value for i in phenotype])
    return value


if __name__ == "__main__":
    # the number of possible items to put in the knapsack
    numItems = 25

    # the items themselves
    # this will generate a random set of items, from 1-30 in value and weight
    items = [Item.random() for x in range(numItems)]

    # the target capacity
    capacity = 10 * numItems

    print("Number of items:", numItems)
    print("Capacity: ", capacity)

    # 1) Can you define a potential solution to the knapsack problem as a binary chromosome?
    # My solution is to have a list for every potential item, 1 = it's in the bag 0 = it isn't
    # Here I'll just create a random one
    chromosome = [1 if random.random() > 0.5 else 0 for x in range(numItems)]

    # 2) Can you take some code from the bruteForceKnapsack function, and create a fitness function to
    score = fitness(chromosome, items, capacity)

    print("Chromosome: ", chromosome)
    print("Fitness: ", score)
