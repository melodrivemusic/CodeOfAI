from itertools import combinations


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
