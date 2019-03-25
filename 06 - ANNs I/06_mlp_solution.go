package main

import (
	"fmt"

	"06_mlp_solution/mlp" //mlp package to abstract away the calculations

	"gonum.org/v1/gonum/mat" //gonum library used for matrix calculations
)

func main() {

	// creating an mlp by defining the number of inputs, outputs
	// and a list of ints for the hidden layers
	m := &mlp.Mlp{
		NumInputs:    2,
		HiddenLayers: []int{2, 3, 4},
		NumOutputs:   5,
	}

	// initializing the mlp by setting the random weights
	m.Init()

	// defining the input matrix based on the size provided earlier
	input := mat.NewDense(1, m.NumInputs, []float64{1.0, 2.0})

	// activate the network
	output := m.Activate(input)

	fmt.Printf("Network Activation: %v\n", mat.Formatted(output, mat.Prefix("")))
}
