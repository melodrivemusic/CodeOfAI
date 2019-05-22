import random
from itertools import combinations
from time import time


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


def getCombinations(items, capacity):
    # get all combinations
    combi = []
    for i in range(1, len(items)):
        c = list(combinations(items, i))
        if len(c[0]) > capacity:
            # early stop - we don't need *all* the combinations
            break
        combi += c
    return combi


def bruteForceKnapsack(items, capacity):
    # find all combinations
    allCombinations = getCombinations(items, capacity)
    numCombinations = len(allCombinations)
    print(numCombinations, "combinations")

    bestCombination = None
    bestWeight = 0
    bestValue = 0
    for i in range(numCombinations):
        thisCombination = allCombinations[i]
        weight = sum([i.weight for i in thisCombination])
        if weight <= capacity:
            value = sum([i.value for i in thisCombination])
            if value > bestValue:
                bestValue = value
                bestWeight = weight
                bestCombination = thisCombination

    return bestCombination, bestValue, bestWeight


if __name__ == "__main__":
    # record the entry point time
    t1 = time()

    # the number of possible items to put in the knapsack
    numItems = 10

    # the items themselves
    # this will generate a random set of items, from 1-30 in value and weight
    items = [Item.random() for x in range(numItems)]

    # the target capacity
    capacity = 10 * numItems

    print("Number of items:", numItems)
    print("Capacity: ", capacity)

    bestCombination, bestValue, bestWeight = bruteForceKnapsack(items, capacity)

    print("Found best combination")
    print("{} items with {} value and {} weight:".format(len(bestCombination), bestValue, bestWeight))
    print(bestCombination)

    print("Took ", time() - t1)
