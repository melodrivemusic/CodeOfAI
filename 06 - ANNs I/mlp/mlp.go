package mlp

import (
	"math"
	"math/rand"

	"gonum.org/v1/gonum/mat"
)

type Mlp struct {
	NumInputs    int
	HiddenLayers []int
	NumOutputs   int
	weights      []mat.Matrix
}

func apply(fn func(i, j int, v float64) float64, m mat.Matrix) mat.Matrix {
	r, c := m.Dims()
	o := mat.NewDense(r, c, nil)
	o.Apply(fn, m)
	return o
}

func sigmoid(r, c int, z float64) float64 {
	return 1.0 / (1 + math.Exp(-1*z))
}

func generateRandom(n, m int) mat.Matrix {
	data := make([]float64, n*m)
	for i := range data {
		data[i] = rand.NormFloat64()
	}
	return mat.NewDense(n, m, data)
}

func (m *Mlp) Init() {
	layers := make([]int, 0)

	layers = append(layers, m.NumInputs)
	layers = append(layers, m.HiddenLayers...)
	layers = append(layers, m.NumOutputs)

	for i := 0; i < len(layers)-1; i++ {
		m.weights = append(m.weights, generateRandom(layers[i], layers[i+1]))
	}
}

func (m *Mlp) Activate(inputs mat.Matrix) mat.Matrix {
	activation := inputs

	for i := 0; i < len(m.weights); i++ {
		r, _ := activation.Dims()
		_, c := m.weights[i].Dims()
		dotProduct := mat.NewDense(r, c, nil)
		dotProduct.Product(activation, m.weights[i])
		activation = apply(sigmoid, dotProduct).(*mat.Dense)
	}

	return activation
}
