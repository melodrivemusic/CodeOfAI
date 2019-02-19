package main

import (
	"fmt"
	"regexp"
)

func createTransitionMatrix(text string) map[string]map[string]float64 {

	matrix := make(map[string]map[string]float64, 0)

	ss := regexp.MustCompile("[^a-zA-Z']+").Split(text, -1)

	for i, word := range ss {

		if i > 0 {

			lastWord := ss[i-1]

			distr, exists := matrix[lastWord]
			if !exists {
				distr = make(map[string]float64, 0)
			}

			count, countExists := distr[word]
			if !countExists {
				count = 0
			}

			distr[word] = count + 1

			matrix[lastWord] = distr
		}
	}

	return matrix
}

func main() {

	text := `Humpty Dumpty sat on a wall
    Humpty Dumpty had a great fall
    All the king's horses and all the king's men
	couldn't put Humpty together again`

	initialDistribution := map[string]float64{
		"Humpty": 1.0,
	}

	transitionMatrix := createTransitionMatrix(text)

	sequence := []string{choose(initialDistribution)}

	for i := 0; i < 100; i++ {
		state := sequence[len(sequence)-1]

		_, exits := transitionMatrix[state]
		if !exits {
			break
		}

		nextDistr := transitionMatrix[state]

		normalizeMap(nextDistr)
		sequence = append(sequence, choose(nextDistr))
	}

	fmt.Printf("Output sentence: %v\n", sequence)
}
