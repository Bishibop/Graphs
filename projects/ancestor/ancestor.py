import sys
import math
sys.path.append('../graph')
from graph import Graph
from util import Queue  # These may come in handy


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for ancestor in ancestors:
        graph.add_vertex(ancestor[0])
        graph.add_vertex(ancestor[1])
        graph.add_edge(ancestor[1], ancestor[0])
    if not graph.get_neighbors(starting_node):
        return -1

    queue = Queue()
    queue.enqueue((starting_node, 0))
    visited = set()
    oldest_ancestors = []
    while queue.size() > 0:
        current_vertex = queue.dequeue()
        if current_vertex not in visited:
            visited.add(current_vertex)
            neighbors = graph.get_neighbors(current_vertex[0])
            if neighbors:
                for neighbor in neighbors:
                    queue.enqueue((neighbor, current_vertex[1] + 1))
            else:
                oldest_ancestors.append(current_vertex)

    oldest = (math.inf, -1)
    for ancestor in oldest_ancestors:
        if ancestor[1] > oldest[1]:
            oldest = ancestor
        elif ancestor[1] == oldest[1] and ancestor[0] < oldest[0]:
            oldest = ancestor
        else:
            pass
    return oldest[0]
