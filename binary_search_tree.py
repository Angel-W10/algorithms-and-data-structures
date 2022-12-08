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
    
    # delete function for the search tree
    def delete_node(self, value):
        r = self.root
        self.delete_helper(r, value)

    # helper function for the delete function for the binary search tree
    def delete_helper(self, root, value):
        if(root == None): # edge case
            return root
        # traversing to the value to delete
        elif (value < root.value):
            root.left = self.delete_helper(root.left, value)
        elif (value > root.value):
            root.right = self.delete_helper(root.right, value)

        # once we are at the value we go inside the else case 
        else:
            # if it is a leaf node or only a right child
            if(not root.left):
                temp = root.right
                del root
                return temp

            # if it only has a left child
            elif(not root.right):
                temp = root.left
                del root
                return temp

            # two children
            else:
                # in the else we take the minimum of the right subtree of the node
                # as it will replace the node to be deleted and still satisfy the conndition
                # of being smaller than all the elements to the right and 
                # larger than all the elements to the left
                temp = self.get_min(root.right)
                root.value = temp.value
                root.right = self.delete_helper(root.right, temp.value)

        return root
                
    def get_min(self, root):
        while(root.left != None):
            root = root.left
        return root


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