package main

import (
	"fmt"

	"06_mlp_solution/mlp"

	"gonum.org/v1/gonum/mat"
)

func matPrint(X mat.Matrix) {
	fa := mat.Formatted(X, mat.Prefix(""), mat.Squeeze())
	fmt.Printf("%v\n", fa)
}

func main() {
	m := &mlp.Mlp{
		NumInputs:    1,
		HiddenLayers: []int{2, 3, 4},
		NumOutputs:   5,
	}

	m.Init()

	inputs := mat.NewDense(1, len([]float64{1.0}), []float64{1.0})

	fmt.Println("Network Activation")
	matPrint(m.Activate(inputs))
}
