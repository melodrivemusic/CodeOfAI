"""
Q1) Can you change the implementation to return all possible paths to the goal (rather than the shortest)?
"""

def bfsAllPaths(graph, start, goal):
    """Finds all paths between 2 nodes in a graph using BFS

    Args:
        graph (dict): Search space represented by a graph
        start (str): Starting state
        goal (str): Goal state

    Returns:
        solutions (list): List of the paths that bring you from the start to
            the goal state
    """

    # set up a path list
    path = [start]

    # return a simple path if start is the goal
    if start == goal:
        return path

    # keep track of all solutions
    solutions = []

    # list to keep track of all visited nodes
    explored = []

    # the FIFO queue
    queue = []

    # add the first path to the queue
    queue.append(path)

    # keep looping until there are no nodes still to be checked
    while len(queue) > 0:

        # pop first item from queue (FIFO)
        path = queue.pop(0)

        # retrieve the last node from the path list
        node = path[-1]

        # check if the node has already been explored
        if node not in explored:

            # add node to list of checked nodes
            explored.append(node)

            # get neighbours if node is present, otherwise default to empty list
            neighbours = graph.get(node, [])

            # go through all neighbour nodes
            for neighbour in neighbours:
                # make a copy of the current path
                path1 = path[:]

                # add this neighbour to the path
                path1.append(neighbour)

                # append path to solutions if neighbour is goal
                if neighbour == goal:
                    solutions.append(path1)
                else:
                    # push it onto the queue for further exploration
                    queue.append(path1)

    # we couldn't find the goal... :(
    return solutions

"""
Q3) Can you find the path with the lowest cumulative weight?
"""

def bfsBestPath(graph, start, goal):
    """Finds the best path (lowest weight) between 2 nodes in a graph using BFS

    Args:
        graph (dict): Search space represented by a weighted graph
        start (str): Starting state
        goal (str): Goal state

    Returns:
        path (list): List of the states that bring you from the start to
            the goal state, in the best way possible
    """

    # set up a path list
    path = [(start, 0)]

    # return a simple path if start is the goal
    if start == goal:
        return path

    # keep track of all solutions
    solutions = []

    # list to keep track of all visited nodes
    explored = []

    # the FIFO queue
    queue = []

    # add the first path to the queue
    queue.append(path)

    # keep looping until there are no nodes still to be checked
    while len(queue) > 0:

        # pop first item from queue (FIFO)
        path = queue.pop(0)

        # retrieve the last node from the path list
        node = path[-1][0]

        # check if the node has already been explored
        if node not in explored:

            # add node to list of checked nodes
            explored.append(node)

            # get neighbours if node is present, otherwise default to empty list
            neighbours = graph.get(node, [])

            # go through all neighbour nodes
            for neighbour in neighbours:
                # make a copy of the current path
                path1 = path[:]

                # add this neighbour to the path
                path1.append(neighbour)

                # append path to solutions if neighbour is goal
                if neighbour[0] == goal:
                    solutions.append(path1)
                else:
                    # push it onto the queue for further exploration
                    queue.append(path1)

    # find the best path by summing the weights:
    bestPath = solutions[0]
    bestCost = sum([x[1] for x in bestPath])

    for i in range(1, len(solutions)):
        path = solutions[i]
        cost = sum([x[1] for x in path])
        if cost < bestCost:
            bestCost = cost
            bestPath = path

    # we couldn't find the goal... :(
    return bestPath

if __name__ == "__main__":

    # simple search space, represented by a dictionary
    graph = {
        "A": ["B", "C", "E"],
        "B": ["A", "D", "E"],
        "C": ["A", "F", "G"],
        "D": ["B", "E"],
        "E": ["A", "B", "D"],
        "F": ["C"],
        "G": ["C"]
    }

    result = bfsAllPaths(graph, "G", "D")
    print("Here's all the paths between nodes \"G\" and \"D\": {}".format(result))

    """
    Q2) Can you add weights to the edges of our graph?
        I've implemented this using tuples. The second item is the weight of the edge.
        All weights are 1, except B to D which is 2. This should mean that G-C-A-E-D is chosen instead of G-C-A-B-D.
    """

    weightedGraph = {
        "A": [("B", 1), ("C", 1), ("E", 1)],
        "B": [("A", 1), ("D", 2), ("E", 1)],
        "C": [("A", 1), ("F", 1), ("G", 1)],
        "D": [("B", 2), ("E", 1)],
        "E": [("A", 1), ("B", 1), ("D", 1)],
        "F": [("C", 1)],
        "G": [("C", 1)]
    }

    result = bfsBestPath(weightedGraph, "G", "D")
    print("Here's the best path between nodes \"G\" and \"D\": {}".format(result))
