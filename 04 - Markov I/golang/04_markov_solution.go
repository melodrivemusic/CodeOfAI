package main

import (
	"fmt"
	"regexp"
)

// createTransitionMatrix creates a transition matrix from some given text
func createTransitionMatrix(text string) map[string]map[string]float64 {

	// create the matrix map
	matrix := make(map[string]map[string]float64, 0)

	// use a regex to split on whitespace
	words := regexp.MustCompile("[^a-zA-Z']+").Split(text, -1)

	// iterate through the words
	for i, word := range words {

		// we need to start from the second word
		if i > 0 {

			// get the current word and the last word from the list
			lastWord := words[i-1]

			// get the distrubution
			distr, exists := matrix[lastWord]
			if !exists {
				distr = make(map[string]float64, 0)
			}

			// get the count
			count, countExists := distr[word]
			if !countExists {
				count = 0
			}

			// add one to the count
			distr[word] = count + 1

			// make sure the distribution is in the matrix
			matrix[lastWord] = distr
		}
	}

	return matrix
}

func main() {

	// the text of our nursery rhyme
	text := `Humpty Dumpty sat on a wall
    Humpty Dumpty had a great fall
    All the king's horses and all the king's men
	couldn't put Humpty together again`

	// the initial distribution - to decide what happens first
	initialDistribution := map[string]float64{
		"Humpty": 1.0,
	}

	// the transition matrix - to decide what happens next
	transitionMatrix := createTransitionMatrix(text)

	// first, we decide the initial state
	sequence := []string{sample(initialDistribution)}

	// then, we'll decide the next text, up to 100 words...
	for i := 0; i < 100; i++ {

		// find the probabilities for the next state
		state := sequence[len(sequence)-1]

		// if the word isn't in the transitionMatrix we can't continue (e.g. "again")
		_, exits := transitionMatrix[state]
		if !exits {
			break
		}

		// grab the next distribution
		nextDistr := transitionMatrix[state]

		// then decide the outcome
		normalizeMap(nextDistr)
		sequence = append(sequence, sample(nextDistr))
	}

	fmt.Printf("Output sentence: %v\n", sequence)
}
