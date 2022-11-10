# graph using a dictionary, 
# a simpler way to implement the graph and also the algorithms on it

from collections import defaultdict

class graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def add_vertex(self, src, des):
        self.graph[src].append(des)

    def DFS(self, v):
        visited = []
        self.DFS_helper(v, visited)

    def DFS_helper(self, v, visited):
        visited.append(v)
        print(v, end=" ")

        for n in self.graph[v]:
            if n not in visited:
                self.DFS_helper(n, visited)



if __name__ == "__main__":
    g = graph()
    g.add_vertex(0, 1)
    g.add_vertex(0, 2)
    g.add_vertex(1, 2)
    g.add_vertex(1, 3)
    g.add_vertex(2, 4)
    g.add_vertex(3, 4)

    g.DFS(0)
