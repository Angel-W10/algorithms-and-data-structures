''' 
creating a union find data structute

''' 

class union_find():
    def __init__(self, N):
        # initialise a list (parents) of length n with all entries = index
        self.parents = list(range(0, N))

    def find(self, x):
        # returns the value of the parent until the value == parent
        if(self.parents[x]==x):
            return x
        self.find(self.parents[x])

    def union(self, x, y):

        # union (x, y) means we need to join x to y
        # we need to change the value of each value that has parent as x to having a parent y

        rootx, rooty = self.parents[x], self.parents[y]
        for i in self.parents:
            if(i==rootx):
                i=rooty
