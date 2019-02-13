"""
Q1) Implement the FIFO queue using the deque object from the collections module.
    What is the benefit of doing this?

See below for the implementation. The benefit is really in optimisation.
popleft() will result in a quicker code, as it has a time complexity of O(1) while pop(0) has O(n).

Q2) Can you change the BFS implementation in order to return the shortest path between the nodes “G” and “D”
    of the example graph we"ve been using?

See below for the implementation
"""

from collections import deque


def bfsShortestPath(graph, start, goal):
    """Finds shortest path between 2 nodes in a graph using BFS

    Args:
        graph (dict): Search space represented by a graph
        start (str): Starting state
        goal (str): Goal state

    Returns:
        path (list): List of the states that bring you from the start to
            the goal state, in the quickest way possible
    """

    # return a simple path if start is the goal
    if start == goal:
        return [start]

    # list to keep track of all visited nodes
    explored = []

    # the FIFO queue
    queue = deque()

    # add the first path to the queue
    queue.append([start])

    # keep looping until there are no nodes still to be checked
    while len(queue) > 0:

        # pop first item from queue (FIFO)
        path = queue.popleft()

        # retrieve the node from the path list
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

                # return path if neighbour is goal
                if neighbour == goal:
                    return path1

                # push it onto the queue for further exploration
                queue.append(path1)

    # we couldn't find the goal... :(
    return None


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

    result = bfsShortestPath(graph, "G", "D")

    print("Here's the shortest path between nodes \"G\" and \"D\": {}".format(result))
