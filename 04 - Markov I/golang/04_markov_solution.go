package main

import (
	"fmt"
	"regexp"
)

func createTransitionMatrix(text string) map[string]map[string]int {

	matrix := make(map[string]map[string]int, 0)

	ss := regexp.MustCompile("[^a-zA-Z']+").Split(text, -1)

	for i, word := range ss {

		if i > 0 {

			lastWord := ss[i-1]

			distr, exists := matrix[lastWord]
			if !exists {
				distr = make(map[string]int, 0)
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

	// initialDistribution := map[string]int{
	// 	"Humpty": 1,
	// }

	transitionMatrix := createTransitionMatrix(text)

	fmt.Println(transitionMatrix["Dumpty"])
}
