/*
Q1) Can you change the implementation to return all possible paths to the goal (rather than the shortest)?
*/
package main

import (
	"fmt"

	"github.com/golang-collections/collections/queue" // queue implementation has O(1) complexity for poping the first element,
	// Go standard library has no queue data structure implementation
)

// stringInSlice is used to check if a string is present in a slice
// Go does not have python styled 'in' to check for existence
func stringInSlice(a string, list []string) bool {
	for _, b := range list {
		if b == a {
			return true
		}
	}
	return false
}

// bfsShortestPath finds all paths between 2 nodes in a graph using BFS
func bfsAllPaths(graph map[string][]string, start, goal string) [][]string {

	// set up a path list
	path := []string{start}

	// return a simple path if start is the goal
	if start == goal {
		return [][]string{path}
	}

	// slice of slice to store all paths between start and goal
	solutions := [][]string{}

	// list to keep track of all visited nodes
	explored := []string{}

	// the FIFO queue
	queue := queue.New()

	// add the first path to the queue
	queue.Enqueue(path)

	// keep looping until there are no nodes still to be checked
	for queue.Len() > 0 {

		// pop first item from queue (FIFO)
		path := queue.Dequeue().([]string)

		// retrieve the node from the path list
		node := path[len(path)-1]

		// check if the node has already been explored
		if !stringInSlice(node, explored) {

			// add node to list of checked nodes
			explored = append(explored, node)

			// get neighbours
			neighbours, exits := graph[node]

			// if no neighbours ignore
			if exits {

				// go through all neighbour nodes
				for _, neighbour := range neighbours {

					// make a copy of the current path
					path1 := make([]string, len(path))
					copy(path1, path)

					// add this neighbour to the path
					path1 = append(path1, neighbour)

					// append path to solutions if neighbour is goal
					// otherwise add path for further exploration
					if neighbour == goal {
						solutions = append(solutions, path1)
					} else {
						queue.Enqueue(path1)
					}
				}
			}
		}
	}

	// Finally return solutions that has all paths
	return solutions
}

// weightedNode represents a node's name and its weight
// Go doesn't have a tuple construct like in python
type weightedNode struct {
	name   string
	weight int
}

// nodeInSlice is used to check if a node is present in a slice
// You might also notice a similar function for bfsAllPath func
// we can avoid this by using reflect, but people prefer repeation
// over making the code hard to read, also not using reflect means
// a slight performance improvement
func nodeInSlice(a weightedNode, list []weightedNode) bool {
	for _, b := range list {
		if b.name == a.name {
			return true
		}
	}
	return false
}

// Finds the best path (lowest weight) between 2 nodes in a graph using BFS
func bfsBestPath(graph map[string][]weightedNode, start, goal string) []weightedNode {

	// set up a path list
	path := []weightedNode{{start, 0}}

	// return a simple path if start is the goal
	if start == goal {
		return path
	}

	// keep track of all solutions
	solutions := [][]weightedNode{}

	// list to keep track of all visited nodes
	explored := []weightedNode{}

	// the FIFO queue
	queue := queue.New()

	// add the first path to the queue
	queue.Enqueue(path)

	// keep looping until there are no nodes still to be checked
	for queue.Len() > 0 {

		// pop first item from queue (FIFO)
		path := queue.Dequeue().([]weightedNode)

		// retrieve the last node from the path list
		node := path[len(path)-1]

		// check if the node has already been explored
		if !nodeInSlice(node, explored) {

			// add node to list of checked nodes
			explored = append(explored, node)

			// get neighbours
			neighbours, exists := graph[node.name]

			// if no neighbours ignore
			if exists {

				// go through all neighbour nodes
				for _, neighbour := range neighbours {

					// make a copy of the current path
					path1 := make([]weightedNode, len(path))
					copy(path1, path)

					// add this neighbour to the path
					path1 = append(path1, neighbour)

					// append path to solutions if neighbour is goal
					if neighbour.name == goal {
						solutions = append(solutions, path1)
					} else {
						// push it onto the queue for further exploration
						queue.Enqueue(path1)
					}
				}
			}
		}
	}

	// find the best path by summing the weights:
	bestPath := solutions[0]
	bestCost := 0
	for _, x := range bestPath {
		bestCost += x.weight
	}

	for i := 0; i < len(solutions); i++ {
		path := solutions[i]
		cost := 0
		for _, x := range path {
			cost += x.weight
		}
		if cost < bestCost {
			bestCost = cost
			bestPath = path
		}
	}

	// return the result
	return bestPath
}

func main() {

	// simple search space, represented by a dictionary
	graph := map[string][]string{
		"A": []string{"B", "C", "E"},
		"B": []string{"A", "D", "E"},
		"C": []string{"A", "F", "G"},
		"D": []string{"B", "E"},
		"E": []string{"A", "B", "D"},
		"F": []string{"C"},
		"G": []string{"C"},
	}

	result := bfsAllPaths(graph, "G", "D")
	fmt.Printf("Here's all the paths between nodes 'G' and 'D': %v\n", result)

	/*
		Q2) Can you add weights to the edges of our graph?
		I've implemented this using tuples. The second item is the weight of the edge.
		All weights are 1, except B to D which is 2. This should mean that G-C-A-E-D is chosen instead of G-C-A-B-D.
	*/
	weightedGraph := map[string][]weightedNode{
		"A": []weightedNode{{"B", 1}, {"C", 1}, {"E", 1}},
		"B": []weightedNode{{"A", 1}, {"D", 2}, {"E", 1}},
		"C": []weightedNode{{"A", 1}, {"F", 1}, {"G", 1}},
		"D": []weightedNode{{"B", 2}, {"E", 1}},
		"E": []weightedNode{{"A", 1}, {"B", 1}, {"D", 1}},
		"F": []weightedNode{{"C", 1}},
		"G": []weightedNode{{"C", 1}},
	}
	resultWeighted := bfsBestPath(weightedGraph, "G", "D")
	fmt.Printf("Here's the best path between nodes 'G' and 'D': %v\n", resultWeighted)
}
