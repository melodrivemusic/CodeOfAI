from random import random, randrange, shuffle
from itertools import tee
from time import time
from search.bruteforce import bruteForceKnapsack


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


def getRandomChromosome(numItems):
    """
    Creates a single random chromosome
    :param numItems: The number of genes in the chromosome
    :return: list
    """
    return [1 if random() > 0.5 else 0
            for x in range(numItems)]


def getRandomPopulation(popSize, numItems):
    """
    Creates a population of random chromosomes
    :param popSize: Population size
    :param numItems: Chromosome size
    :return: list
    """
    return [getRandomChromosome(numItems)
            for x in range(popSize)]


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
    weight = sum([i.weight for i in phenotype])
    if weight > capacity:
        return 0
    value = sum([i.value for i in phenotype])
    return value


def getFitness(population, items, capacity):
    """
    Calculates fitness scores for a population of chromosomes
    :param population:
    :param items:
    :param capacity:
    :return: sorted list of fitnesses [ (chromosome, score), ... ]
    """
    fitnessScores = []
    for chromosome in population:
        score = fitness(chromosome, items, capacity)
        fitnessScores.append((chromosome, score))
    return sorted(fitnessScores, key=lambda x: x[1], reverse=True)


def select(population, *fitnessArgs, selectionRatio=0.5):
    """
    Selects the fittest members of the poplation based on a fitness function and ratio
    :param population:
    :param fitnessArgs: The arguments passed to the fitness function
    :param selectionRatio: how many items to select/reject
    :return: tuple (selected, rejected)
    """
    numToSelect = int(len(population) * selectionRatio)
    # calculate fitness for the population
    fitnessScores = getFitness(population, *fitnessArgs)
    selected = fitnessScores[:numToSelect]
    rejected = fitnessScores[numToSelect:]
    return selected, rejected


def pairwise(iterable):
    """
    Iterates over a list, two items at a time
    :param iterable:
    :return: iterable
    """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def crossover(parents):
    """
    Creates a random crossover of a population
    :param parents:
    :return: list the created children
    """
    children = []
    shuffle(parents)
    chromosomeLength = len(parents[0])
    halfLength = int(chromosomeLength*0.5)

    for a, b in pairwise(parents):
        child = [0] * chromosomeLength

        # Evenly sample indexes from both parents
        indexes = [x for x in range(chromosomeLength)]
        shuffle(indexes)
        takeA = indexes[:halfLength]

        for i in range(chromosomeLength):
            if i in takeA:
                gene = a[i]
            else:
                gene = b[i]
            child[i] = gene

        children.append(child)

    return children


def gaKnapsack(items, capacity, popSize=20, numGenerations=20):
    # Initialise a population and calculate an initial fitness
    population = getRandomPopulation(popSize, numItems)

    for generation in range(numGenerations):
        # 1) Selection
        selected, rejected = select(population, items, capacity)
        print("Generation {} best fitness: {}".format(generation, selected[0][1]))

        # 2) Crossover
        # keep just the chromosomes
        selected = [x[0] for x in selected]
        children = crossover(selected)

        # 4) Form new population
        population = selected + children

        # 4.5) population maintenance
        while len(population) < popSize:
            i = randrange(len(rejected))
            runt = rejected.pop(i)
            population.append(runt[0])

    fitnessScores = getFitness(population, items, capacity)
    bestChromosome = fitnessScores[0][0]
    bestCombination = getPhenotype(bestChromosome, items)
    bestValue = sum([i.value for i in bestCombination])
    bestWeight = sum([i.weight for i in bestCombination])
    return bestCombination, bestValue, bestWeight


if __name__ == "__main__":
    numItemsToTest = [15, 20, 25]
    results = {}

    for numItems in numItemsToTest:
        results[numItems] = {}

        items = [getRandomItem() for x in range(numItems)]
        capacity = 10 * numItems

        print("========== GA ==========")
        t1 = time()

        result = gaKnapsack(items, capacity)
        results[numItems]["GA"] = {
            "result": result,
            "time": time() - t1
        }

        print("====== Brute Force ======")
        t1 = time()

        result = bruteForceKnapsack(items, capacity)
        results[numItems]["Brute Force"] = {
            "result": result,
            "time": time() - t1
        }

    methods = ["GA", "Brute Force"]
    print("{:8} | {:12} | {:10} | {:8}".format("numItems", "method", "bestValue", "time"))
    print("=" * 47)
    for numItems in numItemsToTest:
        for m in methods:
            bestCombination, bestValue, bestWeight = results[numItems][m]["result"]
            time = results[numItems][m]["time"]
            print("{:8} | {:12} | {:10} | {: 8.3f}".format(numItems, m, bestValue, time))
