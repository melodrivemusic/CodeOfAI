import re
import csv
from probability import choose

def updateInitialDistribution(initialDistr, splitText):
    """Updates an initial distribution with some pre-tokenised text

    Args:
        initialDistr (dict): The initial distribution
        splitText (list): The tokenised words
    """
    # get the first word
    word = splitText[0]

    # get the count
    count = initialDistr.get(word, 0)

    # add one to the count
    initialDistr[word] = count + 1


def updateTransitionMatrix(matrix, splitText):
    """Updates a transition matrix with some pre-tokenised text

    Args:
        matrix (dict): The transition matrix
        splitText (list): The tokenised words
    """
    # iterate through the words
    for i in range(len(splitText)):
        # we need to start from the second word
        if i > 0:
            # get the current word and the last word from the list
            word = splitText[i]
            lastWord = splitText[i - 1]

            # get the distrubution and the count
            distr = matrix.get(lastWord, {})
            count = distr.get(word, 0)

            # add one to the count
            distr[word] = count + 1

            # make sure the distribution is in the matrix
            matrix[lastWord] = distr


def createMarkovChain(dataPath, artist):
    """Creates a 1st-order Markov model (an initial distribution and a transition matrix)
        from the Song Lyric dataset

    Args:
        dataPath (str): Path to the dataset
        artist (str): The artist to create a model of
    """
    # create the dictionaries for the initial distribution and transition matrix
    initialDistr = {}
    transitionMatrix = {}

    # read the data, it's in csv format
    with open(dataPath) as csvfile:
        # use the csv module to read the file
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            # the first column is the artist name
            if row[0] == artist:
                # the fourth column contains the lyrics
                text = row[3].strip()

                # use a regex to split on whitespace
                splitText = re.split("[^a-zA-Z']+", text)

                # update the initial distribution
                updateInitialDistribution(initialDistr, splitText)

                # update the transition matrix
                updateTransitionMatrix(transitionMatrix, splitText)

    # once we've read the data, return the model
    return initialDistr, transitionMatrix


if __name__ == "__main__":

    # I'm using mousehead's Song Lyrics dataset, you can get it from here:
    # https://www.kaggle.com/mousehead/songlyrics/home

    # change this so it points to where you downloaded your dataset...
    dataPath = "D:\\Data\\songdata.csv"

    # select the Artist you want...
    artist = "ABBA"
    print("Generating a new {} song!".format(artist))

    # create the initial distribution and the transition matrix from the data
    initialDistr, transitionMatrix = createMarkovChain(dataPath, artist)

    # first, we decide the initial state
    sequence = [choose(initialDistr)]

    # then, we'll create the rest of the song, up to 500 words...
    for x in range(500):
        # find the probabilities for the next state
        state = sequence[-1]

        # if the word isn't in the transitionMatrix we can't continue
        if state not in transitionMatrix:
            break

        # grab the next distribution
        nextDistr = transitionMatrix[state]

        # then decide the outcome
        sequence.append(choose(nextDistr))

    print("Result:")
    print(" ".join(sequence))

