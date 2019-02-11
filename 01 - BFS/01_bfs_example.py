def bfs(graph, start):
    """Visits all the nodes of a graph using BFS

    Args:
        graph (dict): Search space represented by a graph
        start (str): Starting state

    Returns:
        explored (list): List of the explored nodes
    """

    # list to keep track of all visited nodes
    explored = []

    # the FIFO queue
    queue = []

    # add the start node to the queue
    queue.append(start)

    # keep looping until there are no nodes still to be checked
    while len(queue) > 0:

        # pop first item from queue (FIFO)
        node = queue.pop(0)

        # check if the node has already been explored
        if node not in explored:

            # add node to list of checked nodes
            explored.append(node)

            # get neighbours if node is present, otherwise default to empty list
            neighbours = graph.get(node, [])

            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)

    # return the explored nodes
    return explored
