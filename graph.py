# A graph is a list of list and each index on the graph reprrsents a list of the adjecent vertices

# we give input like [source, destination] to add to the graph

# we create a class that would adjvertex

class adjVertex():
    def __init__(self, value):
        self.vertex = value
        self.next = None


# the graph class will initialise the the list of lists


class graph():
    def __init__(self, numV):
        self.numV = numV
        self.graph = [None] * self.numV


    def addEdge(self, src, des):
        # create a vertex for the destination
        # adding the vertex to the source position in the graph
        d = adjVertex(des)
        d.next = self.graph[src]
        self.graph[src] = d

        # adding the source
        s = adjVertex(src)
        s.next = self.graph[des]
        self.graph[des] = s


    # print all the vertices and their edges 
    def printGraph(self):
        for i in range(0, self.numV):
            # go through all the vertices
            # print the index because : the index number is equal to the vertex
            print("vertices at: {}\n head".format(i), end = "")
            # set temp = to the vertices that the vertix is connected to
            temp = self.graph[i]
            while(temp):
                # printing the connected vertices
                print(" -> {}".format(temp.vertex), end = "")
                temp = temp.next
            print("\n")


if __name__ == "__main__":
    g = graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 3)

    g.printGraph()