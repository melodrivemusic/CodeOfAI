/*
Q1) Can you change the implementation to return all possible paths to the goal (rather than the shortest)?
*/
package main

import (
	"fmt"

	"github.com/golang-collections/collections/queue" // queue implementation has O(1) complexity for poping the first element,
	// Go standard library has no queue data structure implementation
)

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
}
