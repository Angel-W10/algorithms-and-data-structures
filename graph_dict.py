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


    def BFS(self, v):
        # print(len(self.graph))
        visited = [-1]* (max(self.graph) + 1)
        q = []

        q.append(v)
        visited[v] = 1

        while(q):
            v = q.pop(0)
            print(v, end=" ")

            for n in self.graph[v]:
                if(visited[n]==-1):
                    q.append(n)
                    visited[n] = 1


if __name__ == "__main__":
    g = graph()
    g.add_vertex(0, 1)
    g.add_vertex(0, 2)
    g.add_vertex(1, 2)
    g.add_vertex(2, 0)
    g.add_vertex(2, 3)
    g.add_vertex(3, 3)
    print("DFS")
    g.DFS(2)
    print("\nBFS")
    g.BFS(2)
    print("\n")
