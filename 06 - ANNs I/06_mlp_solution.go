package main

import (
	"fmt"

	"06_mlp_solution/mlp"

	"gonum.org/v1/gonum/mat"
)

func main() {
	m := &mlp.Mlp{
		NumInputs:    2,
		HiddenLayers: []int{2, 3, 4},
		NumOutputs:   5,
	}

	m.Init()

	input := mat.NewDense(1, m.NumInputs, []float64{1.0, 2.0})

	output := m.Activate(input)

	fmt.Printf("Network Activation: %v\n", mat.Formatted(output, mat.Prefix("")))
}
