# creating a Node class to act as nodes in the tree
class node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

# creating a tree class to create a root node in the init function
class tree():
    def __init__(self, val = None):
        self.root = node(val)
    
    # function to insert node
    def insert_node(self, val):
        temp = self.root
        return self.insert_node_helper(temp, val)
    
    # helper function to get insert node
    def insert_node_helper(self, root, val):
        if(val==None):
            return False

        if(root==None):
            return False
        else:
            temp = root
            if(val<temp.value):
                if(temp.left == None):
                    temp.left = node(val)
                else:
                    return self.insert_node_helper(temp.left, val)
            if(val>temp.value):
                if(temp.right == None):
                    temp.right = node(val)
                else:
                    return self.insert_node_helper(temp.right, val)

    # printing the tree in order
    def print_in_order(self):
        if(self.root):
            trav = [] # array to store the values
            temp = self.root
            return self.print_in_order_helper(temp, trav)
        return "" # return empty string if root = none


    # helper function for the print in order function
    def print_in_order_helper(self, root, trav):
        temp = root
        trav.append(temp.value) # appending the value to the trav list

        if(temp.left):
            self.print_in_order_helper(temp.left, trav)

        if(temp.right):
            self.print_in_order_helper(temp.right, trav)

        return trav


    # printing the tree pre order
    def print_pre_order(self):
        if(self.root):
            trav = [] # array to store the values
            temp = self.root
            return self.print_pre_order_helper(temp, trav)
        return "" # return empty string if root = none


    # helper function for the print in order function
    def print_pre_order_helper(self, root, trav):
        temp = root
        if(temp.left):
            self.print_pre_order_helper(temp.left, trav)

        trav.append(temp.value) # appending the value to the trav list

        if(temp.right):
            self.print_pre_order_helper(temp.right, trav)

        return trav




if __name__ == "__main__":
    t = tree(7)
    t.insert_node(5)
    t.insert_node(3)
    t.insert_node(1)
    t.insert_node(2)
    t.insert_node(6)
    t.insert_node(10)
    t.insert_node(8)
    t.insert_node(9)

    print(t.print_in_order())
    print(t.print_pre_order())