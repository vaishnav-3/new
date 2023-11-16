from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=' ')

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs_recursive(neighbor, visited)

    def dfs(self, start_vertex):
        visited = [False] * len(self.graph)
        print("Depth-First Search (DFS):")
        self.dfs_recursive(start_vertex, visited)
        print()

    def bfs(self, start_vertex):
        visited = [False] * len(self.graph)
        queue = [start_vertex]
        visited[start_vertex] = True

        print("Breadth-First Search (BFS):")
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex, end=' ')

            for neighbor in self.graph[current_vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        print()

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

start_vertex = 0

g.dfs(start_vertex)
g.bfs(start_vertex)
