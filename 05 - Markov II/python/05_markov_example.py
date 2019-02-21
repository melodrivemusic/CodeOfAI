import re
from probability import choose


def createTransitionMatrix(text):
    """Creates a transition matrix from some given text

    Args:
        text (str): The text

    Returns:
        matrix (dict): the transition matrix
    """

    # use a regex to split on whitespace
    splitText = re.split("[^a-zA-Z']+", text)

    # create the matrix dictionary
    matrix = {}

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

    return matrix


if __name__ == "__main__":

    # the text of our nursery rhyme

    text = """Humpty Dumpty sat on a wall
    Humpty Dumpty had a great fall
    All the king's horses and all the king's men
    couldn't put Humpty together again"""

    # the initial distribution - to decide what happens first
    initialDistribution = {
        # for now, let's always start with "Humpty"
        "Humpty": 1,
    }

    # the transition matrix - to decide what happens next
    transitionMatrix = createTransitionMatrix(text)

    # first, we decide the initial state
    sequence = [choose(initialDistribution)]

    # then, we'll decide the next text, up to 100 words...
    for x in range(100):
        # find the probabilities for the next state
        state = sequence[-1]

        # if the word isn't in the transitionMatrix we can't continue (e.g. "again")
        if state not in transitionMatrix:
            break

        # grab the next distribution
        nextDistr = transitionMatrix[state]

        # then decide the outcome
        sequence.append(choose(nextDistr))

    print("Output sentence:")
    print(" ".join(sequence))

