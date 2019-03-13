import re
from probability import sample

def createTransitionMatrix(text):
    """Creates a transition matrix from some given text

    Args:
        text (str): The text

    Returns:
        matrix (dict): the transition matrix
    """
    # create the matrix dictionary
    matrix = {}

    # use a regex to split on whitespace
    splitText = re.split("[^a-zA-Z']+", text)

    # iterate through the words
    for i in range(len(splitText)):
        # we need to start from the second word
        if i > 0:
            # get the current word and the last word from the list
            word = splitText[i]
            lastWord = splitText[i-1]

            # get the distrubution and the count
            distr = matrix.get(lastWord, {})
            count = distr.get(word, 0)

            # add one to the count
            distr[word] = count + 1

            # make sure the distribution is in the matrix
            matrix[lastWord] = distr

    return matrix


if __name__ == "__main__":

    # 1) Can you write a Markov chain to describe the ‘red flower red car red car red flower’ sequence?

    # the initial distribution - to decide what happens first
    initialDistribution = {
        # for now, let's always start with "Humpty"
        "red": 1,
    }

    # transition matrix - to decide what happens next
    transitionMatrix = {
        # for now, let's always start with "Humpty"
        "red": {
            "car": 0.5,
            "flower": 0.5
        },
        "car": {
            "red": 1
        },
        "flower": {
            "red": 1
        }
    }

    # first, we decide the initial state
    sequence = [sample(initialDistribution)]

    # then, we'll decide the next 7 states...
    for x in range(7):
        # find the probabilities for the next state
        state = sequence[-1]
        nextDistr = transitionMatrix[state]

        # then decide the outcome
        sequence.append(sample(nextDistr))

    print(" ".join(sequence))

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

    # 2) Can you write a function that automatically creates a transition matrix
    #       from the words of the popular nursery rhyme Humpty dumpty?

    # the transition matrix - to decide what happens next
    transitionMatrix = createTransitionMatrix(text)


    # 3) Can you use this transition matrix along with an initial distribution to create a
    #       new remix of Humpty Dumpty?

    # first, we decide the initial state
    sequence = [sample(initialDistribution)]

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
        sequence.append(sample(nextDistr))

    print("Output sentence:")
    print(" ".join(sequence))

