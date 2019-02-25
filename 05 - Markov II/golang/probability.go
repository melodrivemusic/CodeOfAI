package main

import (
	"math/rand"
)

// normalizeMap takes in map of floats and normalized it
// so tha that they sum up to one
func normalizeMap(m map[string]float64) {

	// accumulator variable
	var sum float64

	// calculate the sum of the given floats
	for _, v := range m {
		sum += v
	}

	// divide total on each float to create a sort of
	// probability distribution
	for k, v := range m {
		m[k] = v / sum
	}
}

// Sample function takes in a probability distribution
// and returns one based on a uniformly selected random number
func choose(m map[string]float64) string {

	// uniform random number between o.o and 1.0
	r := rand.Float64()

	// key to store the value to return
	var key string

	// iterate over the map
	for k, v := range m {

		// check r and update its value, when greater than 0
		if r >= 0.0 {
			r -= v

			// update key with the current value of k
			key = k

		} else {

			// break out of the loop when r goes below 0
			break
		}
	}

	// return the value that helped cross the r threshold
	return key
}
