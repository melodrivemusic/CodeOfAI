package main

import (
	"fmt"
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

// choose function takes in a probability distribution
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

// simulateThrows simulates a coin throw for given number of times,
// map in the input represents the probability distribution of the sides
func simulateThrows(coin map[string]float64, times int) map[string]int {

	// map to store the results of each toss
	results := make(map[string]int, times)

	for i := 0; i < times; i++ {

		// chooose function to select a side
		result := choose(coin)

		// check if the result has been obtained before
		i, exists := results[result]

		// if result obtained for the first time, initialize with zero
		if !exists {
			results[result] = 0
		}

		// increment the side by one for each face up on completion of throw
		results[result] = i + 1
	}

	return results
}

func main() {

	fmt.Println("===== Fair Dice =====")

	// unbiased dice
	coin := map[string]float64{
		"1": 1,
		"2": 1,
		"3": 1,
		"4": 1,
		"5": 1,
		"6": 1,
	}

	// create probability distribution
	normalizeMap(coin)

	// simulate throws
	results := simulateThrows(coin, 1000)

	// print the result
	fmt.Printf("Throw results: %v\n", results)

	fmt.Println("===== Loaded Dice =====")

	// biased dice
	weightedCoin := map[string]float64{
		"1": 10,
		"2": 1,
		"3": 1,
		"4": 1,
		"5": 1,
		"6": 1,
	}

	// create probability distribution
	normalizeMap(weightedCoin)

	// simulate throws
	results = simulateThrows(weightedCoin, 1000)

	// print the result
	fmt.Printf("Throw results: %v\n", results)
}
