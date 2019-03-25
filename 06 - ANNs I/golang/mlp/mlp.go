package mlp

import (
	"math"
	"math/rand"

	"gonum.org/v1/gonum/mat" //gonum library used for matrix calculations
)

// Mlp has information regarding the neural network
// All except weights are provided by the user hence it is unexported
type Mlp struct {
	NumInputs    int
	HiddenLayers []int
	NumOutputs   int
	weights      []mat.Matrix
}

// Init function initializes the weights for the entire network
func (m *Mlp) Init() {

	// create a generic representation of the layers
	layers := make([]int, 0)
	layers = append(layers, m.NumInputs)
	layers = append(layers, m.HiddenLayers...)
	layers = append(layers, m.NumOutputs)

	// create random connections for the layers
	for i := 0; i < len(layers)-1; i++ {
		m.weights = append(m.weights, generateRandom(layers[i], layers[i+1]))
	}
}

// Activate computes the activation of the network based on the input signals
func (m *Mlp) Activate(inputs mat.Matrix) mat.Matrix {
	activation := inputs.(*mat.Dense)

	// iterate over the network layers
	for i := 0; i < len(m.weights); i++ {

		// calculate dot product between previous activation and weights
		dotProduct := new(mat.Dense)
		dotProduct.Product(activation, m.weights[i])

		// apply sigmoid function
		activation = new(mat.Dense)
		activation.Apply(sigmoid, dotProduct)
	}

	// return the output layer activation
	return activation
}

// sigmoid function helps calculate sigmoid of an element
// in a matrix
func sigmoid(r, c int, z float64) float64 {
	return 1.0 / (1 + math.Exp(-1*z))
}

// generateRandom is helper function to generate a
// matrix filled with random numbers
func generateRandom(n, m int) mat.Matrix {
	data := make([]float64, n*m)
	for i := range data {
		data[i] = rand.NormFloat64()
	}
	return mat.NewDense(n, m, data)
}
