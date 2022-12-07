# creating a graph using adjencey matrix

class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = [[0 for col in range(self.v)] for row in range(self.v)]


    # function to get the next closest 
    def min_dist(self, dist, visited):
        min = 1e8
        for v in range(self.v):
            if(dist[v]<min and visited[v]==False):
                min = dist[v]
                min_index = v
        return min_index

    def dijkstras(self, src):
        # an array of distances
        dist = [1e8]*self.v

        #an array of if the vertex is visited
        visited = [False]*self.v

        dist[src] = 0


        for _ in range(self.v):

            u = self.min_dist(dist, visited)

            visited[u] = True

            for v in range(self.v):
                if(self.graph[u][v] > 0 and visited[v] == False and dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        return dist



if __name__ == "__main__":
   g = Graph(9)
   g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
   [4, 0, 8, 0, 0, 0, 0, 11, 0],
   [0, 8, 0, 7, 0, 4, 0, 0, 2],
   [0, 0, 7, 0, 9, 14, 0, 0, 0],
   [0, 0, 0, 9, 0, 10, 0, 0, 0],
   [0, 0, 4, 14, 10, 0, 2, 0, 0],
   [0, 0, 0, 0, 0, 2, 0, 1, 6],
   [8, 11, 0, 0, 0, 0, 1, 0, 7],
   [0, 0, 2, 0, 0, 0, 6, 7, 0]
   ]

   print(g.dijkstras(0))