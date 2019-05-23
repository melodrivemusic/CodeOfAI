from random import random, randrange, shuffle
from itertools import tee

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


def getRandomChromosome(numItems):
    return [1 if random() > 0.5 else 0
            for x in range(numItems)]


def getRandomPopulation(popSize, numItems):
    return [getRandomChromosome(numItems)
            for x in range(popSize)]


def getPhenotype(chromosome, items):
    return [v for i, v in enumerate(items) if chromosome[i] == 1]


def fitness(chromosome, items, capacity):
    phenotype = getPhenotype(chromosome, items)
    weight = sum([i.weight for i in phenotype])
    if weight > capacity:
        return 0
    value = sum([i.value for i in phenotype])
    return value


def getFitness(population, items, capacity):
    fitnessScores = []
    for chromosome in population:
        score = fitness(chromosome, items, capacity)
        fitnessScores.append((chromosome, score))
    fitnessScores = sorted(fitnessScores, key=lambda x: x[1], reverse=True)
    return fitnessScores


def select(fitnessScores, selectionRatio=0.5):
    numToSelect = int(len(fitnessScores)*selectionRatio)
    selected = fitnessScores[:numToSelect]
    rejected = fitnessScores[numToSelect:]
    return [x[0] for x in selected], [x[0] for x in rejected]


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def crossover(parents):
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


if __name__ == "__main__":
    # Start as we did last time by creating our items and target capacity
    numItems = 25
    items = [getRandomItem() for x in range(numItems)]
    capacity = 10 * numItems

    # Initialise a population and calculate an initial fitness
    popSize = 50
    population = getRandomPopulation(popSize, numItems)
    fitnessScores = getFitness(population, items, capacity)
    print("Initial fitness:", fitnessScores[0][1])

    numGenerations = 10
    for generation in range(numGenerations):
        # 1) Selection
        selected, rejected = select(fitnessScores)

        # 2) Crossover
        children = crossover(selected)

        # 3) Form new population
        population = selected + children

        # 3.5) population maintenance
        while len(population) < popSize:
            i = randrange(len(rejected))
            population.append(rejected.pop(i))

        # 4) Calculate fitness for our new population
        fitnessScores = getFitness(population, items, capacity)
        print("Generation {} fitness: {}".format(generation, fitnessScores[0][1]))

    bestChromosome = fitnessScores[0][0]
    bestCombination = getPhenotype(bestChromosome, items)
    bestValue = sum([i.value for i in bestCombination])
    bestWeight = sum([i.weight for i in bestCombination])
    print("Found best combination")
    print("{} items with {} value and {} weight:".format(len(bestCombination), bestValue, bestWeight))
    print(bestCombination)
