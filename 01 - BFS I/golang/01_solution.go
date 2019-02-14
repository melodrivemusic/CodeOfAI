/*
Package main has the golang implementation of Breadth First Search to find the shortest path

Q2) Can you change the BFS implementation in order to return the shortest path between the nodes
“G” and “D” of the example graph we"ve been using?

	See below for the implementation
*/
package main

import (
	"fmt"

	"github.com/golang-collections/collections/queue" // queue implementation has O(1) complexity for poping the first element,
	// Go standard library has no queue data structure implementation
)

// bfsShortestPath finds shortest path between 2 nodes in a graph using BFS
func bfsShortestPath(graph map[string][]string, start, goal string) []string {

	// set up a path list
	path := []string{start}

	// return a simple path if start is the goal
	if start == goal {
		return path
	}

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
			neighbours, exists := graph[node]

			// if no neighbours ignore
			if exists {

				// go through all neighbour nodes
				for _, neighbour := range neighbours {

					// make a copy of the current path
					path1 := make([]string, len(path))
					copy(path1, path)

					// add this neighbour to the path
					path1 = append(path1, neighbour)

					// return path if neighbour is goal
					if neighbour == goal {
						return path1
					}

					// push it onto the queue for further exploration
					queue.Enqueue(path1)
				}
			}
		}
	}

	// we couldn't find the goal... :(
	return nil

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

	// simple search space, represented by a map
	graph := map[string][]string{
		"A": []string{"B", "C", "E"},
		"B": []string{"A", "D", "E"},
		"C": []string{"A", "F", "G"},
		"D": []string{"B", "E"},
		"E": []string{"A", "B", "D"},
		"F": []string{"C"},
		"G": []string{"C"},
	}

	result := bfsShortestPath(graph, "G", "D")

	fmt.Printf("Here's the shortest path between nodes 'G' and 'D': %v\n", result)
}
