"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id in self.vertices:
            pass
        else:
            self.vertices[vertex_id] = set()
        return self

    def add_edge(self, v1, v2):
        if v2 in self.vertices[v1]:
            pass
        else:
            self.vertices[v1].add(v2)
        return self

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()

        while queue.size() > 0:
            current_vertex = queue.dequeue()
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    queue.enqueue(neighbor)

        return self

    def dft(self, starting_vertex):
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()

        while stack.size() > 0:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    stack.push(neighbor)

        return self

    def dft_recursive(self, starting_vertex):
        def helper(vertex, visited):
            print(vertex)
            visited.add(vertex)
            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    helper(neighbor, visited)

        helper(starting_vertex, set())

        return self

    def bfs(self, starting_vertex, destination_vertex):
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()

        while queue.size() > 0:
            current_path = queue.dequeue()
            current_vertex = current_path[-1]
            if current_vertex == destination_vertex:
                return current_path
            else:
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited:
                        new_path = current_path.copy()
                        new_path.append(neighbor)
                        queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()

        while stack.size() > 0:
            current_path = stack.pop()
            current_vertex = current_path[-1]
            if current_vertex == destination_vertex:
                return current_path
            else:
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited:
                        new_path = current_path.copy()
                        new_path.append(neighbor)
                        stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        def helper(path, visited):
            vertex = path[-1]

            if vertex == destination_vertex:
                return path
            else:
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        new_path = path.copy()
                        new_path.append(neighbor)
                        result = helper(new_path, visited)
                        if result:
                            return result

        return helper([starting_vertex], set())


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))
    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
