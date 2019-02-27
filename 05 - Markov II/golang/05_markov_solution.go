package main

import (
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"os"
	"regexp"
	"strings"
)

// Updates an initial distribution with some pre-tokenised text
func updateInitialDistribution(initialDistr map[string]float64, splitText []string) {
	// get the first word
	word := splitText[0]

	// get the count
	count, exists := initialDistr[word]
	if !exists {
		count = 0.0
	}

	// add one to the count
	initialDistr[word] = count + 1.0
}

// Updates a transition matrix with some pre-tokenised text
func updateTransitionMatrix(matrix map[string]map[string]float64, splitText []string) {

	// terate through the words
	for i, word := range splitText {

		// we need to start from the second word
		if i > 0 {

			// get the current word and the last word from the list
			lastWord := splitText[i-1]

			// get the distrubution and the count
			distr, exists := matrix[lastWord]
			if !exists {
				distr = make(map[string]float64)
			}
			count, wordExists := distr[word]
			if !wordExists {
				count = 0
			}

			// add one to the count
			distr[word] = count + 1

			// make sure the distribution is in the matrix
			matrix[lastWord] = distr
		}
	}
}

// Creates a 1st-order Markov model (an initial distribution and a transition matrix)
// from the Song Lyric dataset
func createMarkovChain(file io.Reader, artist string) (map[string]float64, map[string]map[string]float64) {

	// create the dictionaries for the initial distribution and transition matrix
	initialDistr := make(map[string]float64)
	transitionMatrix := make(map[string]map[string]float64)

	re := regexp.MustCompile("[^a-zA-Z']+")

	// read the data, it's in csv format
	r := csv.NewReader(file)

	// read the rows in a loop till end of file
	for {
		record, err := r.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatal(err)
		}

		// the first column is the artist name
		if record[0] == artist {

			// the fourth column contains the lyrics
			text := strings.Trim(record[3], " ")

			// use a regex to split on whitespace
			splitText := re.Split(text, -1)

			// update the initial distribution
			updateInitialDistribution(initialDistr, splitText)

			// update the transition matrix
			updateTransitionMatrix(transitionMatrix, splitText)
		}
	}

	// once we've read the data, return the model
	return initialDistr, transitionMatrix
}

func main() {

	// I'm using mousehead's Song Lyrics dataset, you can get it from here:
	// https://www.kaggle.com/mousehead/songlyrics/home

	// change this so it points to where you downloaded your dataset...
	dataPath := "./songdata.csv"

	f, err := os.Open(dataPath)
	if err != nil {
		log.Fatalf("error opening file: %v", err)
	}

	// select the Artist you want...
	artist := "ABBA"

	fmt.Printf("Generating a new %s song!\n", artist)

	// create the initial distribution and the transition matrix from the data
	initialDistr, transitionMatrix := createMarkovChain(f, artist)

	// first, we decide the initial state
	sequence := []string{choose(initialDistr)}

	// then, we'll create the rest of the song, up to 500 words...
	for i := 0; i < 500; i++ {

		// find the probabilities for the next state
		state := sequence[len(sequence)-1]

		// grab the next distribution
		nextDistr, exists := transitionMatrix[state]

		// if the word isn't in the transitionMatrix we can't continue
		if !exists {
			break
		}

		// then decide the outcome
		sequence = append(sequence, choose(nextDistr))
	}

	fmt.Printf("Result: %v\n", sequence)
}
